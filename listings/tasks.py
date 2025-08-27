from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task

@shared_task
def send_email(to, subject, body):
    # Simulate email sending logic
    print(f"Sending email to {to}, subject: {subject}")
    return f"Email sent to {to}"

@shared_task
def send_sms(phone_number, message):
    # Simulate SMS sending logic
    print(f"Sending SMS to {phone_number}: {message}")
    return f"SMS sent to {phone_number}"

# Example task that processes notifications based on the type
@shared_task
def process_notification(notification_type, payload):
    if notification_type == 'email':
        return send_email(payload['to'], payload['subject'], payload['body'])
    elif notification_type == 'sms':
        return send_sms(payload['phone_number'], payload['message'])
    else:
        print("Unknown notification type.")
        return "Error: Unknown notification type"