import json

class ChatbotDeployer:
    def __init__(self, bot_engine):
        self.bot = bot_engine

    def simulate_channel(self, user_id, message, channel="web"):
        # Process through your Week 1-8 logic
        response_text = self.bot.get_response(user_id, message)
        
        # Format based on channel requirements
        if channel == "whatsapp":
            return self._format_whatsapp(response_text)
        elif channel == "mobile_app":
            return self._format_json_payload(response_text)
        return response_text # Default Web/Console

    def _format_whatsapp(self, text):
        # WhatsApp supports bolding with asterisks
        return f"*Campus Bot:* {text}\n\n_Reply 'MENU' for options._"

    def _format_json_payload(self, text):
        # Mobile apps often need structured data
        return json.dumps({
            "status": "success",
            "message": text,
            "quick_replies": ["Fee Info", "Exams", "Contact Admin"]
        })

# Usage
# deployer = ChatbotDeployer(your_trained_bot)
# print(deployer.simulate_channel("user123", "When are exams?", channel="whatsapp"))
