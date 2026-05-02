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



st.header("🎧 بودكاست تعليمي")

# هذا هو الرابط المباشر الصحيح لملفك
podcast_url = "https://drive.google.com/uc?export=download&id=1wAQRGhUfzUDVTGh2jxilhj2RPcHZ4HyX"

try:
    st.audio(podcast_url)
    st.success("تم تحميل البودكاست بنجاح!")
except Exception as e:
    st.error(f"حدث خطأ في تحميل الصوت: {e}")
st.write("في هذا البودكاست، نناقش أهمية لغة البرولوج في الذكاء الاصطناعي.")
