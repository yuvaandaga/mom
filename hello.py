import streamlit as st
import random

# App title
st.set_page_config(page_title="Why I Love You, Mom 💖", page_icon="🌷", layout="centered")
st.title("💐 Why I Love You, Mom 💐")
st.write("Click the button below to reveal a reason why you're the best mom in the world! 🥰")

# List of reasons
reasons = [
    "You always put others before yourself 💞",
    "Your hugs can fix anything 🤗",
    "You make every place feel like home 🏡",
    "You never gave up on me — ever 🙌",
    "You make the yummiest food in the world 🍲",
    "You listen to me even when I don't make sense 🎧",
    "You believe in me more than I believe in myself 💪",
    "You taught me how to be kind and strong at the same time 💐",
    "You are my forever best friend 💬",
    "You’re the reason I smile a little more each day 😊"
]

# Button to generate reason
if st.button("💝 Show me a reason!"):
    st.success(random.choice(reasons))

# Footer
st.markdown("---")
st.markdown("<center><sub>Made with love by your [Beta/Beti/Bachha] 💖</sub></center>", unsafe_allow_html=True)
