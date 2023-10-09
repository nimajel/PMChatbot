from flask import Flask, request, make_response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp-webhook', methods=['POST'])
def whatsapp_webhook():
    # Get the message sent by the user
    incoming_msg = request.values.get('Body', '').lower()

    # Create a response object
    resp = MessagingResponse()

    # Let's just echo the text back for now
    # In a real-world scenario, you'll process the message and send an appropriate response or pass it to ChatGPT.
    msg = resp.message(f"You said: {incoming_msg}")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)