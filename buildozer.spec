[app]
# نام برنامه شما
title = CCTV Bot
package.name = cctvbot
package.domain = org.test

# مسیر فایل‌های برنامه (نقطه یعنی همین پوشه)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# نسخه برنامه
version = 0.1

# کتابخانه‌های پایتون که باید نصب شوند
requirements = python3,kivy,requests,pyjnius,urllib3

# دسترسی‌های اندروید
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# تنظیمات نسخه اندروید و معماری پردازنده
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
