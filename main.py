import streamlit as st
from dotenv import load_dotenv
load_dotenv()

#from langchain.llms import OpenAI
#llm = OpenAI()
#result = llm.invoke("내가 좋아하는 동물은 ")
#print(result.content)

#from langchain.chat_models import ChatOpenAI
#from langchain_openai import ChatOpenAI
#chat_model = ChatOpenAI()

#content = "유전체"
#result = chat_model.invoke(content+" 에 대한 특허 주제를 짧게 써줘.")
#print(result.content)

#st.title("인공지능 특허AI")
st.title("AI POET")
subject = st.text_input("특허의 주제를 제시히주시오.")

if st.button("Ask for poem writing"):
    with st.spinner("making poem ..."):
        result = chat_model.invoke(subject+" 에 대한 시를 짧게 써줘.")
        #st.write("특허주제: ", result.content)
        st.write(result.content)
#result = chat_model.invoke(subject+" 에 대한 특허를 짧게 써줘.")
#result = chat_model.invoke(subject+" 에 대한 시를 짧게 써줘.")
#st.write("특허주제: ", result.content)