import streamlit as st

def generate_response(query):
    # GPT-3.5를 이용한 응답 생성
    return "GPT-3.5 응답: " + query

# st.title("자비스")
st.title("💬 업무비서 자비스")
st.caption("🚀 A Streamlit chatbot powered by CRAFTERS")

user_input = st.text_input("how can I help you, sir?")
if user_input:
    response = generate_response(user_input)
    st.write("자비스:", response)
