# from email.mime.image import MIMEImage
# import mimetypes
# import smtplib
# import base64
# import models
# import os.path
# import os
from datetime import datetime

# import smtplib
# import ssl
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from email.utils import formatdate
# from email import encoders


# def send_mail(send_from, send_to, subject, text, files, server, port, username='', password='', isTls=True):
#     msg = MIMEMultipart()
#     msg['From'] = send_from
#     msg['To'] = send_to
#     msg['Date'] = formatdate(localtime=True)
#     msg['Subject'] = subject
#     msg.attach(MIMEText(text))

#     part = MIMEBase('application', "octet-stream")
#     part.set_payload(open("WorkBook3.xlsx", "rb").read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition',
#                     'attachment; filename="WorkBook3.xlsx"')
#     msg.attach(part)

#     #context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
#     # SSL connection only working on Python 3+
#     smtp = smtplib.SMTP(server, port)
#     if isTls:
#         smtp.starttls()
#     smtp.login(username, password)
#     smtp.sendmail(send_from, send_to, msg.as_string())
#     smtp.quit()


# #!/usr/bin/env python


# class Mail():
#     def __init__(self, parent):
#         self.parent = parent
#         self.db = self.parent.application.settings['db']
#         self.user = 'Foo'
#         self.password = 'MYPASSWORD'
#         self.to = 'foo@bar.com'
#         self.fromx = 'for@bar.com'

#     def send(self, files=False):

#         msg = MIMEMultipart()
#         msg['Subject'] = 'Excel'

#         msg['From'] = 'foo@bar.com'
#         msg['To'] = 'foo@bar.com'
#         msg.preamble = 'excel test'

#         filename = 'test_file.xls'

#         fp = open('tmp/'+filename, 'rb')
#         xls = MIMEBase('application', 'vnd.ms-excel')
#         xls.set_payload(fp.read())
#         fp.close()
#         encoders.encode_base64(xls)
#         xls.add_header('Content-Disposition', 'attachment', filename=filename)
#         msg.attach(xls)

#         s = smtplib.SMTP('bar.com:26')
#         s.ehlo
#         s.login(self.user, self.password)
#         s.sendmail(self.to, self.fromx, msg.as_string())
#         s.close()


def get_data_now():
    now = datetime.now()
    years = now.year
    month = now.month-1

    d = dict()

    d["now"] = now
    d["years"] = years
    d["month"] = month

    return d
