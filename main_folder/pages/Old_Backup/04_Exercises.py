import streamlit as st

st.set_page_config(page_title="تمارين تطبيقية - البرولوج", page_icon="📝")

st.title("📝 اختبر فهمك: تمارين تطبيقية")

st.write("""
أفضل طريقة لتعلم البرولوج هي المحاولة والخطأ. إليك مجموعة من التمارين المتدرجة في الصعوبة. 
حاول كتابة الكود في مفكرتك أولاً ثم قارنه بالحل الصحيح.
""")

st.divider()

# التمرين الأول: شجرة العائلة البسيطة
st.header("التمرين الأول: العلاقات العائلية")
st.markdown("""
بناءً على الحقائق التالية:
* `parent(mohammad, bayan).`
* `parent(mohammad, ali).`
* `female(bayan).`

**المطلوب:** اكتب قاعدة `sister(X, Y)` التي تحدد إذا كانت X هي أخت Y. 
*(تلميح: الأخت يجب أن تكون أنثى ولديها نفس الأب/الأم)*.
""")

if st.button("إظهار حل التمرين الأول"):
    st.code("""
sister(X, Y) :- 
    female(X), 
    parent(P, X), 
    parent(P, Y), 
    X \== Y.  % للتأكد أن الشخص ليس أخاً لنفسه
    """, language="prolog")

st.divider()

# التمرين الثاني: المنطق الحسابي
st.header("التمرين الثاني: المقارنة الحسابية")
st.markdown("""
اكتب قاعدة `can_vote(Person)` التي تحدد إذا كان الشخص مسموحاً له بالتصويت (إذا كان عمره 18 فما فوق).
استخدم الحقائق:
* `age(bayan, 21).`
* `age(sami, 15).`
""")

if st.button("إظهار حل التمرين الثاني"):
    st.code("""
can_vote(Person) :- 
    age(Person, Age), 
    Age >= 18.
    """, language="prolog")



st.divider()
st.subheader("💻 مختبر برولوغ الحي (جرب كودك هنا!)")
st.write("اكتب القواعد والحقائق بالأسفل، واطرح سؤالك (Query) لترى النتيجة الفورية:")

# تقسيم الشاشة لجزأين
col_code, col_query = st.columns([2, 1])

with col_code:
    default_kb = """parent(khaled, omar).
parent(omar, zayed).
grandfather(X, Y) :- parent(X, Z), parent(Z, Y)."""
    user_kb = st.text_area("أكواد البرولوج (Facts & Rules)", value=default_kb, height=150)
    
with col_query:
    user_query = st.text_input("الاستعلام (Query)", value="grandfather(khaled, zayed).")
    run_btn = st.button("🚀 تشغيل المنطق حياً")

if run_btn:
    # إرسال الكود لجيميني ليقوم بدور محرك البروليرغ الصارم ويحسب النتيجة حياً أمام اللجنة
    engine_instruction = f"أنت محرك استدلال منطقي لغة برولوغ (Prolog Engine). قيم هذا الاستعلام بناءً على القواعد فقط. قاعدة المعرفة:\n{user_kb}\n\nالاستعلام:\n{user_query}\n\nأعط النتيجة كـ true أو false مع شرح التراجع (Backtracking) بالعربية."
    with st.spinner("جاري التقييم..."):
        try:
            engine_response = model.generate_content(engine_instruction)
            st.info(engine_response.text)
        except Exception as e:
            st.error(f"خطأ: {e}")
