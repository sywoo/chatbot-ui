import streamlit as st

def generate_response(query):
    # GPT-3.5를 이용한 응답 생성
    return "GPT-3.5 응답: " + query

st.title("자비스")
user_input = st.text_input("여기에 메시지를 입력하세요")
if user_input:
    response = generate_response(user_input)
    st.write("챗봇 응답:", response)
