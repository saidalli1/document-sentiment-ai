import streamlit as st
from sentiment_model import analyze_sentiment
from explanation_ai import generate_explanation
from document_loader import load_text_from_pdf, load_text_from_docx

# Sets the browser tab title and the icon (favicon)
st.set_page_config(
    page_title = "Document Sentiment Analyzer",
    page_icon="📄"
)

st.title("📄 AI-Powered Document Sentiment Analysis")

# Creates a sidebar or main-page radio button to let users choose their input method
option= st.radio(
    "Choose input type:",
    ["Paste text", "Upload PDF", "Upload Word document"]
)

# Initialize an empty string to store text extracted from any source
text = ""

# Handle manual text entry
if option == "Paste text":
    text = st.text_area("Paste your text here")

# Handle PDF uploads
elif option == "Upload PDF":
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    if pdf_file:
        text = load_text_from_pdf(pdf_file)

# Handle Word document uploads
elif option == "Upload Word document":
    docx_file = st.file_uploader("Upload a Word document", type="docx")
    if docx_file:
        text = load_text_from_docx(docx_file)


#Processing & Output Section
if st.button("Analyze"):
    # Ensure there is actually text to analyze before running models
    if text.strip():
        # Run the sentiment model logic
        sentiment, confidence = analyze_sentiment(text)
        # Run the explanation model
        explanation = generate_explanation(text, sentiment)

        # Display results in the UI
        st.subheader(f"Sentiment: {sentiment}")
        st.write(f"Confidence Score: {confidence}")
        st.markdown("### AI Explanation")
        st.write(explanation)
    else:
        # Show a warning if the user clicks "Analyze" with no data
        st.warning("Please provide some text input for analysis.")