import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from ..config.config import config


def mail(path_doc):

    app_config = config()

    email_from = app_config['MAIL']['EMAIL_FROM']
    email_to = app_config['MAIL']['EMAIL_TO']
    subject = app_config['MAIL']['SUBJECT']
    email_password = app_config['MAIL']['EMAIL_PASSWORD']

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    body = app_config['MAIL']['BODY']
    msg.attach(MIMEText(body, 'plain'))

    filename = path_doc
    attachment = open(filename, 'rb')

    part = MIMEBase('application', "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)

    name_sheet = app_config['NAME_SHEET']

    part.add_header('Content-Disposition',
                    f'attachment; filename="{name_sheet}.xlsx"')

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, email_password)

    server.sendmail(email_from, email_to, text)
    server.quit()


def message(path_doc, body, subject, name_sheet):

    app_config = config()

    email_from = app_config['MAIL']['EMAIL_FROM']
    email_to = app_config['MAIL']['EMAIL_TO']
    email_password = app_config['MAIL']['EMAIL_PASSWORD']

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    filename = path_doc
    attachment = open(filename, 'rb')

    part = MIMEBase('application', "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header('Content-Disposition',
                    f'attachment; filename="{name_sheet}.xlsx"')

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, email_password)

    server.sendmail(email_from, email_to, text)
    server.quit()
