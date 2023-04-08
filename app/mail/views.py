import os
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from flask import Flask, render_template, request, flash, redirect, url_for
from . import mail

MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")


@mail.route("/")
def contact():
    return render_template("mail/contact.html")


@mail.route("/send_email", methods=["POST"])
def send_email():
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = subject
    msg["From"] = MAIL_USERNAME
    msg["To"] = email

    try:
        with smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT) as server:
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            server.send_message(msg)
        flash("メールが送信されました", "success")
    except Exception as e:
        print(e)
        flash("メールの送信に失敗しました", "error")

    return redirect(url_for("mail.contact"))
