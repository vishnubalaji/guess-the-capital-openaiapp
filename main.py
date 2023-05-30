import os
import openai
import streamlit as st

openai.api_key = os.environ['OPENAI_API']

def get_country():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{
    "role":"user",
    "content":"name a country"
}])
    st.session_state.country = completion.choices[0].message.content.strip()

def verify_capital():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{
    "role":"user",
    "content":f"is {st.session_state.capital} the capital of {st.session_state.country}?"
}])
    completion = completion.choices[0].message.content.strip()
    st.write(completion)
    if "yes" in completion.lower():
        increment_score()

def increment_score():
    st.session_state['score']+=1

if "score" and "country" not in st.session_state:
    st.session_state['score'] = 0
    st.session_state['country'] = None

st.write("Country name : ", st.session_state.country)
st.write("Current score : ", st.session_state['score'])
st.button("Get the country name", on_click=get_country)
st.text_input("Enter the capital city", key="capital")
st.button("Submit guess", on_click=verify_capital)