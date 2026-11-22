
import random
import streamlit as st

# 웹앱 제목
st.title("🍱 오늘의 점심 메뉴 추천")

# 점심 메뉴 목록
menu = ["김치찌개", "돈가스", "제육볶음", "비빔밥", "파스타",
        "초밥", "햄버거", "떡볶이", "라면", "마라탕"]

# 안내 문구
st.write("오늘은 무엇을 먹을까요?")
st.write("버튼을 누르면 랜덤으로 점심 메뉴를 추천해 줍니다!")

# 버튼을 누르면 메뉴 추천
if st.button("오늘의 점심 메뉴 추천받기"):
    result = random.choice(menu)
    st.success(f"오늘의 점심 메뉴는 🍴 {result} 입니다!")
