import email
import os
import smtplib
from email.message import EmailMessage

#Configuração do Email e Senha

EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''

#Criação do Email

msg = EmailMessage()
msg['Subject'] = ''
msg['From'] = ''
msg['To'] = ''
msg.set_content('')

#Enviar Email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
