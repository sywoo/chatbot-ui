import streamlit as st

st.title("우리의 AI 챗봇")
user_input = st.text_input("여기에 메시지를 입력하세요")
if user_input:
    response = generate_response(user_input)
    st.write("챗봇 응답:", response)
