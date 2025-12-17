def generate_explanation(text, sentiment):
    """
    Generates a human-readable explanation for the sentiment
    """

    if sentiment == 'Positive':
        reason = "The text uses optimistic language, positive expressions, and favorable descriptions."
        
    elif sentiment == 'Negative':
        reason = "The text contains critical wording, negative emotions, or expressions of dissatisfaction."
    else:
        reason = "The text maintains a balanced tone with factual language and minimal emotional bias."

    explantion = (
        f"The overall sentiment is ** {sentiment}** becuase {reason}"
        "Key phrases and tone throughout the document support this classification."
    )

    return explantion
