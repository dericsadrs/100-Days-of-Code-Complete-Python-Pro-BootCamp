from twilio.rest import Client
import os

TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
