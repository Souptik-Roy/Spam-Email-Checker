import streamlit as st
import pickle

# Load pipeline
with open("spam-checker-pipeline.pkl", "rb") as f:
    spam_clf = pickle.load(f)

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="centered")

# Title
st.title("📧 Intelligent Spam Detector")
st.markdown(
    """
    Welcome to the **Spam Detector App**!  
    Enter any text message below, and the app will analyze it to check whether it's **🚨 Spam** or **✅ Not Spam**.
    """
)

# Input box
message = st.text_area("✍️ Type your message here:")

# Button + prediction
if st.button("🔍 Check Message"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message before checking.")
    else:
        prediction = spam_clf.predict([message])[0]
        if prediction == 1:
            st.error("🚨 This looks like **Spam!**")
        else:
            st.success("✅ This message is **Not Spam.**")

# Footer with your name + link
st.markdown("---")

# Two link buttons side by side
# Balanced side-by-side buttons
col1, col2, col3 = st.columns([1,2,1])

with col2:
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🌐 GitHub", "https://github.com/Souptik-Roy/Spam-Email-Checker.git")
    with c2:
        st.link_button("💻 Portfolio", "https://souptik-roy-portfolio.netlify.app/")


st.caption("Made with ❤️ by **Souptik Roy** ")
