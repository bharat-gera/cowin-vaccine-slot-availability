import smtplib
from config import logger

def send_mail(data):

    sent_from = 'VACCINE Available MESSAGE'
    subject = 'OMG Super Important Message'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(TO_USERS), subject, data)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(sent_from, TO_USERS, email_text)
    server.close()

    logger.info('Email sent!')
