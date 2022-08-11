import smtplib

def send_mail():
    try:
        email_server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
        email_server.login("namelessmonsterel0@yandex.com","12345isg")
        email_server.sendmail("namelessmonsterel0@yandex.com","namelessmonsterel0@yandex.com","test")
        email_server.quit()
        email_server.quit()
    except:
        pass
send_mail()