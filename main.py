import threading
import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass

# --- تنظیمات تلگرام ---
# توکن رباتی که از BotFather گرفته‌اید را اینجا بگذارید
BOT_TOKEN = "8911654965:AAGkY8QXu3FW4re4FQPz3QzzJIv1YpXWn5Y"
# چت آیدی خودتان (از userinfobot گرفته‌اید) را اینجا بگذارید
ADMIN_CHAT_ID = "137721326"

class CCTVApp(App):
    def build(self):
        self.status_label = Label(text="CCTV Bot is Running...\nWaiting for commands.")
        # شروع Thread برای بررسی پیام‌های تلگرام بدون فریز شدن برنامه
        threading.Thread(target=self.poll_telegram, daemon=True).start()
        return self.status_label

    def poll_telegram(self):
        offset = 0
        while True:
            try:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}&timeout=10"
                response = requests.get(url, timeout=15).json()
                
                if response.get("ok"):
                    for result in response["result"]:
                        offset = result["update_id"] + 1
                        message = result.get("message", {})
                        chat_id = str(message.get("chat", {}).get("id", ""))
                        text = message.get("text", "")

                        # بررسی اینکه آیا پیام از طرف شماست
                        if chat_id == ADMIN_CHAT_ID:
                            if text == "/photo":
                                self.update_ui("Command received: /photo\nTaking picture...")
                                self.take_photo()
                            elif text == "/video":
                                self.update_ui("Command received: /video\nRecording video...")
                                # تابع ضبط ویدیو را اینجا صدا می‌زنیم
            except Exception as e:
                pass

    def update_ui(self, text):
        # بروزرسانی رابط کاربری Kivy در Thread اصلی
        Clock.schedule_once(lambda dt: self._set_label_text(text))

    def _set_label_text(self, text):
        self.status_label.text = text

    def take_photo(self):
        # کدهای Pyjnius برای دسترسی به دوربین اندروید در اینجا قرار می‌گیرد
        # برای سادگی در قدم اول، فقط پیام موفقیت به تلگرام می‌فرستیم
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": ADMIN_CHAT_ID, "text": "Camera accessed (simulated). Photo will be sent here."})

if __name__ == '__main__':
    CCTVApp().run()
