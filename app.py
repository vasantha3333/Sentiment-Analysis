
import streamlit as st
from textblob import TextBlob
from PIL import Image
def main():
  st.title("Sentiment Analysis")
  img=Image.open("sentiment-analysis_1.jpg")
  st.image(img)
  st.write("sentiment analysis")
  text=st.text_input("Enter a sentence--")
  if st.button("Analysis"):
    br=TextBlob(text)
    result=br.sentiment.polarity
    if result==0:
      st.success("This is a Neutral Message")
    elif result>0:
      st.success("This is a Positive Message")
    else:
      st.success("This is a Negative Message")
   
if __name__=="__main__":
  main()
