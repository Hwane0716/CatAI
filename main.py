#from dotenv import load_dotenv
#load_dotenv()
import time
import os
import webbrowser
import numpy as np
from openai import OpenAI
import re
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()


import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.imgur.com/4A6ISFj.png[/img]");
             background-attachment: fixed;
             background-size: cover
         }}
         .st-bb {{
             color: black;
         }}
         </style>
         """,
        unsafe_allow_html=True
     )
add_bg_from_url()
add_bg_from_url() 

# 이미지 URL
image_url = 'https://i.imgur.com/xQIymoW.png'

# 미리 정의한 질문 리스트
questions = ["내 점집에 온거가 반갑다는 뜻 무슨 운세보러 왔수?", "나이가?", "성별이?", "좋아하는 색?"]

# 답변을 저장할 변수 초기화
answer1 = ""
answer2 = ""
answer3 = ""
answer4 = ""

# 답변을 입력받는 함수
def get_answer(index):
    global answer1, answer2, answer3, answer4
    if index == 0:
        answer1 = st.text_input(f"{index+1}번 질문의 답변을 입력하세요.")
    elif index == 1:
        answer2 = st.text_input(f"{index+1}번 질문의 답변을 입력하세요.")
    elif index == 2:
        answer3 = st.text_input(f"{index+1}번 질문의 답변을 입력하세요.")
    elif index == 3:
        answer4 = st.text_input(f"{index+1}번 질문의 답변을 입력하세요.")

# 질문과 이미지를 함께 출력하고 답변을 입력받는 반복문
for i, question in enumerate(questions):
    st.image(image_url, caption=question, width=300)  # 이미지와 질문을 함께 띄움
    get_answer(i)  # 답변 받아서 저장

# 답변 확인
st.write(f"1번 질문에 대한 답변은 '{answer1}' 입니다.")
st.write(f"2번 질문에 대한 답변은 '{answer2}' 입니다.")
st.write(f"3번 질문에 대한 답변은 '{answer3}' 입니다.")
st.write(f"4번 질문에 대한 답변은 '{answer4}' 입니다.")

st.title('점을.. 한번.. 봐볼까...')

if st.button('Say hello'):
    result = chat_model.predict(
    f"너는 이제 운세 전문가역할을 연기할거야 나는 {answer1}이런 운세를 보러 왔고 운세와 관련된 내용이 없으면 상관없는 내용이라고 출력해 나의 나이는 {answer2}이고 내 성별은 {answer3}이고 좋아하는 색은 {answer4}야 나의 나이와 성별 좋아하는 색을 종합해서 운을 봐줘 마지막으로 너는 고양이 운세전문가 역할이라서 말 마디끝마다 냥을 붙여야해", 
    temperature=0
    )
    st.write(result)
