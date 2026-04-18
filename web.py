import streamlit as st
from openai import OpenAI
import math

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Humanise Writing")

st.write("Upload your assignment")

uploaded_file = st.file_uploader("Upload file", type=["txt"])

def count_words(text):
    return len(text.split())

def calculate_price(word_count):
    return math.ceil(word_count / 100) * 1.5

def humanise(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Make writing more natural and smooth."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

    word_count = count_words(text)
    price = calculate_price(word_count)

    st.write(f"Word count: {word_count}")
    st.write(f"Estimated price: RM {price}")

    if st.button("Generate Preview"):
        result = humanise(text)
        preview = " ".join(result.split()[:120])

        st.write("Preview:")
        st.write(preview)
