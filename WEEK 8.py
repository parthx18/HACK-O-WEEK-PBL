#Week 8: Fallbacks and HandoverThe Goal: No bot is perfect. 
#This week focuses on "Graceful Failure." If the bot doesn't understand, it shouldn't just break; it should offer options or escalate to a human.
#The StrategyConfidence Threshold: If the SVM/Classifier score is $< 0.4$, trigger a fallback.
#Clarification: "I'm not sure if you're asking about Exams or Fees. 
#Could you clarify?"Human Handoff: Provide a link to a live chat or create a "Support Ticket" automatically.
def generate_response(user_id, user_input):
    intent, confidence = get_intent_with_confidence(user_input)
    
    if confidence < 0.3:
        return "I'm still learning! Would you like to speak to a human advisor or try rephrasing?"
    
    if confidence < 0.6:
        return f"I think you're asking about {intent}. Is that correct?"
    
    # Standard response logic...
    return get_final_answer(intent)
