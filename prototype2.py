from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def teams_webhook():
    data = request.json
    message = data['text']
    send_message_whatsapp(message)
    return '', 204

def send_message_whatsapp(message):
    url = "https://api.green-api.com/waGateway/v1/chat/send/message/YOUR_INSTANCE_ID/YOUR_TOKEN"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "chatId": "PHONE_NUMBER",  # the phone number of the recipient
        "message": message
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return '', 204

# Replace "YOUR_INSTANCE_ID" and "YOUR_TOKEN" with your actual Green API instance ID and token. Also, replace "PHONE_NUMBER" with the actual phone number of the recipient.

if __name__ == '__main__':
    app.run(port=5000)
