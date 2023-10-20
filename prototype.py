from flask import Flask, request
import requests
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.stacks import YowStackBuilder
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent, YowParallelLayer
from yowsup.layers.auth import AuthError
from yowsup.layers.network import NetworkLayer
from yowsup.env import YowsupEnv

# Setup the yowsup configuration
config = {
    "cc": "CC",  # Replace with your country code
    "phone": "PHONENUMBER",  # Replace with your phone number
    "password": "PASSWORD"  # Replace with your password
}

# Build the yowsup stack
stackBuilder = YowStackBuilder()

stack = stackBuilder\
    .pushDefaultLayers(True)\
    .push(YowParallelLayer([SubLayer]))\
    .build()

stack.setCredentials(config)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def teams_webhook():
    data = request.json
    message = data['text']
    send_message_whatsapp(message)
    return '', 204

def send_message_whatsapp(message):
    outgoingMessage = TextMessageProtocolEntity(message, to="PHONENUMBER")
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
    stack.loop()
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
