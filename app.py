import streamlit as st
import random
import time

st.set_page_config(page_title="Dice", page_icon="🎲")

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

if "dice" not in st.session_state:
    st.session_state.dice = "⚀"

display = st.empty()

def show(face):
    display.markdown(
        f"""
        <div style="
            font-size:40vw;
            text-align:center;
            line-height:1;
            margin-top:10vh;
            margin-bottom:10vh;
        ">
            {face}
        </div>
        """,
        unsafe_allow_html=True
    )

# 現在の目を表示
show(st.session_state.dice)

if st.button("ふる 🎲", use_container_width=True):

    # コロコロ演出（だんだん遅くなる）
    delays = [0.08, 0.08, 0.1, 0.12, 0.15, 0.2]

    for d in delays:
        face = random.choice(dice_faces)
        show(face)
        time.sleep(d)

    # 最終決定
    final = random.choice(dice_faces)
    st.session_state.dice = final
    show(final)
