import streamlit as st

def generate_response(query):
    # GPT-3.5를 이용한 응답 생성
    return "GPT-3.5 응답: " + query

# st.title("자비스")
st.title("💬 업무비서 자비스")
st.caption("🚀 A Streamlit chatbot powered by CRAFTERS")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
