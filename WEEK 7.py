#Week 7: Context Handling for Follow-ups
#The Goal: Support multi-turn conversations. If a user asks "When is the exam?" and then says "For third year?", the bot should remember that the topic is still "exams."

#The Implementation (Session State)
#We use a simple dictionary to store the "last intent" and "last entities" for a specific user.

#Python
# Simple Global State (In production, use Redis or a Database)
user_sessions = {}

def handle_conversation(user_id, user_input):
    # 1. Get current intent and entities
    current_intent = classify_intent(user_input) # From Week 5 logic
    current_entities = extract_entities(user_input) # From Week 6 logic
    
    # 2. Retrieve session history
    session = user_sessions.get(user_id, {"last_intent": None, "entities": {}})
    
    # 3. Context Filling logic
    if current_intent == "uncertain" and session["last_intent"]:
        current_intent = session["last_intent"] # Assume they are still on the same topic
    
    # Update session
    session["last_intent"] = current_intent
    session["entities"].update(current_entities)
    user_sessions[user_id] = session
    
    return f"Processing {current_intent} for {session['entities']}"
