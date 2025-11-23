from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from assistant import handle_whatsapp_message
import logging
from session_utils import reset_session

app = Flask(__name__)

# Configure logging to track the session flow
logging.basicConfig(level=logging.DEBUG)

# Dictionary to hold session data for each user
user_sessions = {}

# Function to reset the session for a user
#def reset_session(user_id):
    #user_sessions[user_id] = {
    #    "customer_name": None,
    #    "project_name": None,
    #    "work_description": None,
    #    "welcomed": False  # Track whether the user received a welcome message
  #  }
   # logging.debug(f"Session reset for user {user_id}")
    

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    user_id = request.values.get("From", "")

    # Initialize session if not already present
    if user_id not in user_sessions:
        user = reset_session(user_id)

    # Log the incoming message and user session
    logging.debug(f"Received message: '{incoming_msg}' from user {user_id}")
    logging.debug(f"Current session state for user {user_id}: {user[user_id]}")

    # Process the message with the session state
    session = user[user_id]
    response_text = handle_whatsapp_message(incoming_msg, session)
    
    # Reset the session if the user entered 'quit'
    if incoming_msg.lower() == "quit":
        user = reset_session(user_id)

    # Create a Twilio MessagingResponse and send back the response
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)


