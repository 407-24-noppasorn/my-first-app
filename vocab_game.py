import time
import streamlit as st

st.title("⏰ เกมเติมศัพท์จับเวลา")

# Initialize session state variables
for key in ["ans1_val", "ans2_val", "ans3_val", "ans4_val"]:
    if key not in st.session_state:
        st.session_state[key] = ""


def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    answers = [
        (ans1.strip().lower(), "apple", "ข้อ 1"),
        (ans2.strip().lower(), "fish", "ข้อ 2"),
        (ans3.strip().lower(), "mango", "ข้อ 3"),
        (ans4.strip().lower(), "pen", "ข้อ 4"),
    ]

    for user_ans, correct_ans, label in answers:
        if user_ans == correct_ans:
            st.success(f"✅ {label}: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ {label}: ยังไม่ถูกต้อง (คุณตอบ '{user_ans}')")

    st.info(f"🏅 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


st.button("🚀 เริ่มเล่นเกม", on_click=reset_game)

# Timer logic
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# Input fields bound directly to session state
st.session_state.ans1_val = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
st.session_state.ans2_val = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h` . 🐟",
    value=st.session_state.ans2_val,
)
st.session_state.ans3_val = st.text_input(
    "ข้อ 3: I love m _ _ g _. 🥭",
    value=st.session_state.ans3_val,
)
st.session_state.ans4_val = st.text_input(
    "ข้อ 4: I always use p _ _ to write . 🖊️",
    value=st.session_state.ans4_val,
)

# Submit button
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

# Trigger results dialog
if st.session_state.get("is_ended", False):
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val,
    )

st.divider()
st.write("นางสาวนภสร วงค์นิธิกุล เลขที่ 24 ม.4/7")
