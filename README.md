# 📧 Spam Email/SMS Detection Project

## 📌 Overview

This project is a Spam Email/SMS Classifier built using Python, Scikit-Learn, and Naive Bayes.
It classifies text messages as either Spam (1) or Not Spam (0) with high accuracy (~98%).

The dataset contains 5572 labeled messages (ham or spam) and is commonly used for text classification tasks.

## 🚀 Features

Preprocess dataset and label messages as spam (1) or ham (0).

Convert text into numerical features using CountVectorizer (Bag of Words).

Train a Naive Bayes classifier (MultinomialNB).

Achieves 98.65% accuracy on the test dataset.

Allows custom email/message predictions.

Model can be saved and loaded for deployment.

## 📂 Dataset

File: spam.csv

Total records: 5572

Columns:

Category: ham or spam

Message: text content of the email/SMS

During preprocessing:

Category → Converted to spam (1 for spam, 0 for ham).

Final dataset contains:

Message (text)

spam (label)

## ⚙️ Technologies Used

Python 🐍

Pandas (Data handling)

Scikit-learn (ML models & preprocessing)

CountVectorizer (Text to features)

Naive Bayes (Classification)

Pickle (Model saving)
