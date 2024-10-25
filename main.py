import streamlit as st


st.title("💬 업무비서 자비스")
# st.caption("🚀 A Streamlit chatbot powered by CRAFTERS")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "무엇을 도와드릴까요??"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
   
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    msg = "답변" # 여기에 모델 답변 SET 하면 답변 출력됨
    st.session_state.messages.append({"role": "assistant", "content": msg})
    # st.chat_message("assistant").write(msg)
