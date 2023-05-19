from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from config import account_sid, auth_token

client = Client(account_sid, auth_token)

# Ensure that we are working with US pone numbers and fixes the input to +1XXXXXXXXXX
def format_us_number(phone_number):
    # Remove all non-digits
    digits = ''.join(char for char in phone_number if char.isdigit())
    
    if len(digits) == 10:
        return "+1" + digits
    elif len(digits) == 11 and digits[0] == "1":
        return "+" + digits
    else:
        return None


def send_sms(phone_number, text_msg):
    message = client.messages.create(
        to=format_us_number(phone_number),
        from_="+18446850593",
        body=text_msg)
    print(message.sid)


