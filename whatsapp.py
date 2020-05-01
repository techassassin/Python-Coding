import requests
TWILIO_SID='ACd1c4fa71abc9e08811029940110d630f'
TWILIO_AUTHTOKEN='11ca9bd3d0b225f02b5c28533014c460'
TWILIO_MESSAGE_ENDPOINT = "https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json".format(TWILIO_SID=TWILIO_SID)
TWILIO_NUMBER='whatsapp:+14155238886'
def send_whatsapp_message(to, message):
    message_data = {
        "To": to,
        "From": TWILIO_NUMBER,
        "Body": message,
    }
    print(message_data)
    response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))
    response_json = response.json()
    return response_json

contact_directory = {'Gullu':'+918770575861','Prakhar':'+919039531884'}
for key, value in contact_directory.items():
    to_number='whatsapp:'+value,
    appointment_msg='Hello Gullu, what are you doing?'
    msg = send_whatsapp_message(to_number, appointment_msg)
    print(msg['sid'])  #SM5xxxafa561e34b1e84c9d22351ae08a0
    print(msg['status'])  #queued

print("Completed")


# to_number = 'whatsapp:+919039531884'
# appointment_msg = 'Hello this is an automated message'
# msg = send_whatsapp_message(to_number, appointment_msg)
# print(msg['sid']) # SM5xxxafa561e34b1e84c9d22351ae08a0
# print(msg['status']) # queued

