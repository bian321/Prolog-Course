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

@st.cache_resource
def load_model():
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        return genai.GenerativeModel(models[0]) if models else None
    except: return None



model = load_model()

# تعليمات "النظام" المخصصة لهذا البوت
system_prompt = """
أنت خبير ومحلل منطقي متقدم جداً في لغة Prolog ومتخصص في تحليل النصوص الشريفة (آيات قرآنية، قصص الأنبياء، وأحكام المواريث).
عندما يعطيك المستخدم آية قرآنية أو نصاً تشريعياً، قم بتحليله كالتالي:

1. إذا كان النص عن الأنبياء والأنساب والسلسلة:
   - استخرج علاقات النسب (أب، ابن، أخ، زوجة).
   - اكتب كود Prolog للحقائق (Facts).
   - استنتج سلسلة الأنبياء (مثال: الـ Ancestor أو الجد).

2. إذا كان النص عن المواريث والفرائض (مثل آيات سورة النساء):
   - حدد الورثة المذكورين (الزوج، الأولاد، الأبوين).
   - حدد النصيب المقدر لكل وارث بناءً على الآية الشريفة (النصف، الثلث، السدس، إلخ).
   - اكتب كود Prolog يحتوي على القواعد (Rules) التي تحسب الحصة تلقائياً بناءً على الشروط (مثال: إذا كان هناك ولد، الأم تأخذ السدس).

3. اشرح للمستخدم بالعربي البسيط كيف يمكن لكود البرولوج هذا أن يحسب المواريث أو يتتبع السلسلة المنطقية (السبب والمسبب).

تأكد من وضع كود البرولوج داخل بلوك كود نظيف: ```prolog ... ```
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
        st.markdown(response.text)

st.subheader("📊 جدول العلاقات المنطقية المستخرجة (الأنساب):")

# طلب من جيميني صياغة البيانات كجدول Markdown عشان ستريمليت يعرضه كجدول حقيقي
table_instruction = f"بناءً على القصة التالية، استخرج فقط العلاقات العائلية وضعها في جدول Markdown بأعمدة: (الشخص الأول، صلة القرابة، الشخص الثاني). النص: {prompt}"
try:
    table_response = model.generate_content(table_instruction)
    st.markdown(table_response.text)
except:
    pass

st.sidebar.info("💡 جرب كتابة قصة قصيرة وشوف كيف الذكاء الاصطناعي رح يفككها لمنطق برولوج!")
