from twilio.rest import Client
import os

twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(twilio_account_sid, twilio_auth_token)

message = client.messages \
                .create(
                     body="Beep boop.",
                     from_='+17739005109',
                     to='+18622543503'
                 )

print(message.sid)
