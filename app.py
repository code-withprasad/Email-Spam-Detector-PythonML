# import streamlit as st
# import pickle
# import string
# from nltk.corpus import stopwords
# import nltk
#
# from nltk.stem.porter import PorterStemmer
# ps = PorterStemmer()
#
#
# def transform_text(text):
#     # convert in lower case
#     text = text.lower()
#     # convert into list
#     text = nltk.word_tokenize(text)
#     # remove special characters
#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         y.append(ps.stem(i))
#
#     return " ".join(y)
#
#
# tfidf = pickle.load(open("vectorizer.pkl", 'rb'))
# model = pickle.load(open('model.pkl', 'rb'))
#
# st.title("E-mail spam Classifier")
#
# input_sms = st.text_input("Enter the message")
#
# if st.button('Predict'):
#     # 1. preprocess
#     transformed_sms = transform_text(input_sms)
#     # 2. vectorize
#     vector_input = tfidf.transform([transformed_sms])
#     # 3. predict
#     result = model.predict(vector_input)[0]
#     # 4. Display
#     if result == 1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam")
import pickle
#
#
# import streamlit as st
# import pickle
# import string
# from nltk.corpus import stopwords
# import nltk
# import random
# import webbrowser
# # import subprocess
# from PIL import Image
#
# from nltk.stem.porter import PorterStemmer
#
# ps = PorterStemmer()
#
# # A list of tips to avoid spam
# spam_tips = [
#     "Never reply to spam messages, even to unsubscribe.",
#     "Use a spam filter to block unwanted messages.",
#     "Do not click on links in suspicious emails.",
#     "Be cautious when giving out your email address.",
#     "Avoid opening attachments from unknown senders.",
#     "Use strong and unique passwords.",
#     "Be wary of messages that request personal information.",
#     "Don't trust emails that appear to be from a familiar company but have an unusual sender address."
# ]
#
#
# def transform_text(text):
#     # convert in lower case
#     text = text.lower()
#     # convert into list
#     text = nltk.word_tokenize(text)
#     # remove special characters
#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         y.append(ps.stem(i))
#
#     return " ".join(y)
#
#
# tfidf = pickle.load(open("vectorizer.pkl", 'rb'))
# model = pickle.load(open('model.pkl', 'rb'))
#
# st.set_page_config(page_title="E-mail spam Classifier", page_icon=":email:")
# st.title("E-mail Spam Classifier")
#
# image = Image.open('spam_detection.jpg')
# # st.image(image, width=600, height=100)
# st.image(image, use_column_width=True)
#
# st.write("""
# This application is designed to classify emails as spam or not spam.
# """)
#
# st.sidebar.title("How to Use")
# st.sidebar.write("""
# 1. Enter the email message in the input box.
# 2. Click on the 'Predict' button to see if it's spam or not.
# 3. A tip to avoid spam will be suggested after a prediction is made.
# """)
#
# input_sms = st.text_area("Enter the email message here:")
#
# if st.button('Predict'):
#     if not input_sms:
#         st.warning("Please enter an email message.")
#     else:
#         # 1. preprocess
#         transformed_sms = transform_text(input_sms)
#         # 2. vectorize
#         vector_input = tfidf.transform([transformed_sms])
#         # 3. predict
#         result = model.predict(vector_input)[0]
#         # 4. Display
#         if result == 1:
#             st.error("This email is spam.")
#         else:
#             st.success("This email is not spam.")
#
#         # # Open Gmail to copy email address
#         # open_gmail = st.button("Open Gmail to Copy Email Address")
#         # if open_gmail:
#         #     # webbrowser.open_new_tab("https://mail.google.com/")
#         #     # webbrowser.get('Edge').open_new_tab("https://mail.google.com/")
#         #     webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application"))
#         #     webbrowser.get('chrome').open_new_tab("https://mail.google.com/")
#         #     st.write("Copy the email address and paste it in the input box above to check for spam.")
#
#
#         # Open Gmail to copy email address
#         open_gmail = st.button("Open Gmail to Copy Email Address")
#         if open_gmail:
#             gmail_url = "https://mail.google.com/"
#             # subprocess.call(["open", "-a", "Microsoft Edge", gmail_url])
#             webbrowser.get('Edge').open_new_tab("https://mail.google.com/")
#             st.write("https://mail.google.com/mail/u/0/#inbox")
#
# # Suggest a tip on how to avoid spam
# if input_sms:
#     st.write("Tip to avoid spam: ", random.choice(spam_tips))


import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
import random
import webbrowser
from PIL import Image

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# A list of tips to avoid spam
spam_tips = [
    "Never reply to spam messages, even to unsubscribe.",
    "Use a spam filter to block unwanted messages.",
    "Do not click on links in suspicious emails.",
    "Be cautious when giving out your email address.",
    "Avoid opening attachments from unknown senders.",
    "Use strong and unique passwords.",
    "Be wary of messages that request personal information.",
    "Don't trust emails that appear to be from a familiar company but have an unusual sender address."
]


def transform_text(text):
    # convert in lower case
    text = text.lower()
    # convert into list
    text = nltk.word_tokenize(text)
    # remove special characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="E-mail spam Classifier", page_icon=":email:")
st.title("E-mail Spam Classifier")

image = Image.open('spam_detection.jpg')
st.image(image, use_column_width=True)

st.write("""
This application is designed to classify emails as spam or not spam.
""")

st.sidebar.title("How to Use")
st.sidebar.write("""
1. Enter the email message in the input box.
2. Click on the 'Predict' button to see if it's spam or not.
3. A tip to avoid spam will be suggested after a prediction is made.
""")

input_sms = st.text_area("Enter the email message here:")

if st.button('Predict'):
    if not input_sms:
        st.warning("Please enter an email message.")
    else:
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.error("This email is spam.")
        else:
            st.success("This email is not spam.")

        # Open Gmail to copy email address
        open_gmail = st.button("Open Gmail to Copy Email Address")
        if open_gmail:
            webbrowser.open_new_tab("https://mail.google.com/")
            st.write("Copy the email address and paste it in the input box above to check for spam.")

# Suggest a tip on how to avoid spam
if input_sms:
    st.write("Tip to avoid spam: ", random.choice(spam_tips))

