import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="محلل القصص المنطقي", page_icon="📖")

st.title("📖 المحلل المنطقي للقصص")
st.write("اكتب قصة (مثل قصة قابيل وهابيل) وسأقوم بتحويلها إلى علاقات وحقائق وقواعد بلغة Prolog!")

# الربط مع Gemini (تأكدي من وجود المفتاح في Secrets)
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("تأكدي من وجود مفتاح GOOGLE_API_KEY في إعدادات Secrets")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# إعداد النموذج
@st.cache_resource
def load_model():
    return genai.GenerativeModel('gemini-pro')

model = load_model()

# تعليمات "النظام" المخصصة لهذا البوت
system_prompt = """
أنت خبير في تحليل النصوص واستخراج المنطق الرياضي (Logic) وتحويله إلى لغة Prolog.
عندما يعطيك المستخدم قصة، اتبع الخطوات التالية:
1. استخراج الكيانات (الأشخاص، الأشياء).
2. استخراج العلاقات (الحقائق - Facts) مثل (أب، أم، ابن، يملك).
3. تحويل هذه العلاقات إلى كود Prolog دقيق (أحرف صغيرة، ينتهي بنقطة).
4. اقتراح قواعد (Rules) منطقية تناسب القصة (مثل قاعدة الأخ، قاعدة الجد).
5. شرح بسيط بالعربي لكيفية عمل الكود.

تأكد من كتابة الكود داخل بلوك كود: ```prolog ... ```
"""

# واجهة التشات
if "story_messages" not in st.session_state:
    st.session_state.story_messages = []

# عرض المحادثة
for message in st.session_state.story_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال القصة
if prompt := st.chat_input("اكتب القصة هنا... مثلاً: آدم والد قابيل وهابيل، وهما أخوان..."):
    st.session_state.story_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        full_instruction = f"{system_prompt}\n\nالقصة الحالية: {prompt}"
        response = model.generate_content(full_instruction)
        
        st.markdown(response.text)
        st.session_state.story_messages.append({"role": "assistant", "content": response.text})

st.sidebar.info("💡 جربي كتابة قصة قصيرة وشوفي كيف الذكاء الاصطناعي رح يفككها لمنطق برولوج!")
