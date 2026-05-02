import streamlit as st

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

# الرابط المباشر اللي جهزناه
podcast_url = "https://drive.google.com/uc?export=download&id=1wAQRGhUfzUDVTGh2jxilhj2RPcHZ4HyX"

# تشغيل البودكاست مباشرة
st.audio(podcast_url)

st.write("في هذا البودكاست، نناقش أهمية لغة البرولوج في الذكاء الاصطناعي.")
