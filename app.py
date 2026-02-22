import streamlit as st
import random
import time

st.set_page_config(page_title="Garden Dice", page_icon="🎲")

# ===== 背景を庭グリーンに =====
st.markdown(
    """
    <style>
    .stApp {
        background-color: #9EDC8A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

if "dice" not in st.session_state:
    st.session_state.dice = "⚀"

display = st.empty()

def show(face, size="40vw"):
    display.markdown(
        f"""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            margin-top:10vh;
            margin-bottom:10vh;
        ">
            <div style="
                width:30vw;
                height:30vw;
                background:white;
                border-radius:20%;
                display:flex;
                justify-content:center;
                align-items:center;
                font-size:{size};
                box-shadow:0 8px 20px rgba(0,0,0,0.25);
            ">
                {face}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# 現在表示
show(st.session_state.dice)

if st.button("ふる 🎲", use_container_width=True):

    # コロコロ演出
    delays = [0.08, 0.08, 0.1, 0.12, 0.15, 0.2]

    for d in delays:
        face = random.choice(dice_faces)
        show(face, "40vw")
        time.sleep(d)

    # ===== 最終決定 =====
    final = random.choice(dice_faces)
    st.session_state.dice = final

    # 少し大きく表示
    show(final, "48vw")
    time.sleep(0.25)

    # 通常サイズに戻す（落ち着き）
    show(final, "40vw")
