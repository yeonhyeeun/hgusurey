import streamlit as st
import pandas as pd

# 데이터: 리스트 내 딕셔너리 형태
data = [
    {
        "링크 제목": "수시 면접 도우미 모집",
        "응답 바로가기 링크": "https://forms.gle/i8AFLZnZz6JX47UU6",
        "주최명": "홍보대사 나누미",
        "공고기한": "2024-11-11 (월)",
        "설명": "안녕하세요 홍보대사 나누미입니다😊 일반학생 전형 수시 면접 도우미를 모집합니다!           2024년 가을학기 💛12주차 토요일(11월 16일)💛에 예비 25학번들이 면접을 보기 위해 한동에 옵니다. 내년에 만날 새로운 한동인들을 기대하는 마음으로 수시 면접고사를 나누미와 함께 섬길 면접 도우미를 모집합니다.",
        "보상" : "없음", 
        
    },
    {
        "링크 제목": "24-2 전산전자 MT",
        "응답 바로가기 링크": "https://forms.gle/SrjuTctTMNqPrfLs8",
        "주최명": "전산전자공학부 임원단 ",
        "공고기한": "2024-11-13 (수)",
        "설명": "드디어! 여러분이 많이많이 기다려주셨던 전산전자 학부 MT가 13주차 화요일에 열립니다! 👏🏻👏🏻",
        "보상" : "없음", 
    },
        {
        "링크 제목": "24-2 RRM 수업 설문조사",
        "응답 바로가기 링크": "https://docs.google.com/forms/d/e/1FAIpQLSfncmCMVJWXFbRJ3sQ_QPrrpE2tOoC4BQhaXN5Q1zFKRnMTdA/viewform?usp=sf_link",
        "주최명": "24-2 RRM 수업 수강자(김00, 남00, 박00)",
        "공고기한": "-",
        "설명": "성경적 관점에서 봤을 때 결혼에 대한 인식 조사를 실시하고자 설문을 진행하려고 합니다〰️❕" ,
        "보상" : "4,500원 상당 기프티콘 추첨", 
    }
]

# 페이지 구성
st.title("📋 한동대 교내 설문조사 리스트")
st.write("아래에서 원하는 설문조사 링크를 선택하여 해당 설문조사 페이지로 이동하세요.")

# 링크 리스트 표시
for item in data:
    st.write(f"### {item['링크 제목']}")
    st.write(f"[바로가기]({item['응답 바로가기 링크']})")
    st.write(f"주최명: {item['주최명']} | 마감일: {item['공고기한']} | 보상: {item['보상']}")
    
    # "더보기" 클릭 시 내용 표시
    with st.expander("더보기"):
        st.write(item["설명"])

# 하단 설문조사 신청 폼
st.write("---")
st.header("💬 설문조사 신청하기")

# 필수 입력란: 제목, 바로가기 링크, 문의 내용
title = st.text_input("설문조사 제목", "")
link = st.text_input("바로가기 링크", "")
contact = st.text_area("문의 내용", "")

# 선택 입력란: 보상, 더보기
reward = st.text_input("보상 (선택)", "")
more_info = st.text_area("더보기 (선택)", "")

# 제출 버튼
if st.button("제출"):
    if title and link and contact:
        st.success("설문조사 신청이 완료되었습니다!")
        st.write("제출된 내용:")
        st.write(f"**제목**: {title}")
        st.write(f"**바로가기 링크**: {link}")
        st.write(f"**문의 내용**: {contact}")
        if reward:
            st.write(f"**보상**: {reward}")
        if more_info:
            st.write(f"**더보기**: {more_info}")
    else:
        st.error("제목, 바로가기 링크, 문의 내용은 필수 입력 사항입니다.")
        
# 하단 Footer
st.write("---")
st.write("개발자: hyerong | 문의: [yeonyen622@handong.ac.kr](mailto:example@example.com)") 
