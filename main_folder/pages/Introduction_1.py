import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="المقدمة - عالم المنطق", page_icon="💡")

st.title("💡 مقدمة في لغة البرولوج (Prolog)")

st.markdown("""
### ما هي لغة البرولوج؟
كلمة **Prolog** هي اختصار لـ **PROgramming in LOGic**. 
على عكس اللغات اللي بنعرفها (مثل Python أو Java) اللي بنحكي فيها للكمبيوتر "كيف" يحل المشكلة، في البرولوج بنحكي للكمبيوتر "شو" هي المشكلة وهوه بيحلها!
""")

# إضافة فيديو توضيحي (من مجلد assets أو رابط)
st.subheader("📺 فيديو تعريفي")
video_file_path = os.path.join(assets_path, "video1.mp4")

if os.path.exists(video_file_path):
    video_file = open(video_file_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    st.error("عذراً، ملف الفيديو غير موجود في مجلد assets")

st.divider()

### الفرق الجوهري (مهم جداً للفهم)
st.subheader("🤔 كيف بتفكر لغة البرولوج؟")
col1, col2 = st.columns(2)

with col1:
    st.info("**اللغات التقليدية (Imperative)**\n\nبنعطي أوامر متسلسلة (خطوة بخطوة).")

with col2:
    st.success("**لغة البرولوج (Declarative)**\n\nبنعطي حقائق وقواعد، والكمبيوتر بيستنتج الحل.")

# صورة توضيحية لمنطق الاستنتاج
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Logic_gate_and.svg/1200px-Logic_gate_and.svg.png", 
         caption="البرولوج يعتمد على المنطق الرياضي (Logic Gate Thinking)", width=300)

st.markdown("""
### مجالات استخدام البرولوج:
1. **الذكاء الاصطناعي (AI):** بناء الأنظمة الخبيرة.
2. **معالجة اللغات الطبيعية (NLP):** فهم اللغات البشرية.
3. **قواعد البيانات:** البحث الذكي في العلاقات المعقدة.
""")

st.success("جاهز ننتقل للدرس الجاي؟ رح نتعلم كيف نكتب أول جملة بالبرولوج!")
