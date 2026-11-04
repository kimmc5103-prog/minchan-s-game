
import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="가위바위보 챌린지",
    page_icon="✊",
    layout="centered"
)

# CSS 디자인
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e0f2fe, #f5f3ff);
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 900;
        color: #3730a3;
        margin-bottom: 10px;
    }

    .sub-title {
        text-align: center;
        font-size: 17px;
        color: #64748b;
        margin-bottom: 30px;
    }

    .result-box {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-top: 20px;
    }

    .result-text {
        font-size: 30px;
        font-weight: bold;
        color: #3730a3;
    }

    .choice-text {
        font-size: 22px;
        font-weight: bold;
        color: #334155;
    }

    div.stButton > button {
        border-radius: 12px;
        height: 55px;
        font-size: 20px;
        font-weight: bold;
        border: none;
        background-color: #6366f1;
        color: white;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background-color: #4338ca;
        color: white;
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)


# 선택지 설정
choices = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐️"
}

# 세션 상태 초기화
if "win" not in st.session_state:
    st.session_state.win = 0

if "lose" not in st.session_state:
    st.session_state.lose = 0

if "draw" not in st.session_state:
    st.session_state.draw = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None

if "result" not in st.session_state:
    st.session_state.result = None


# 게임 제목
st.markdown(
    '<div class="main-title">✊ 가위바위보 챌린지 ✌️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">컴퓨터를 이기고 최고의 승부사가 되어보세요!</div>',
    unsafe_allow_html=True
)

st.divider()

# 점수판
st.subheader("🏆 나의 전적")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🥇 승리", st.session_state.win)

with col2:
    st.metric("💔 패배", st.session_state.lose)

with col3:
    st.metric("🤝 무승부", st.session_state.draw)

st.divider()

# 사용자 선택
st.subheader("🎮 무엇을 낼까요?")
st.write("아래 버튼 중 하나를 선택하세요!")

col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice = "가위"

with col2:
    if st.button("✊ 바위", use_container_width=True):
        user_choice = "바위"

with col3:
    if st.button("🖐️ 보", use_container_width=True):
        user_choice = "보"


# 게임 진행
if user_choice is not None:

    computer_choice = random.choice(list(choices.keys()))

    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice

    # 승패 판정
    if user_choice == computer_choice:
        result = "draw"
        result_text = "🤝 무승부!"
        result_color = "#64748b"
        st.session_state.draw += 1

    elif (
        (user_choice == "가위" and computer_choice == "보")
        or (user_choice == "바위" and computer_choice == "가위")
        or (user_choice == "보" and computer_choice == "바위")
    ):
        result = "win"
        result_text = "🎉 승리!"
        result_color = "#16a34a"
        st.session_state.win += 1

    else:
        result = "lose"
        result_text = "😢 패배!"
        result_color = "#dc2626"
        st.session_state.lose += 1

    st.session_state.result = result

    # 게임 기록 저장
    st.session_state.history.insert(
        0,
        {
            "사용자": user_choice,
            "컴퓨터": computer_choice,
            "결과": result_text
        }
    )

    st.session_state.history = st.session_state.history[:10]


# 결과 출력
if st.session_state.result is not None:

    st.divider()
    st.subheader("🎯 게임 결과")

    result = st.session_state.result

    if result == "win":
        result_text = "🎉 승리!"
        result_color = "#16a34a"
        message = "대단해요! 컴퓨터를 이겼어요!"

    elif result == "lose":
        result_text = "😢 패배!"
        result_color = "#dc2626"
        message = "아쉬워요! 다음에는 꼭 이겨봐요!"

    else:
        result_text = "🤝 무승부!"
        result_color = "#64748b"
        message = "비겼어요! 한 번 더 도전해 보세요!"

    # 선택 결과 보여주기
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="result-box">
                <div class="choice-text">🙋 나의 선택</div>
                <div style="font-size:65px;">
                    {choices[st.session_state.user_choice]}
                </div>
                <div class="choice-text">
                    {st.session_state.user_choice}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="result-box">
                <div class="choice-text">🤖 컴퓨터의 선택</div>
                <div style="font-size:65px;">
                    {choices[st.session_state.computer_choice]}
                </div>
                <div class="choice-text">
                    {st.session_state.computer_choice}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 승패 결과
    st.markdown(
        f"""
        <div class="result-box">
            <div style="
                font-size:36px;
                font-weight:900;
                color:{result_color};
            ">
                {result_text}
            </div>
            <div style="font-size:18px; color:#475569; margin-top:10px;">
                {message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🔄 한 번 더 도전하기", use_container_width=True):
        st.rerun()


# 게임 기록
if st.session_state.history:

    st.divider()
    st.subheader("📋 최근 게임 기록")

    for i, record in enumerate(st.session_state.history):
        st.write(
            f"**{i + 1}회차** | "
            f"나: {choices[record['사용자']]} {record['사용자']} | "
            f"컴퓨터: {choices[record['컴퓨터']]} {record['컴퓨터']} | "
            f"{record['결과']}"
        )


# 기록 초기화
st.divider()

if st.button("🗑️ 전체 기록 초기화", use_container_width=True):
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0
    st.session_state.history = []
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None
    st.rerun()


# 하단 문구
st.markdown("""
<div style="
    text-align:center;
    color:#94a3b8;
    font-size:14px;
    margin-top:30px;
">
    ✨ ROCK · PAPER · SCISSORS CHALLENGE ✨<br>
    오늘의 승부사는 바로 당신!
</div>
""", unsafe_allow_html=True)
