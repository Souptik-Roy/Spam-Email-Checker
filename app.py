import streamlit as st  
import pickle

# Load pipeline
with open("models/spam-checker-pipeline.pkl", "rb") as f:
    spam_clf = pickle.load(f)

st.title("📧 Spam Email/SMS Classifier")

message = st.text_area("Enter a message:")
if st.button("Check"):
    prediction = spam_clf.predict([message])[0]
    st.write("### Prediction: ", "🚨 Spam" if prediction == 1 else "✅ Not Spam")

