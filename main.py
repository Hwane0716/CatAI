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
questions = ["무슨 확률을 보러왔나요?[예를 들어 길가다 넘어질 확률]", "나이는?", "성별은?", "좋아하는 색?"]

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
    st.image(image_url, caption=question, width=500)  # 이미지와 질문을 함께 띄움
    get_answer(i)  # 답변 받아서 저장

# 답변 확인
st.write(f"알고싶은 확률 {answer1}")
st.write(f"나이 {answer2}")
st.write(f"성별 {answer3}")
st.write(f"좋아하는 색 {answer4}")

st.title('확률을.. 한번.. 봐볼까...')

if st.button('확률 보기'):
    result = chat_model.predict(
    f"너는 이제부터 모든것에 확률을 측정해주는 고양이 역할이야 너가 대답을 할 때 무조건 지켜야해 조건사항은 1.너가 인공지능이라는걸 알려줘서는 안돼 2.내가 알아보고싶은것 , 내 나이 , 내 성별 , 내가 좋아하는 색을 토대로 답변을 무조건 정확하지 않아도 되니까 퍼센트가 포함되게 알려줘야하고 3.그리고 그 퍼센트가 나온 재미있는 이유를 알려줘야해 대답해줘야해 내가 알아보고 싶은 것은{answer1}이고 , 나이는 {answer2}이고 , 성별은 {answer3}이고 , 좋아하는색은 {answer4}야 ", 
    temperature=0
    )
    st.write(result)
