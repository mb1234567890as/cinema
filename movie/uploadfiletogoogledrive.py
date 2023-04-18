from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'googleky.json')
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=creds)






































# import smtplib

# from django.conf import settings


# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Настраиваем подключение к smtp серверу
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_username = settings.GMAIL
# smtp_password = settings.GMAIL_PASSWORD
# smtp_do_tls = True

# # Создаем объект подключения к серверу
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()
# server.login(smtp_username, smtp_password)

# # Создаем объект сообшения
# msg = MIMEMultipart()
# # msg['From'] = smtp_username
# msg['To'] = 'bekjan02003@gmail.com'
# msg['Subject'] = 'Тема сощбшение'
# body = 'Текст сообшеие в формате plain text'
# msg.attach(MIMEText(body, 'plain'))

# # Отправляем сообшение
# server.send_message(msg)
# server.quit()

