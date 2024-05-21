import openai
import time

class Chatbot:
    def __init__(self):
        openai.api_key = "____ your Key___"

    def get_response(self, user_input):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ],
                max_tokens=3000,
                temperature=0.5
            ).choices[0].message['content']
            return response
        except openai.error.RateLimitError as e:
            print("Rate limit exceeded. Please try again later.")
            # Optionally, implement a retry mechanism
            # time.sleep(60)  # Wait for 60 seconds before retrying
            # return self.get_response(user_input)
            return "Rate limit exceeded. Please try again later."

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
