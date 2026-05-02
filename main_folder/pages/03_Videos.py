import streamlit as st
import os
assets_path = "main_folder/assets" 

st.title("🎥 المكتبة المرئية والمسموعة")
st.subheader("📺 فيديو ")
video_file_path = os.path.join(assets_path, "video1.mp4")

if os.path.exists(video_file_path):
    video_file = open(video_file_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    # هاد السطر رح يساعدك تعرفي وين بايثون عم بيدوّر بالظبط لو لسه فيه مشكلة
    st.error(f"الملف غير موجود في: {video_file_path}")

import streamlit.components.v1 as components


st.header("🎧 بودكاست تعليمي")


# تضمين مشغل Cloudinary
cloudinary_embed_url = "https://player.cloudinary.com/embed/?cloud_name=dnaaujzam&public_id=audio1_q73mmw"

components.iframe(cloudinary_embed_url, height=100)
st.write("في هذا البودكاست، نناقش أهمية لغة البرولوج في الذكاء الاصطناعي.")
