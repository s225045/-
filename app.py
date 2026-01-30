import streamlit as st
from datetime import date

# 페이지 설정
st.set_page_config(page_title="디데이 계산기", page_icon="📅")

st.title("📅 D-Day 계산기")
st.write("중요한 일정을 설정하고 남은 기간을 확인하세요!")

# 1. 날짜 설정 (사용자 입력)
today = date.today()
target_date = st.date_input("목표 날짜를 선택하세요", today)

# 2. 날짜 계산
diff = target_date - today
days_left = diff.days

# 3. 화면 출력
st.divider()

if days_left > 0:
    st.subheader(f"🔥 목표일까지 **{days_left}일** 남았습니다!")
    st.info(f"선택한 날짜: {target_date}")
elif days_left == 0:
    st.subheader("🎉 드디어 **오늘**입니다!")
    st.balloons()
else:
    st.subheader(f"✅ 목표일로부터 **{abs(days_left)}일**이 지났습니다.")
    st.secondary(f"선택한 날짜: {target_date}")

# 프로그래스 바 (선택 사항: 올해 기준 시각화)

st.progress(min(max(days_left / 365, 0.0), 1.0))
