import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Page config
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="🚀", layout="wide")

# Custom styling
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
}
.sub-text {
    text-align: center;
    color: gray;
}
.stButton>button {
    width: 100%;
    background-color: #0077b5;
    color: white;
    font-size: 18px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="big-title">🚀 LinkedIn Post Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Generate high-quality posts using AI</p>', unsafe_allow_html=True)

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Layout
col1, col2, col3 = st.columns(3)

fs = FewShotPosts()
tags = fs.get_tags()

with col1:
    selected_tag = st.selectbox("📌 Topic", options=tags)

with col2:
    selected_length = st.selectbox("📏 Length", options=length_options)

with col3:
    selected_language = st.selectbox("🌐 Language", options=language_options)

# Generate button
if st.button("✨ Generate Post"):
    with st.spinner("Generating your post..."):
        post = generate_post(selected_length, selected_language, selected_tag)

    st.success("✅ Post Generated Successfully!")

    st.markdown("### 📝 Your Post:")
    st.text_area("Generated Post", post, height=300)
