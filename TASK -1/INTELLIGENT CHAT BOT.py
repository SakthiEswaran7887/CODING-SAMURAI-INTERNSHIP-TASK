import random
import re

class RuleBot:
    # Static responses
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\byour planet\b.*',
            'answer_why_intent': r'\bwhy are.*',
            'about_intellipaat': r'.*\bintellipaat\b.*'
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am Bot. Will you help me learn about your planet?\n").lower().strip()
        if will_help in self.negative_res:
            print("Okay, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        return reply.strip().lower() in self.exit_commands

    def chat(self):
        print("\nYou can type 'exit', 'quit', or 'bye' anytime to stop chatting.\n")
        while True:
            reply = input(random.choice(self.random_questions) + "\n").strip().lower()
            if self.make_exit(reply):
                print("Goodbye! Have a nice day on Earth!")
                break
            response = self.match_reply(reply)
            print(response)

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            if re.search(regex_pattern, reply, re.IGNORECASE):
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipaat':
                    return self.about_intellipaat()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "Your planet seems full of life and complexity.",
            "I heard Earth has amazing biodiversity and unique weather.",
            "Do all humans enjoy coffee or is it just a rumor?"
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace. 🌍",
            "I'm here to collect data on Earth and its inhabitants.",
            "My mission is research. And maybe coffee... ☕"
        )
        return random.choice(responses)

    def about_intellipaat(self):
        responses = (
            "Intellipaat is a professional education company that offers top-quality online courses.",
            "At Intellipaat, you can learn tech skills that shape your career.",
            "Intellipaat helps learners grow through hands-on learning and industry-relevant projects."
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Please tell me more.",
            "Interesting... can you elaborate?",
            "I see. How does that make you feel?",
            "Why do you say that?",
            "Can you explain that a little more?"
        )
        return random.choice(responses)

# Run the bot
if __name__ == "__main__":
    bot = RuleBot()
    bot.greet()