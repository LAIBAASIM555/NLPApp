import paralleldots
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

class API:
    def __init__(self):
        paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

    def sentiment_analysis(self, text):
        """Perform sentiment analysis on the provided text."""
        try:
            response = paralleldots.sentiment(text)
            logging.info("Sentiment analysis successful.")
            return response
        except Exception as e:
            logging.error(f"Sentiment analysis error: {str(e)}")
            return {"error": str(e)}

    def ner(self, text):
        """Perform named entity recognition on the provided text."""
        try:
            response = paralleldots.ner(text)
            logging.info("NER successful.")
            return response
        except Exception as e:
            logging.error(f"NER error: {str(e)}")
            return {"error": str(e)}

    def emotion_prediction(self, text):
        """Predict emotions from the provided text."""
        try:
            response = paralleldots.emotion(text)
            logging.info("Emotion prediction successful.")
            return response
        except Exception as e:
            logging.error(f"Emotion prediction error: {str(e)}")
            return {"error": str(e)}
