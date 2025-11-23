
import os
import openai
import logging
from dotenv import load_dotenv
from session_utils import reset_session

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("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")

logging.basicConfig(level=logging.DEBUG)

def translate_text(text, target_language):
    """
    Uses OpenAI API to translate the text into the target language.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Ensure the model supports advanced multilingual capabilities
            messages=[
                {
                    "role": "system",
                    "content": f"You are a translation assistant. Translate the following text into {target_language}:"
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"Error during translation: {e}")
        return "⚠️ Error translating text. Please try again later."

def handle_whatsapp_message(incoming_msg, session):
    greetings = ["hi", "hello", "hey", "start"]

    # If user types "quit," end the session
    if incoming_msg.strip().lower() == "quit":
        reset_session(session["user_id"])
        return "👋 Thank you for using DLI Project Assistant! Goodbye! 🌟 If you need assistance in the future, just reach out!"
    
    # Handle language preference
    if not session.get("preferred_language"):
        if incoming_msg.lower() in greetings:
            return (
                "👋 Hi there! Welcome to DLI Project Assistant 🤖!\n\n"
                "🌐 Please select your preferred language:\n"
                "1. English\n"
                "2. हिंदी (Hindi)\n"
                "3. Español (Spanish)\n"
                "4. Français (French)\n"
                "5. Deutsch (German)\n"
                "Type the number or name of your preferred language."
            )
        else:
            # Map user's choice to a language
            language_map = {
                "1": "English",
                "2": "Hindi",
                "3": "Spanish",
                "4": "French",
                "5": "German",
                "english": "English",
                "hindi": "Hindi",
                "spanish": "Spanish",
                "french": "French",
                "german": "German",
            }
            session["preferred_language"] = language_map.get(incoming_msg.strip().lower())
            if session["preferred_language"]:
                return (
                    f"👍 Great! I'll assist you in {session['preferred_language']}.\n"
                    "Could you please provide the customer name?"
                )
            else:
                return "⚠️ Please choose a valid language option: 1 (English), 2 (Hindi), 3 (Spanish), 4 (French), or 5 (German)."

    # Translate response based on preferred language
    def translate_and_respond(response):
        if session["preferred_language"] == "English":
            return response
        return translate_text(response, target_language=session["preferred_language"].lower())

    if not session.get("welcomed"):
        session["welcomed"] = True
        return translate_and_respond(
            "👋 Hi there! Welcome to DLI Project Assistant 🤖! I’m here to assist you every step of the way. "
            "Let’s get started! 🚀\n\nCould you please provide the customer name?"
        )

    if session.get("customer_name") is None:
        session["customer_name"] = incoming_msg
        return translate_and_respond("👍 Perfect! Now, could you please provide the project name?")

    if session.get("project_name") is None:
        session["project_name"] = incoming_msg
        return translate_and_respond("Great! 📂 Lastly, could you give me a detailed description of the work? 🖊️")

    if session.get("work_description") is None:
        session["work_description"] = incoming_msg

        customer_name = session["customer_name"]
        project_name = session["project_name"]
        work_description = session["work_description"]

        email_draft = (
            "✅ The request has been successfully processed! "
            "An email has been sent to the responsible team. 📧 "
            "If there’s anything else I can help you with, feel free to ask! 😊\n\n"
            "Type 'quit' to end the conversation.\n\n"
            "🔔 *Attention Required: New Issue Notification* 🔔\n\n"
            f"Subject: Issue Notification: {customer_name} for {project_name}\n\n"
            f"Dear Development Team,\n\n"
            f"We have received a message from {customer_name} regarding the project '{project_name}'. "
            f"Here are the details:\n\n"
            f"📋 *Project Description*: {work_description}\n\n"
            "🚨 *Please prioritize this issue* and respond to the customer at your earliest convenience.\n\n"
            "Best regards,\nDLI Project Assistant 🤖"
        )

        # Reset session after completing the process
        reset_session(session["user_id"])

        return translate_and_respond(
            email_draft + "\n\n✅ If you need more help, type 'start' to begin again. 😊"
        )

    return translate_and_respond("⚠️ Oops! Something went wrong. Please try again. 🛠️")
