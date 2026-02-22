import streamlit as st
import random
import time

st.set_page_config(page_title="Dice", page_icon="🎲")

# タイトル最小限
st.markdown(
    "<h3 style='text-align:center; margin-bottom:0;'>🎲 Dice 🎲</h3>",
    unsafe_allow_html=True
)

# セッション初期化
if "dice" not in st.session_state:
    st.session_state.dice = "⚀"

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# 表示エリア（画面の大部分を使う）
display = st.empty()

display.markdown(
    f"""
    <div style="
        font-size:40vw;
        text-align:center;
        line-height:1;
        margin-top:5vh;
        margin-bottom:5vh;
    ">
        {st.session_state.dice}
    </div>
    """,
    unsafe_allow_html=True
)

# ボタン（下に大きく）
if st.button("ふる 🎲", use_container_width=True):
    with st.spinner("ころころころ…"):
        time.sleep(0.4)
    st.session_state.dice = random.choice(dice_faces)
    st.rerun()
