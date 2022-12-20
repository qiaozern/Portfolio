import os
from twilio.rest import Client

TWILIO_SID = os.environ("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ("TWILIO_AUTH_TOKEN")
TWILIO_VISUAL_NUMBER = os.environ("TWILIO_VISUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ("TWILIO_VERIFIED_NUMBER")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VISUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )