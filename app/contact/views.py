import os
from flask import render_template, request, flash
from . import contact
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")


@contact.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        # お問い合わせ内容の控えメールオブジェクトを作成
        confirmation_message = Mail(
            from_email=FROM_EMAIL,
            to_emails=email,
            subject="お問い合わせ内容の控え(" + subject + ")",
            html_content=f"""
                <p>こんにちは、{name}様。</p>
                <p>お問い合わせいただきありがとうございます！以下に、お問い合わせ内容の控えをお送りします。</p>
                <p>お名前: {name}<br>
                メールアドレス: {email}<br>
                お問い合わせ内容:<br>
                {message}</p>
                <p>できるだけ早く対応させていただきますので、お待ちいただけると幸いです。</p>
                <p>引き続きよろしくお願いいたします。</p>
                <p>うまみちゃん</p>
                        """,
        )


        # SendGridメールオブジェクトの作成
        sendgrid_message = Mail(
            from_email=FROM_EMAIL,
            to_emails=TO_EMAIL,
            subject=subject,
            html_content=f"""
                <p>{name}様からのお問い合わせ</p>
                メールアドレス: {email}<br>
                お問い合わせ内容:<br>
                {message}</p>
                        """,
        )


        try:
            # SendGrid APIクライアントの作成
            sendgrid_client = SendGridAPIClient(api_key=SENDGRID_API_KEY)

            # メール送信
            sendgrid_client.send(sendgrid_message)
            sendgrid_client.send(confirmation_message)  # 問い合わせ者に控えメールを送信
            flash("お問い合わせが送信されました。ありがとうございます！", "success")
        except Exception as e:
            print(e)
            flash("お問い合わせの送信中にエラーが発生しました。もう一度お試しください。"+str(e), "error")

    return render_template("contact/contact.html")
