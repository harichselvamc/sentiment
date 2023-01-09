import streamlit as st 
import nltk #nltk defined as natural language tool kit from natural language processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer #vader is NLTK tool
nltk.download('vader_lexicon')
#VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media

st.sidebar.title("This Webapp is developed by harichselvam")

st.title("sentimental analysis")
st.write("This is sentimental analysis")

user_input1=st.text_area("Please Rate Our Services")
sid=SentimentIntensityAnalyzer()
sid1=SentimentIntensityAnalyzer()

score1=sid1.polarity_scores(user_input1)
score = sid.polarity_scores(user_input1)
st.write(score)

if score1["neg"] != 0:
        st.write("your service review is negative")
else:
        st.write("your service review is positive")


