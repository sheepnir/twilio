from customer_list import read_phone_numbers
from config import api_key
from send_sms import send_sms

# Reading the phone numbers from the customer database
file_name = 'customer_list.csv'
phone_numbers = read_phone_numbers(file_name)
test_number = phone_numbers[0] 

# Generating a text message using chatGPT
import openai

openai.api_key = api_key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I have a pita bread delivery service that is called Pita Best. We deliver fresh pita bread to the customer's door. Craft me a shot, funny, and creative text message that I can send customers a day before their scheduled delivery.)",
  max_tokens=80
)

print(response["choices"][0]["text"])
print(test_number)

# Enter the message you'd like to send
text_msg = response["choices"][0]["text"]
phone_num = test_number

send_sms(phone_num, text_msg)
