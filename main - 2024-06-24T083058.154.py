import spacy
from spacy.cli import download

# Try to load the spaCy model, and download if not found
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Define some sample questions and responses
responses = {
    "greet": "Hello! How can I help you today?",
    "name": "I am a chatbot created to assist you.",
    "weather": "I'm sorry, I can't check the weather for you, but you can try a weather website or app.",
    "recommend_book": "I recommend 'The Great Gatsby' by F. Scott Fitzgerald. It's a classic!",
    "recommend_movie": "I recommend watching 'Inception'. It's a mind-bending thriller!",
    "recommend_food": "How about trying some sushi? It's delicious!",
    "goodbye": "Goodbye! Have a great day!"
}

# Define a simple function to categorize user input
def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greet"
        elif token.lemma_ == "name":
            return "name"
        elif token.lemma_ == "weather":
            return "weather"
        elif token.lemma_ in ["recommend", "suggest"]:
            for child in token.children:
                if child.lemma_ == "book":
                    return "recommend_book"
                elif child.lemma_ == "movie":
                    return "recommend_movie"
                elif child.lemma_ == "food":
                    return "recommend_food"
        elif token.lemma_ in ["bye", "goodbye"]:
            return "goodbye"
    return "default"

# Main chatbot function
def chatbot():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)
        if intent in responses:
            print(f"Chatbot: {responses[intent]}")
            if intent == "goodbye":
                break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()
