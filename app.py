import streamlit as st
import random
import time

st.set_page_config(page_title="Dice", page_icon="🎲")

st.markdown(
    "<h1 style='text-align:center;'>🎲 Dice Roller 🎲</h1>",
    unsafe_allow_html=True
)

if "dice" not in st.session_state:
    st.session_state.dice = None

st.divider()

display = st.empty()

if st.session_state.dice:
    display.markdown(
        f"<div style='font-size:120px; text-align:center;'>"
        f"{st.session_state.dice}"
        f"</div>",
        unsafe_allow_html=True
    )
else:
    display.markdown(
        "<div style='font-size:60px; text-align:center; color:gray;'>？</div>",
        unsafe_allow_html=True
    )

st.divider()

if st.button("サイコロをふる 🎲", use_container_width=True):
    with st.spinner("ころころころ…"):
        time.sleep(0.5)
    st.session_state.dice = random.randint(1, 6)
