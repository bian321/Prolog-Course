import streamlit as st
import requests
import os

# 1. إعداد الصفحة الأساسي
st.set_page_config(
    page_title="منصة PrologLogic التعليمية", 
    page_icon="🧩", 
    layout="centered"
)

# 2. كود الـ CSS السحري لحل مشكلة تداخل العربي والإنجليزي وضبط الخطوط والألوان
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    h1, h2, h3, h4, p, span, li, label, div {
        font-family: 'Cairo', sans-serif !important;
        unicode-bidi: plaintext !important; 
        text-align: right;
    }

    code {
        direction: ltr !important;
        display: inline-block;
        font-family: monospace !important;
        background-color: #f1f2f6;
        padding: 2px 6px;
        border-radius: 4px;
        color: #d63384;
    }

    [data-testid="stMarkdownContainer"] pre {
        direction: ltr !important;
        text-align: left !important;
        background-color: #2d3436 !important;
        border-radius: 8px;
    }
    [data-testid="stMarkdownContainer"] pre code {
        color: #f5f6fa !important;
        background-color: transparent !important;
    }

    [data-testid="stChatInput"] {
        direction: rtl;
    }
    [data-testid="stChatInput"] textarea {
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
    }
    
    .main-title {
        color: #2196F3;
        text-align: center;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #666666;
        text-align: center;
        margin-bottom: 25px;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. دالة الاتصال بمحرك Groq الذكي والسريع
if "GROQ_API_KEY" not in st.secrets:
    st.error("⚠️ تأكدي من وجود مفتاح GROQ_API_KEY في إعدادات Secrets الخاصة بـ Streamlit")
    st.stop()

def generate_groq_content(system_prompt, user_prompt):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
            "Content-Type": "application/json"
        }
        data = {
            # 🔴 تم التعديل هنا لاسم الموديل المعتمد والمستقر مجاناً
            "model": "llama-3.3-70b-versatile", 
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ حدث خطأ في الاتصال بمحرك الاستدلال: {e}"
# 4. تصميم الهيكل الرئيسي للموقع (العناوين والتبويبات)
st.markdown('<h1 class="main-title">🧩 منصة PrologLogic التعليمية</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">رحلتك التفاعلية لتعلم البرمجة المنطقية وتحليل الأنساب والقصص</p>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 المقدمة والأساسيات", 
    "🏗️ الحقائق والقواعد", 
    "📖 محلل القصص الذكي", 
    "🤖 المعلم الخصوصي", 
    "💻 مختبر برولوغ الحي"
])

# ==================== التبويب الأول: المقدمة والأساسيات ====================
with tab1:
    st.subheader("ما هي لغة البرولوج؟")
    st.write("""
    كلمة **Prolog** هي اختصار لـ **PROgramming in LOGic**. 
    على عكس اللغات التقليدية (مثل Python أو Java) التي نملي فيها على الكمبيوتر "كيف" يحل المشكلة خطوة بخطوة، في البرولوج نحن نخبر الكمبيوتر "ما هي" المشكلة والعلاقات، وهو يتكفل باستنتاج الحل تلقائياً!
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**💡 اللغات التقليدية (Imperative)**\n\nتعتمد على إعطاء أوامر متسلسلة للوصول للحل.")
    with col2:
        st.success("**🎯 لغة البرولوج (Declarative)**\n\nتعتمد على وصف الحقائق والقواعد، والكمبيوتر يستنتج الحل.")

# ==================== التبويب الثاني: الحقائق والقواعد ====================
with tab2:
    st.subheader("🏗️ اللبنات الأساسية: الحقائق والقواعد والاستعلامات")
    st.markdown("### 1. الحقائق (Facts)")
    st.code("""
% أمثلة على الحقائق في البرولوج:
parent(bayan, sanaatha).    % بيان هي أم (مؤسسة) مشروع "صنعتها"
likes(ali, prolog).         % علي يحب البرولوج
female(sara).               % سارة أنثى
    """, language="prolog")
    
    st.markdown("### 2. القواعد (Rules)")
    st.code("""
% مثال على قاعدة:
is_happy(X) :- likes(X, prolog).
    """, language="prolog")

# ==================== التبويب الثالث: محلل القصص المنطقي (جدول الأنساب) ====================
# ==================== التبويب الثالث: محلل القصص المنطقي ====================
with tab3:
    st.subheader("📖 المحلل المنطقي للقصص والنصوص الشريفة")
    st.write("اكتب قصة وسيقوم الذكاء الاصطناعي بتحويلها فوراً إلى منطق برولوج، مع استخراج شجرة العلاقات كجدول مرتب!")

system_prompt_story = """أنت خبير ومحلل منطقي ومترجم أنساب متقدم جداً في لغة Prolog.
ووظيفتك الأساسية هي استخراج العلاقات العائلية كاملة (المباشرة وغير المباشرة) من النص وتحويلها لمنطق صارم.

عندما يعطيك المستخدم نصاً، يجب أن تلتزم بالقوانين التالية:
1. تحليل العلاقات بالكامل: لا تقتصر على الحقائق المذكورة حرفياً؛ بل استنتج العلاقات غير المباشرة المذكورة في النص (مثل: علاقة الأعمام، الأخوال، الأجداد، والأحفاد) واشرح صلة القرابة بينهم بالكامل (مثل صلة يوسف بكرم).

2. أصول كود Prolog:
- اكتب الكود داخل بلوك نظيف بأسماء متغيرات إنجليزية واضحة: ```prolog ... ```
- الترتيب الإلزامي للحقائق: اسم_العلاقة(الأكبر، الأصغر). مثل: father(yaqoub, yousef) لتعني يعقوب والد يوسف.
- شروط صياغة القواعد (Rules): عند كتابة أي قاعدة مثل الأخ أو ابن العم، أضف دائماً شرط عدم التساوي (X \\== Y) لضمان عدم استنتاج أن الشخص قريب نفسه أثناء التراجع المنطقي (Backtracking).

3. أسلوب العرض والشرح:
- ابدأ بردك بكتابة كود Prolog النظيف.
- صغ مثالاً لسؤال (Query) ذكي يسأل عن علاقة غير مباشرة (مثل صلة القرابة بين شخصين بعيدين بالنص).
- اشرح التراجع المنطقي (Backtracking Trace) باللغة العربية خطوة بخطوة وكيف وصل المحرك للحل.
- في النهاية، صمم جدول Markdown شامل لكل شخصين في النص يوضح صلة القرابة بينهما بأعمدة: (الشخص الأول | صلة القرابة | الشخص الثاني).

تحدث باللغة العربية المبسطة والمشوقة لتناسب حضور من تخصصات مختلفة."""

    if "story_messages" not in st.session_state:
        st.session_state.story_messages = []

    for message in st.session_state.story_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if story_prompt := st.chat_input("اكتب القصة هنا... (مثال: يعقوب والد يوسف، ويوسف أخو بنيامين...)", key="story_input"):
        st.session_state.story_messages.append({"role": "user", "content": story_prompt})
        with st.chat_message("user"):
            st.markdown(story_prompt)

        with st.chat_message("assistant"):
            with st.spinner("جاري تحليل النص منطقياً واستخراج جدول العلاقات..."):
                response_text = generate_groq_content(system_prompt_story, story_prompt)
                st.markdown(response_text)
                st.session_state.story_messages.append({"role": "assistant", "content": response_text})

# ==================== التبويب الرابع: المعلم الخصوصي الذكي ====================
with tab4:
    st.subheader("🤖 معلم البرولوج الأكاديمي الخصوصي")
    
    system_prompt_tutor = "أنت خبير أكاديمي متخصص في لغة البرمجة المنطقية Prolog فقط. اشرح المفاهيم وحل المشكلات البرمجية بالعربية وبأسلوب ممتع ونظم الأكواد."

    if "tutor_messages" not in st.session_state:
        st.session_state.tutor_messages = [{"role": "assistant", "content": "مرحباً بك! أنا معلمك الخاص بلغة Prolog. كيف يمكنني مساعدتك اليوم؟"}]

    for msg in st.session_state.tutor_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if tutor_prompt := st.chat_input("اسألني: كيف أكتب قاعدة الـ Recursion في البرولوج؟", key="tutor_input"):
        st.session_state.tutor_messages.append({"role": "user", "content": tutor_prompt})
        with st.chat_message("user"):
            st.markdown(tutor_prompt)

        with st.chat_message("assistant"):
            with st.spinner("جاري صياغة الإجابة..."):
                response_text = generate_groq_content(system_prompt_tutor, tutor_prompt)
                st.markdown(response_text)
                st.session_state.tutor_messages.append({"role": "assistant", "content": response_text})

# ==================== التبويب الخامس: مختبر برولوغ الحي والتفاعلي ====================
with tab5:
    st.subheader("💻 مختبر برولوغ الحي والتفاعلي")
    st.write("اكتبي قواعدكِ وحقائقكِ بالأسفل، واطرحي سؤالكِ (Query) لتري النتيجة الحية مباشرة وكيف يفكر المحرك دون الحاجة لفتح مواقع خارجية!")
    
    col_code, col_query = st.columns([2, 1])
    
    with col_code:
        st.markdown("**1. اكتب قاعدة المعرفة هنا (Knowledge Base):**")
        default_kb = """parent(khaled, omar).
parent(omar, zayed).
grandfather(X, Y) :- parent(X, Z), parent(Z, Y)."""
        user_kb = st.text_area("أكواد البرولوج (Facts & Rules)", value=default_kb, height=150)
        
    with col_query:
        st.markdown("**2. اطرح سؤالك المنطقي:**")
        user_query = st.text_input("الاستعلام (Query)", value="grandfather(khaled, zayed).")
        st.write("")
        run_btn = st.button("🚀 تشغيل وتحليل الكود حياً")

    if run_btn:
        st.markdown("### 🎯 نتيجة التنفيذ الفورية:")
        
        engine_instruction = f"""
        أنت الآن تعمل كمحرك استدلال منطقي صارم للغة برولوغ (Prolog Inference Engine).
        أمامك قاعدة معرفة كتبها الطالب، واستعلام. قيم الاستعلام بناءً على القواعد فقط:
        1. ابدأ بكلمة "النتيجة:" واكتب إما 'true.' أو 'false.'.
        2. تحتها، اكتب عنوان "🔍 مسار التراجع المنطقي (Backtracking Trace):" واشرح للطالب باللغة العربية البسيطة كيف طابق المحرك المتغيرات وانتقل بين الشروط للوصول للحل.
        """
        
        with st.spinner("جاري تشغيل محرك برولوغ بالخلفية..."):
            response_text = generate_groq_content(engine_instruction, f"قاعدة المعرفة:\n{user_kb}\n\nالاستعلام:\n{user_query}")
            st.info(response_text)
                    
    st.divider()
    st.markdown("### 📝 تمارين تطبيقية استرشادية")
    with st.expander("🎯 التمرين الأول: صلة الأخت (Sister Rule)"):
        st.code("""sister(X, Y) :- female(X), parent(P, X), parent(P, Y), X \\== Y.""", language="prolog")

# 5. القائمة الجانبية الثابتة
with st.sidebar:
    st.markdown("### 🎓 مشروع السيمناريون")
    st.info("📌 **تحت إشراف:** د. أمجد سيف\n\n🎯 **تطوير الطالبة:** بيان ابو شيخه\n\n📚 تخصص: علم الحاسوب والتربية غير المنهجية (السنة الثالثة)")
