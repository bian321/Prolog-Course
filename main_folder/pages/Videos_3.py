import streamlit as st
import os
assets_path = "main_folder/assets" 

st.title("🎥 المكتبة المرئية والمسموعة")
st.subheader("📺 فيديو تعريفي")
video_file_path = os.path.join(assets_path, "video1.mp4")

if os.path.exists(video_file_path):
    video_file = open(video_file_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    # هاد السطر رح يساعدك تعرفي وين بايثون عم بيدوّر بالظبط لو لسه فيه مشكلة
    st.error(f"الملف غير موجود في: {video_file_path}")


import streamlit as st

st.header("🎧 بودكاست تعليمي")

# الرابط الجديد المباشر
# لاحظي استخدمنا uc?id= بدلاً من export=download في البداية
podcast_url = "https://drive.google.com/file/d/1wAQRGhUfzUDVTGh2jxilhj2RPcHZ4HyX/view?usp=sharing"

# نستخدم st.audio مع تحديد النوع
st.audio(podcast_url, format="audio/m4a")

st.write("في هذا البودكاست، نناقش أهمية لغة البرولوج في الذكاء الاصطناعي.")
