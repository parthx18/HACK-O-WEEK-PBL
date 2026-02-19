/*Week 1: The "Rule-Engine" with Regex (Advanced)
Instead of simple if "word" in text, use Regular Expressions (Regex) to catch variations and JSON-based Knowledge Bases to keep data separate from your code.
Logic: Use a rules.json file to store patterns.
Code: Use re.search() to identify intents regardless of word order.
*/

import re
import json

# Rule-based Knowledge Base
RULES = {
    r"(cost|price|fees?|tuition)": "Annual tuition is $5,000.",
    r"(time|hours?|open|close)": "We are open 9 AM - 5 PM.",
    r"(call|phone|email|contact)": "Contact us at admin@edu.com."
}

def rule_bot(user_input):
    for pattern, response in RULES.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm not sure. Try asking about fees or contact info."
