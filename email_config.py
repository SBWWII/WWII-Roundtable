from fastapi_mail import ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="sbwwiiroundtable@gmail.com",
    MAIL_PASSWORD="tsbqnufpstkswmwp",  # ✅ Closing quote fixed
    MAIL_FROM="sbwwiiroundtable@gmail.com",  # ✅ Should match MAIL_USERNAME
    MAIL_PORT=465,  # ✅ SSL port
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=False,  # ✅ STARTTLS disabled
    MAIL_SSL_TLS=True,  # ✅ SSL/TLS enabled
    USE_CREDENTIALS=True
)