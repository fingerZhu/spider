import smtplib
from email.mime.text import MIMEText

msg = MIMEText("hello")

msg["Subject"] = "personal test"
msg["From"] = "finger_zhu@qq.com"
msg["To"] = "finger_zhu@qq.com"

s = smtplib.SMTP("smtp.qq.com", 587)
s.starttls()
s.login("finger_zhu@qq.com", "dgpjykityizkbdeg")
for i in range(4):
    s.send_message(msg)
s.quit()
