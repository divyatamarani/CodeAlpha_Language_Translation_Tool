import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    color:#0f62fe;
    text-align:center;
}
.copy-btn{
    margin-top:10px;
}
.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("🌍 AI Language Translation Tool")

st.write(
    "Translate text between different languages instantly using Artificial Intelligence."
)

# ---------------- Languages ----------------
languages = {
    "English":"en",
    "Hindi":"hi",
    "Telugu":"te",
    "Tamil":"ta",
    "Kannada":"kn",
    "Malayalam":"ml",
    "Marathi":"mr",
    "Gujarati":"gu",
    "Punjabi":"pa",
    "Bengali":"bn",
    "Urdu":"ur",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Italian":"it",
    "Portuguese":"pt",
    "Russian":"ru",
    "Japanese":"ja",
    "Korean":"ko",
    "Chinese":"zh-CN",
    "Arabic":"ar"
}

# ---------------- Session State ----------------
if "history" not in st.session_state:
    st.session_state.history = []
    # ---------------- Language Selection ----------------
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "🌐 Source Language",
        list(languages.keys()),
        index=0
    )

with col2:
    target = st.selectbox(
        "🌍 Target Language",
        list(languages.keys()),
        index=1
    )

# ---------------- Swap Button ----------------
if st.button("🔄 Swap Languages"):
    source, target = target, source

# ---------------- Input ----------------
text = st.text_area(
    "✍ Enter Text",
    height=150,
    placeholder="Type or paste text here..."
)

# ---------------- Translate ----------------
if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("⚠ Please enter some text.")
    else:
        try:

            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("✅ Translation Successful")

            st.text_area(
                "📄 Translated Text",
                translated,
                height=150
            )

            if st.button("📋 Copy Translation"):
                pyperclip.copy(translated)
                st.success("Copied to clipboard!")

            st.session_state.history.append({
                "From": source,
                "To": target,
                "Input": text,
                "Output": translated
            })

        except Exception as e:
            st.error(f"❌ {e}")
            # ---------------- Translation History ----------------
if st.session_state.history:

    st.markdown("---")
    st.subheader("📜 Translation History")

    for item in reversed(st.session_state.history):

        with st.expander(
            f"{item['From']} ➜ {item['To']}"
        ):

            st.write("**Input:**")
            st.write(item["Input"])

            st.write("**Output:**")
            st.write(item["Output"])

# ---------------- Footer ----------------
st.markdown("---")

st.markdown(
    """
<div class='footer'>
Built using ❤️ with Python, Streamlit & Google Translator API
</div>
""",
    unsafe_allow_html=True
)