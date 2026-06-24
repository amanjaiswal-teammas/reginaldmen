import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr, make_msgid

from fastapi import File, UploadFile

from ..config import settings
from typing import Optional, List
import logging
from email.mime.base import MIMEBase
from email import encoders
import requests
from sendgrid import SendGridAPIClient
import base64


logger = logging.getLogger(__name__)


MAX_ATTACHMENT_SIZE_MB = 25
MAX_ATTACHMENT_SIZE = MAX_ATTACHMENT_SIZE_MB * 1024 * 1024


# def send_mail(
#     to_email: str,
#     subject: str,
#     body: str,
#     cc_emails: Optional[list] = None,
#     bcc_emails: Optional[list] = None,
#     attachments: Optional[List[UploadFile]] = None,
#     in_reply_to: Optional[str] = None
# ) -> Optional[str]:
#     """
#     Send email via SMTP and return Message-ID.
#     Supports threading with In-Reply-To and References headers.
#     """
#     try:
#         # Create message
#         msg = MIMEMultipart()
#         msg['From'] = formataddr(("Support", settings.SMTP_FROM))
#         msg['To'] = to_email
#         msg['Subject'] = subject
#
#         # Add CC if provided
#         if cc_emails:
#             msg['Cc'] = ', '.join(cc_emails)
#
#         # Generate Message-ID
#         message_id = make_msgid()
#         msg['Message-ID'] = message_id
#
#         # Set threading headers if replying
#         if in_reply_to:
#             msg['In-Reply-To'] = in_reply_to
#             msg['References'] = in_reply_to
#
#         # Add body
#         body_part = MIMEMultipart("alternative")
#
#         # Plain fallback
#         body_part.attach(MIMEText("Please view this email in HTML format.", "plain", "utf-8"))
#
#         # HTML content
#         html_body = body.replace("\n", "<br>")
#         body_part.attach(MIMEText(html_body, "html", "utf-8"))
#
#         msg.attach(body_part)
#
#         # Attach files
#         if attachments and isinstance(attachments, list):
#             for file in attachments:
#
#                 file_data = file.file.read()
#                 file.file.seek(0)
#
#                 # Validate size under 25MB
#                 if len(file_data) > MAX_ATTACHMENT_SIZE:
#                     raise Exception(f"Attachment {file.filename} exceeds 25MB limit")
#
#                 # Detect file type
#                 maintype, subtype = file.content_type.split("/", 1)
#
#                 part = MIMEBase(maintype, subtype)
#                 part.set_payload(file_data)
#                 encoders.encode_base64(part)
#                 part.add_header(
#                     "Content-Disposition",
#                     f'attachment; filename="{file.filename}"'
#                 )
#                 msg.attach(part)
#
#         # Connect to SMTP server
#         # if settings.SMTP_USER:
#         #     server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=30)
#         #     server.ehlo()
#         #     server.starttls()
#         #     server.ehlo()
#         #     server.login(settings.SMTP_USER, settings.SMTP_PASS)
#         # else:
#         #     server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
#
#         # Prepare all recipients (To + CC + BCC)
#         all_recipients = [to_email]
#         if cc_emails:
#             all_recipients.extend(cc_emails)
#         if bcc_emails:
#             all_recipients.extend(bcc_emails)
#
#         # Send email
#         text = msg.as_string()
#
#         # Send via Mailgun API
#         # response = requests.post(
#         #     f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages.mime",
#         #     auth=("api", settings.API_KEY),
#         #     data={"to": all_recipients},
#         #     files=[("message", ("message.mime", text.encode("utf-8")))]
#         # )
#         #
#         # if response.status_code != 200:
#         #     raise Exception(f"Mailgun error: {response.text}")
#
#         # server.sendmail(settings.SMTP_FROM, all_recipients, text)
#         # server.quit()
#
#         encoded_message = base64.b64encode(text.encode("utf-8")).decode()
#
#         sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
#
#         personalization = {
#             "to": [{"email": to_email}]
#         }
#
#         if cc_emails:
#             personalization["cc"] = [{"email": cc} for cc in cc_emails]
#
#         if bcc_emails:
#             personalization["bcc"] = [{"email": bcc} for bcc in bcc_emails]
#
#         if in_reply_to:
#             personalization["headers"] = {
#                 "In-Reply-To": in_reply_to,
#                 "References": in_reply_to
#             }
#
#         response = sg.client.mail.send.post(request_body={
#             "personalizations": [personalization],
#             "from": {"email": settings.SMTP_FROM},
#             "subject": subject,
#             "content": [
#                 {
#                     "type": "text/html",
#                     "value": html_body
#                 }
#             ]
#         })
#
#         logger.info(f"Email sent successfully to {to_email} (CC: {cc_emails}, BCC: {bcc_emails})")
#         return message_id.strip('<>')  # Remove angle brackets
#
#     except Exception as e:
#         logger.error(f"Failed to send email to {to_email}: {str(e)}")
#         return None








import os
# import requests
# from ..config import settings

# def send_simple_message():
#
#   	return requests.post(
#   		"https://api.mailgun.net/v3/mg.thechemistcompany.com/messages",
#   		auth=("api", settings.API_KEY),
#   		data={"from": "<info@thechemistcompany.com>",
# 			"to": "<amanjaiswal1412000@gmail.com>",
#   			"subject": "Hello mas itsupport",
#   			"text": "Congratulations, you just sent an email with Mailgun!"})



import os
# import requests
# def send_simple_message():
#   	return requests.post(
#   		"https://api.mailgun.net/v3/mg.reginaldmen.com/messages",
#   		auth=("api", settings.API_KEY),
#   		data={"from": "<info@reginaldmen.com>",
# 			"to": "<amanjaiswal1412000@gmail.com>",
#   			"subject": "Hello mas itsupport",
#   			"text": "Congratulations mas itsupport, you just sent an email with Mailgun! You are truly awesome!"})





from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Cc, Bcc, HtmlContent, PlainTextContent, Attachment, Header
import base64


def send_mail(
    to_email: str,
    subject: str,
    body: str,
    cc_emails: Optional[list] = None,
    bcc_emails: Optional[list] = None,
    attachments: Optional[List[UploadFile]] = None,
    in_reply_to: Optional[str] = None
) -> Optional[str]:

    try:
        # Create SendGrid Mail object
        message = Mail(
            from_email=Email(settings.SMTP_FROM, "Support"),
            to_emails=To(to_email),
            subject=subject,
            html_content=HtmlContent(body.replace("\n", "<br>"))
        )

        # Plain text fallback
        message.plain_text_content = PlainTextContent(body)

        # CC
        if cc_emails:
            for cc in cc_emails:
                message.add_cc(Cc(cc))

        # BCC
        if bcc_emails:
            for bcc in bcc_emails:
                message.add_bcc(Bcc(bcc))

        # Threading headers
        if in_reply_to:
            message.add_header(Header("In-Reply-To", in_reply_to))
            message.add_header(Header("References", in_reply_to))

        # if in_reply_to:
        #     message.personalizations[0].headers = {
        #         "In-Reply-To": in_reply_to,
        #         "References": in_reply_to
        #     }

        # Attachments
        if attachments:
            for file in attachments:
                file_data = file.file.read()
                file.file.seek(0)

                if len(file_data) > MAX_ATTACHMENT_SIZE:
                    raise Exception(f"{file.filename} exceeds 25MB limit")

                encoded = base64.b64encode(file_data).decode()

                attachment = Attachment(
                    file_content=encoded,
                    file_type=file.content_type,
                    file_name=file.filename,
                    disposition="attachment"
                )

                message.add_attachment(attachment)

        # Send email
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

        # Retry logic
        response = None
        for attempt in range(3):
            try:
                response = sg.send(message)
                break
            except Exception as e:
                if attempt == 2:
                    raise
                logger.warning(f"SendGrid retry {attempt + 1} failed: {str(e)}")

        # Validate response
        if response.status_code >= 400:
            logger.error(f"SendGrid error: {response.body}")
            raise Exception(f"SendGrid failed with status {response.status_code}")

        # Logging
        logger.info(f"SendGrid status: {response.status_code}")
        logger.info(f"SendGrid headers: {response.headers}")

        # Extract SendGrid Message ID
        sg_message_id = response.headers.get("X-Message-Id")

        return sg_message_id

    except Exception as e:
        logger.error(f"SendGrid failed: {str(e)}")
        return None






if __name__ == "__main__":

    response = send_mail(
        to_email="amanjaiswal1412000@gmail.com",
        subject="Test3 SendGrid Email",
        body="Hello Aman,\n\nThis is a test3 email via SendGrid.\n\nThanks"
    )

    print("Message ID:", response)