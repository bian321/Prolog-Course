import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="مساعد البرولوج الذكي", page_icon="🤖")

st.title("🤖 معلم البرولوج الخصوصي")
st.write("اسألني أي سؤال عن لغة Prolog، القواعد، الحقائق، أو حتى اطلب مني شرح كود معين!")

# الربط مع Gemini (نفس طريقتك الشغالة)
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("تأكدي من وجود المفتاح في Secrets")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

@st.cache_resource
def load_model():
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        return genai.GenerativeModel(models[0]) if models else None
    except: return None

model = load_model()

# إدارة الجلسة
if "prolog_messages" not in st.session_state:
    st.session_state.prolog_messages = [
        {"role": "assistant", "content": "أهلاً بك! أنا خبير في لغة Prolog. كيف يمكنني مساعدتك في فهم المنطق اليوم؟"}
    ]

# عرض الرسائل
for msg in st.session_state.prolog_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# التفاعل
if prompt := st.chat_input("مثلاً: كيف أكتب قاعدة Recursion في البرولوج؟"):
    st.session_state.prolog_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if model:
            try:
                # أهم جزء: تخصص البوت
                system_instruction = (
                    "أنت خبير أكاديمي متخصص في لغة البرمجة المنطقية Prolog فقط. "
                    "مهمتك شرح المفاهيم، حل المشكلات البرمجية في البرولوج، وتصحيح الكود للمستخدم. "
                    "إذا سألك المستخدم عن أي موضوع خارج البرولوج (مثل طبخ، سياسة، أو لغات أخرى)، "
                    "اعتذر منه بلباقة وقل له أنك متخصص في البرولوج فقط. "
                    "تحدث بلغة عربية بسيطة وسلسة."
                )
                
                full_prompt = f"{system_instruction}\n\nسؤال المستخدم: {prompt}"
                response = model.generate_content(full_prompt)
                
                st.markdown(response.text)
                st.session_state.prolog_messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"خطأ: {e}")
