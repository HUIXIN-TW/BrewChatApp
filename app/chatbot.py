import nltk
import json
from nltk.chat import eliza
from nltk.sentiment import SentimentIntensityAnalyzer
import os

class ElizaChatbot:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
        nltk.download('stopwords')
        nltk.download('vader_lexicon')
        coffee_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app/data/coffee_script.txt")
        self.pairs = self.load_pairs(coffee_file_path)
        self.suggestions = self.load_suggestions()
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
        

    def load_pairs(self, file_name):
        result = []
        with open(file_name, "r") as file:
            for line in file:
                pattern, response_part = line.strip().split('::')
                patterns = pattern.strip()
                responses = tuple(response.strip() for response in response_part.split(';'))
                result.append((patterns, responses))
            pairs = tuple(result)
        return pairs


    def load_suggestions(self):
        suggestion_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app/data/suggestions.json")
        with open(suggestion_file_path, "r") as file:
            suggestions_data = json.load(file)

        my_suggestions = {
            'positive': suggestions_data['positive'],
            'negative': suggestions_data['negative']
        }
        return my_suggestions