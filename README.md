# 📧 Intelligent Spam Detector  

A machine learning project that detects whether a given message is **🚨 Spam** or **✅ Not Spam**, with a beautiful **Streamlit web app** interface.  

---

## ✨ Features
- Trains a **Naive Bayes classifier** using SMS spam dataset.  
- Uses **CountVectorizer** for feature extraction.  
- Achieves **98% accuracy** on test data.  
- Interactive **Streamlit app** to check messages in real time.  
- Clean UI with emojis, warnings, and results display.  

---

## 🧑‍💻 Tech Stack
- Python  
- Pandas, Scikit-learn  
- Streamlit  
- Pickle (for saving model & pipeline)  

---

## 📂 Project Structure
📦 spam-detector
┣ 📜 spam.csv # Dataset
┣ 📜 train_model.py # Model training script
┣ 📜 spam-checker-pipeline.pkl # Saved ML pipeline
┣ 📜 app.py # Streamlit app
┣ 📜 README.md # Project documentation
