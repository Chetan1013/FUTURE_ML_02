import streamlit as st
import joblib
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



category_model = joblib.load(
    'category_model.pkl'
)

priority_model = joblib.load(
    'priority_model.pkl'
)

tfidf = joblib.load(
    'tfidf.pkl'
)



lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))

def clean_text(text):
    
    text = text.lower()
    
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    
    words = text.split()
    
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]
    
    return " ".join(words)



st.set_page_config(
    page_title="Support Ticket Classification System",
    page_icon="🎫",
    layout="wide"
)



st.title("🎫 AI-Powered Support Ticket Classification System")

st.markdown("""
This system automatically:
- Predicts ticket category
- Predicts ticket priority
- Helps support teams improve response time
""")


ticket = st.text_area(
    "Enter Support Ticket",
    height=200
)



if st.button("Analyze Ticket"):
    
    cleaned = clean_text(ticket)
    
    vectorized = tfidf.transform([cleaned])
    
    category = category_model.predict(
        vectorized
    )[0]
    
    priority = priority_model.predict(
        vectorized
    )[0]
    
    st.success(
        f"Predicted Category: {category}"
    )
    
    st.warning(
        f"Predicted Priority: {priority}"
    )

# =========================
# BUSINESS BENEFITS
# =========================

st.subheader("💡 Business Benefits")

st.markdown("""
✅ Faster ticket routing

✅ Reduced support backlog

✅ Improved customer response time

✅ Better operational efficiency

✅ AI-powered support automation
""")

