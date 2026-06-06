import streamlit as st
import google.generativeai as genai
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
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* ضبط الخط والاتجاه العام للموقع بالكامل للعربية */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    /* منع تداخل الكلمات الإنجليزية والعربية داخل النصوص ويحافظ على ترتيب الأقواس */
    h1, h2, h3, h4, p, span, li, label, div {
        font-family: 'Cairo', sans-serif !important;
        unicode-bidi: plaintext !important; 
        text-align: right;
    }

    /* عزل الأكواد الإنجليزية الصغيرة لتبقى مرتبة من اليسار لليمين دون تخريب السطر العربي */
    code {
        direction: ltr !important;
        display: inline-block;
        font-family: monospace !important;
        background-color: #f1f2f6;
        padding: 2px 6px;
        border-radius: 4px;
        color: #d63384;
    }

    /* ضبط صناديق النصوص البرمجية الكبيرة (Prolog Code Blocks) */
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

    /* ضبط شريط إدخال الشات وتوجيهه لليمين */
    [data-testid="stChatInput"] {
        direction: rtl;
    }
    [data-testid="stChatInput"] textarea {
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
    }
    
    /* تجميل العناوين */
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

# 3. إعداد نموذج Gemini الذكي (قراءة المفتاح من الـ Secrets)
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("⚠️ تأكدي من وجود مفتاح GOOGLE_API_KEY في إعدادات Secrets الخاصة بـ Streamlit")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

@st.cache_resource
def load_model():
    try:
        # تثبيت اسم الموديل مباشرة بدل طلب اللستة كل مرة
        return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return None

model = load_model()

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

    st.markdown("""
    ### 🚀 مجالات الاستخدام:
    1. **الذكاء الاصطناعي (AI):** بناء الأنظمة الخبيرة التي تحاكي اتخاذ القرار البشري.
    2. **معالجة اللغات الطبيعية (NLP):** تحليل وفهم القواعد اللغوية المعقدة.
    3. **قواعد البيانات الذكية:** تتبع العلاقات المعقدة مثل الأنساب والمواريث.
    """)

# ==================== التبويب الثاني: الحقائق والقواعد ====================
with tab2:
    st.subheader("🏗️ اللبنات الأساسية: الحقائق والقواعد والاستعلامات")
    
    st.markdown("### 1. الحقائق (Facts)")
    st.info("الحقيقة هي علاقة بسيطة بين الأشياء، وتعتبر دائماً صحيحة في النظام.")
    st.code("""
% أمثلة على الحقائق في البرولوج:
parent(bayan, sanaatha).    % بيان هي أم (مؤسسة) مشروع "صنعتها"
likes(ali, prolog).         % علي يحب البرولوج
female(sara).               % سارة أنثى
    """, language="prolog")
    st.warning("⚠️ تنبيه برامجي: يجب أن تنتهي كل جملة بنقطة `.` والأسماء تبدأ بحروف صغيرة (lowercase) إذا كانت ثوابت.")
    
    st.markdown("### 2. القواعد (Rules)")
    st.write("القاعدة هي حقيقة مشروطة. نستخدم الرمز `:-` ليعني 'إذا كان' (if).")
    st.code("""
% مثال على قاعدة:
is_happy(X) :- likes(X, prolog).
% الترجمة: X يكون سعيداً إذا كان X يحب البرولوج.
    """, language="prolog")
    
    st.markdown("### 3. الاستعلامات (Queries)")
    st.write("بعد بناء قاعدة المعرفة، نسأل البرولوج أسئلة لنحصل على إجابات إما بنعم/لا أو بقيم مخصصة.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**السؤال المعروض:**")
        st.code("?- likes(ali, prolog).")
    with c2:
        st.markdown("**إجابة محرك البرولوج:**")
        st.success("true.")

# ==================== التبويب الثالث: محلل القصص المنطقي (جدول الأنساب) ====================
with tab3:
    st.subheader("📖 المحلل المنطقي للقصص والنصوص الشريفة")
    st.write("اكتب قصة (مثل قصة عائلية، أو نسب من قصص الأنبياء، أو آيات المواريث) وسيقوم الذكاء الاصطناعي بتحويلها فوراً إلى منطق برولوج، مع استخراج شجرة العلاقات كجدول مرتب!")

    system_prompt_story = """
    أنت خبير ومحلل منطقي متقدم جداً في لغة Prolog ومتخصص في تحليل النصوص الشريفة (آيات قرآنية، قصص الأنبياء، وأحكام المواريث والأنساب).
    عندما يعطيك المستخدم نصاً، قم بتحليله كالتالي:
    1. اكتب كود Prolog للحقائق (Facts) والقواعد (Rules) المستخرجة داخل بلوك كود نظيف: ```prolog ... ```
    2. صغ مثالاً لسؤال (Query) يمكن طرحه على هذا الكود.
    3. اشرح للمستخدم بالعربي البسيط خطوة بخطوة كيف يقوم محرك البرولوج بالاستنتاج والتراجع (Backtracking) لحل هذا السؤال لتبسيط المفهوم الأكاديمي.
    4. في نهاية ردك، قم بعمل جدول Markdown يوضح العلاقات العائلية والأنساب المستخرجة بأعمدة واضحة: (الشخص الأول | صلة القرابة | الشخص الثاني).
    تحدث بلغة عربية سلسة وواضحة جداً، واجعل الرموز البرمجية الإنجليزية معزولة لتكون مرتبة.
    """

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
                try:
                    full_instruction = f"{system_prompt_story}\n\nالنص الحالي للتحليل: {story_prompt}"
                    response = model.generate_content(full_instruction)
                    st.markdown(response.text)
                    st.session_state.story_messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.warning("⚠️ محرك الـ API مضغوط حالياً بسبب كثرة الطلبات المتتالية. الرجاء الانتظار نصف دقيقة وإرسال النص مجدداً للتحليل.")

# ==================== التبويب الرابع: المعلم الخصوصي الذكي ====================
with tab4:
    st.subheader("🤖 معلم البرولوج الأكاديمي الخصوصي")
    st.write("اسألني أي سؤال يخطر ببالك عن لغة Prolog (كيفية كتابة الأكواد، الـ Recursion، الـ Unification) وسأشرحه لك كبروفيسور حاسوب!")

    system_prompt_tutor = """
    أنت خبير أكاديمي وبروفيسور متخصص في لغة البرمجة المنطقية Prolog فقط. 
    مهمتك شرح المفاهيم، حل المشكلات البرمجية وتصحيح الكود للمستخدم بأسلوب تعليمي ممتع.
    إذا سألك المستخدم عن أي موضوع خارج البرولوج، اعتذر منه بلباقة وقل له أنك متخصص في البرولوج ومساعدته في المنطق فقط.
    احرص على تنظيم النص العربي وتنسيق الأكواد الإنجليزية لتبدو مريحة للعين دون أي تداخل في السطور.
    """

    if "tutor_messages" not in st.session_state:
        st.session_state.tutor_messages = [
            {"role": "assistant", "content": "مرحباً بك! أنا معلمك الخاص بلغة Prolog. كيف يمكنني إضاءة درب المنطق لك اليوم؟"}
        ]

    for msg in st.session_state.tutor_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if tutor_prompt := st.chat_input("اسألني: كيف أكتب قاعدة الـ Recursion في البرولوج? ", key="tutor_input"):
        st.session_state.tutor_messages.append({"role": "user", "content": tutor_prompt})
        with st.chat_message("user"):
            st.markdown(tutor_prompt)

        with st.chat_message("assistant"):
            with st.spinner("جاري صياغة الإجابة الأكاديمية المنظمة..."):
                try:
                    full_prompt = f"{system_prompt_tutor}\n\nسؤال الطالب: {tutor_prompt}"
                    response = model.generate_content(full_prompt)
                    st.markdown(response.text)
                    st.session_state.tutor_messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.warning("⚠️ السيرفر مشغول حالياً بطلبات أخرى. الرجاء الانتظار قليلاً ثم إعادة كتابة سؤالك.")

# ==================== التبويب الخامس: مختبر برولوغ التفاعلي والمباشر ====================
with tab5:
    st.subheader("💻 مختبر برولوغ الحي والتفاعلي")
    st.write("اكتبي قواعدكِ وحقائقكِ بالأسفل، واطرحي سؤالكِ (Query) لتري النتيجة الحية مباشرة وكيف يفكر المحرك دون الحاجة لفتح مواقع خارجية!")
    
    # تقسيم الشاشة لجزأين: إدخال الكود والاستعلام
    col_code, col_query = st.columns([2, 1])
    
    with col_code:
        st.markdown("**1. اكتب قاعدة المعرفة هنا (Knowledge Base):**")
        default_kb = """parent(khaled, omar).
parent(omar, zayed).
parent(omar, sara).

grandfather(X, Y) :- parent(X, Z), parent(Z, Y)."""
        user_kb = st.text_area("أكواد البرولوج (Facts & Rules)", value=default_kb, height=180, help="اكتب الحقائق والقواعد بالإنجليزية")
        
    with col_query:
        st.markdown("**2. اطرح سؤالك المنطقي:**")
        user_query = st.text_input("الاستعلام (Query)", value="grandfather(khaled, zayed).", help="مثال: grandfather(khaled, zayed).")
        st.write("")
        run_btn = st.button("🚀 تشغيل وتحليل الكود حياً")

    # تشغيل المحاكي المنطقي المباشر عند الضغط على الزر
    if run_btn:
        st.markdown("### 🎯 نتيجة التنفيذ الفورية:")
        
        engine_instruction = f"""
        أنت الآن تعمل كمحرك استدلال منطقي صارم للغة برولوغ (Prolog Inference Engine).
        أمامك قاعدة معرفة (Knowledge Base) كتبها الطالب، واستعلام (Query).
        
        قاعدة المعرفة:
        {user_kb}
        
        الاستعلام المطلوب حله:
        {user_query}
        
        قم بتقييم الاستعلام بناءً على القواعد المعطاة فقط:
        1. ابدأ بكلمة "النتيجة:" واكتب إما 'true.' أو 'false.' أو اسم المتغير إذا كان الاستعلام يبحث عن مجهول (مثل X = omar).
        2. تحتها، اكتب عنوان "🔍 مسار التراجع المنطقي (Backtracking Trace):" واشرح للطالب باللغة العربية البسيطة والمستقيمة كيف قام المحرك بمطابقة المتغيرات والانتقال من شرط إلى شرط خطوة بخطوة للوصول للحل.
        """
        
        with st.spinner("جاري تشغيل محرك برولوغ الاستدلالي بالخلفية..."):
            try:
                engine_response = model.generate_content(engine_instruction)
                st.info(engine_response.text)
            except Exception as e:
                st.warning("⚠️ تخطينا الحد المسموح به للمفتاح المجاني حالياً. يرجى الانتظار 30 ثانية لتفريغ الذاكرة ثم الضغط على زر التشغيل مرة أخرى.")
                
    st.divider()
    st.markdown("### 📝 تمارين تطبيقية استرشادية")
    
    with st.expander("🎯 التمرين الأول: صلة الأخت (Sister Rule)"):
        st.write("الحقائق: `parent(mohammad, bayan).` و `parent(mohammad, ali).` و `female(bayan).` والقاعدة:")
        st.code("""sister(X, Y) :- female(X), parent(P, X), parent(P, Y), X \\== Y.""", language="prolog")
        
    with st.expander("🎯 التمرين الثاني: شروط السن الحسابي (Voting)"):
        st.write("القاعدة لمعرفة هل يحق للشخص التصويت بناءً على عمره (18 سنة فما فوق):")
        st.code("""can_vote(Person) :- age(Person, Age), Age >= 18.""", language="prolog")

# 5. معلومات إضافية ثابتة في الشاشة الجانبية لتعزيز العرض
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/22/Prolog_logo.png", width=120)
    st.markdown("### 🎓 مشروع السيمناريون")
    st.info("📌 **تحت إشراف:** د. أمجد سيف\n\n🎯 **تطوير الطالبة:** بيان ابو شيخه\n\n📚 تخصص: علم الحاسوب والتربية غير المنهجية (السنة الثالثة)")
    st.write("منصة متكاملة لربط المنطق اللغوي بالبرمجة الذكية وتسهيل المفاهيم المجردة.")
