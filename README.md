# فرم ثبت اطلاعات افراد ملاقات کننده با همکاران دانشگاه جامع علمی کاربردی واحد استان خراسان رضوی

این پروژه یک فرم آنلاین برای ثبت اطلاعات ملاقات کنندگان با همکاران دانشگاه جامع علمی کاربردی واحد استان خراسان رضوی است. این فرم با استفاده از Streamlit توسعه داده شده و اطلاعات ورودی را در Google Sheets ذخیره می‌کند.

## ویژگی‌ها

ثبت اطلاعات ملاقات کنندگان شامل نام، نام خانوادگی، کد ملی، تلفن تماس و آدرس.

اعتبارسنجی ورودی‌ها و نمایش پیام‌های خطا در صورت ناقص بودن اطلاعات.

محدودیت ثبت اطلاعات تنها در روزهای دوشنبه.

جلوگیری از ثبت کد ملی تکراری.

ذخیره اطلاعات ثبت شده در Google Sheets.

## پیش‌نیازها

Python 3.7 یا بالاتر

کتابخانه‌های مورد نیاز:

``` bash
pip install streamlit streamlit_gsheets pandas khayyam
```

## نحوه اجرا
1. مطمئن شوید که پیش‌نیازها نصب شده‌اند.

2. کلید API را در کنسول ابری گوگل ایجاد کنید و در Google Sheet خود اجازه دسترسی دهید.

3. فایل Secrets.toml را در پوشه streamlit. در ریشه پروژه بر اساس فایل API Key json که در کنسول ابری گوگل ایجاد کردید، ایجاد کنید.

```bash
[secrets]

[connections.gsheets]
spreadsheet = "YOUR_SPREADSHEET_URL"
worksheet = "YOUR_WORKSHEET_GID"
type= "service_account"
project_id = "YOUR_PROJECT_ID"
private_key_id = "YOUR_PRIVATE_KEY_ID"
private_key = "YOUR_PRIVATE_KEY"
client_email = "YOUR_CLIENT_EMAIL"
client_id = "YOUR_CLIENT_ID"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/streamlit-gsheets%40api-class-423418.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

4. فایل CSS استایل‌ها (app/style.css) را در مسیر مربوطه قرار دهید.

5. برنامه را با استفاده از دستور زیر اجرا کنید:

``` bash
streamlit run app.py
```

## ساختار پروژه

`app.py`: فایل اصلی برنامه که منطق فرم و ثبت اطلاعات را مدیریت می‌کند.

`app/style.css`: فایل استایل‌ها برای زیباسازی فرم.

## نحوه استفاده

فرم شامل فیلدهای نام، نام خانوادگی، کد ملی، تلفن تماس و آدرس است. لطفاً همه فیلدها را تکمیل کنید.

تنها در روزهای دوشنبه امکان ثبت اطلاعات وجود دارد.

پس از تکمیل فرم و فشردن دکمه "ثبت اطلاعات"، اطلاعات شما بررسی و در صورت صحت، در Google Sheets ذخیره خواهد شد.

در صورتی که کد ملی شما قبلاً ثبت شده باشد، پیام خطا نمایش داده می‌شود.

## توسعه‌دهندگان

این پروژه توسط [مهدی سالاری](https://github.com/MehdiSlr/) ایجاد شده است. برای اطلاعات بیشتر یا پیشنهادات، با ما تماس بگیرید.