import os
import ssl
import certifi
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

# 🔥 SSL FIX
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
def send_otp_email(receiver_email, otp):

    api_key = os.getenv("SENDGRID_API_KEY")
    sender_email = os.getenv("SENDER_EMAIL")

    print("API KEY:", api_key)
    print("FROM:", sender_email)
    print("TO:", receiver_email)

    message = Mail(
        from_email=sender_email,
        to_emails=receiver_email,
        subject="Your OTP Code",
        html_content = f"""
<div style="font-family: Arial, sans-serif; background-color:#f4f4f4; padding:20px;">
    
    <div style="max-width:500px; margin:auto; background:white; padding:30px; border-radius:10px; box-shadow:0 0 10px rgba(0,0,0,0.1);">
        
        <h2 style="text-align:center; color:#4CAF50;">🔐 OTP Verification</h2>
        
        <p style="font-size:16px; color:#333;">
            Hello,
        </p>

        <p style="font-size:15px; color:#555;">
            Use the following OTP to complete your verification. This OTP is valid for <b>5 minutes</b>.
        </p>

        <div style="text-align:center; margin:30px 0;">
            <span style="font-size:28px; letter-spacing:5px; font-weight:bold; color:#000;">
                {otp}
            </span>
        </div>

        <p style="font-size:14px; color:#777;">
            If you did not request this, please ignore this email.
        </p>

        <hr style="margin:20px 0;">

        <p style="text-align:center; font-size:12px; color:#aaa;">
            © 2026 Career AI System 🚀
        </p>

    </div>
</div>
"""
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)

        print("✅ STATUS:", response.status_code)

    except Exception as e:
        print("❌ ERROR:", str(e))