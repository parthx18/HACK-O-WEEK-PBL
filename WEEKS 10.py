import pandas as pd
from datetime import datetime

class ChatAnalytics:
    def __init__(self, log_file="chat_logs.csv"):
        self.log_file = log_file

    def log_interaction(self, query, intent, confidence, response):
        log_entry = {
            "timestamp": datetime.now(),
            "query": query,
            "predicted_intent": intent,
            "confidence": round(confidence, 2),
            "response": response,
            "needs_review": confidence < 0.5  # Flag for Week 10 'Propose Improvements'
        }
        
        # Append to CSV
        df = pd.DataFrame([log_entry])
        df.to_csv(self.log_file, mode='a', header=not pd.io.common.file_exists(self.log_file), index=False)

    def generate_improvement_report(self):
        df = pd.read_csv(self.log_file)
        # Find the most common queries where the bot was confused
        review_needed = df[df['needs_review'] == True]['query'].value_counts()
        print("--- Improvement Report ---")
        print("Top queries needing new intents/patterns:")
        print(review_needed.head(5))

# Example Integration
# analytics = ChatAnalytics()
# intent, conf = model.predict(user_query)
# analytics.log_interaction(user_query, intent, conf, bot_response)
