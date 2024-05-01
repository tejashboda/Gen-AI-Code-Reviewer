import google.generativeai as genai
import streamlit as st
f = open("D://Intership//chatbots//in class//gen_api.txt")
key = f.read()

genai.configure(api_key=key)
st.title('CODE BUG FIXER')

user_prompt= st.text_area('Enter the code')

if st.button("Submit"):

    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                                system_instruction='''You are a mentor to students who are learning python language, and you main task is to take python codes 
                        as inputs and check for bugs in the code line by line and explaining the error, and giving the correct code. The output should be in text format''')


    response = model.generate_content(user_prompt)
    content_parts = response.candidates[0].content.parts
    text_content = content_parts[0].text
    st.write(text_content)