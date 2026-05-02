import streamlit as st

st.title("🎥 المكتبة المرئية والمسموعة")

st.header("1. مقدمة شاملة (فيديو)")
st.video("https://app.steve.ai/video/3ZS4I0K4GHMKFO0O") 

st.divider()

st.header("🎧 بودكاست تعليمي")

# الرابط المباشر اللي جهزناه
podcast_url = "https://drive.google.com/uc?export=download&id=1wAQRGhUfzUDVTGh2jxilhj2RPcHZ4HyX"

# تشغيل البودكاست مباشرة
st.audio(podcast_url)

st.write("في هذا البودكاست، نناقش أهمية لغة البرولوج في الذكاء الاصطناعي.")
