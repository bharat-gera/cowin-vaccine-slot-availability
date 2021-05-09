import smtplib
import config

def send_mail(data):

    sent_from = 'VACCINE Available MESSAGE'
    subject = 'OMG Super Important Message'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(config.TO_USERS), subject, data)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(config.GMAIL_USER, config.GMAIL_PASSWORD)
    server.sendmail(sent_from, config.TO_USERS, email_text)
    server.close()

    config.logger.info('Email sent!')
