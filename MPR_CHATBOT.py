#importing libraries
import openai
import streamlit as st
from streamlit_chat import message

key = "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"
openai.api_key = key

#creating a widget which can allow the users to change the temperature aspect of the model.
temp = st.slider("Select temperature:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

#creating a widget which allows user to change the model type 
model_type = st.selectbox(
    "Select model type:", 
    ("text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"))

#creating a widget which allows users 
#to change the number of tokens using a slider


num_tokens = st.slider("Select number of tokens:", min_value=1, max_value=1024, value=1024, step=20)     


#creating a widget which allows users to change 
#the 'n' parameter.


n_value = st.slider("Select value of n:", min_value=1, max_value=10, value=1, step=1)

#creating a function which will generate calls from api

def generate_response(p,temp):
    completions = openai.Completion.create(
        engine=model_type,
        prompt = p,
        max_tokens = num_tokens,
        n=n_value,
        stop = None,
        temperature = temp

    )
    message = completions.choices[0].text
    return message

st.write("MPR Project made by Deepanshu, Ansh and Gaurav", style={"font-family": "Arial", "font-size": "16px"})
st.title("A friendly Chatbot you can talk to!")

# Storing the chat

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input,temp)
    # storing the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


# using local css
def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# loading snowflake animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>

    <div class = "snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True
) 



        
