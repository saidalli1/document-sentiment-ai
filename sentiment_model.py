from transformers import pipeline

"""
Initialize the sentiment analysis pipeline 
and use hugging face roberta model which is trained 
on social media text to better understand slang and context
"""
sentiment_pipeline = pipeline(
    "sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment"
)

def analyze_sentiment(text):
    """
    Takes text input and returns sentiment label + confidence score
    """
    # limit input text to 512 tokens to avoid model error    
    result = sentiment_pipeline(text[:512])[0]   

    # Extract the label and the confidence probability
    label = result["label"]
    score = round(result["score"], 3)

    # Return the label capitalized and the confidence score
    return label.capitalize(), score