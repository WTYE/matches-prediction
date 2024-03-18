import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.title("Chatbot")
with st.chat_message("user"):  # 或者寫 "human"
    st.write("Hi 👋，請問你是誰？")

# 另一種寫法
message = st.chat_message("assistant")  # 或者寫 "ai"
# message = st.chat_message("assistant", avatar="🦖")  # 自訂頭像
message.write("你好！我是 ChatBot 🤖，可以回答各種問題，提供資訊。")
message.write("有什麼我可以幫助你的嗎？")

st.chat_input("Say something...")
