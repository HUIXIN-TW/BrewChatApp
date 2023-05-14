import nltk
from nltk.chat import eliza
from nltk.sentiment import SentimentIntensityAnalyzer

class ElizaChatbot:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
        nltk.download('stopwords')
        nltk.download('vader_lexicon')

        # Load pairs for the chatbot to use
        my_pairs = self.load_pairs()
        self.suggestions = self.load_suggestions()

        # Combine pairs and initialize chatbot
        self.pairs =  my_pairs + eliza.pairs
        self.chatbot = eliza.Chat(self.pairs, eliza.reflections)
        self.sentiment_analyzer = SentimentIntensityAnalyzer()


    def get_response(self, message):
        # Get sentiment of user's message
        sentiment = self.sentiment_analyzer.polarity_scores(message)['compound']
        
        if sentiment > 0:
            response = "I'm glad to hear that! "
            suggestion = self.suggestions['positive'][0]
        elif sentiment < 0:
            response = "I'm sorry to hear that. "
            suggestion = self.suggestions['negative'][0]
        else:
            response = ""
            suggestion = self.chatbot.respond(message)
        
        response += suggestion
        return response

    def load_pairs(self):
        my_pairs = (
            ('hi|hey|hi, there', ('Hello, how are you?', 'Hi, how are you?')),
            ('Remy need (.*) (.*) (.*)', ('%1, %2, %3 are good things to need.', 'I love %1, %2, %3')),
            ('Huixin need (.*) (.*)', ('Why do you need %1 %2?', 'Are you sure you need %1 and %2?'))
        )
        return my_pairs

    def load_suggestions(self):
        my_suggestions = {
            'positive': [
                "Maybe you could celebrate by doing something you enjoy?",
                "How about treating yourself to a nice meal or doing something fun?",
                "Perhaps you could reward yourself by watching your favorite movie or show?",
            ],
            'negative': [
                "Maybe you could talk to someone you trust about what's going on?",
                "How about doing something to take your mind off things, like going for a run or playing a game?",
                "I'm here for you. Perhaps you could try some meditation or journaling to help you feel better?",
            ]
        }
        return my_suggestions


# Get a response to a user message
# my_chatbot = Chatbot()
# response = my_chatbot.get_response("I'm feeling sad.")
# print(response)
