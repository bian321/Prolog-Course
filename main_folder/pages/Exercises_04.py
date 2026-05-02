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
st.divider()

st.subheader("🚀 جرب الكود بنفسك!")
st.write("عشان تتقن البرولوج، لازم تجرب تكتب الكود وتنفذه. افتح المختبر الأونلاين من الرابط تحت:")

# استخدام رابط بدل زر لمنع مشاكل التنقل
st.markdown("""
<a href="https://swish.swi-prolog.org/" target="_blank" style="
    text-decoration: none;
    background-color: #ff4b4b;
    color: white;
    padding: 10px 20px;
    border-radius: 10px;
    font-weight: bold;
    display: inline-block;
">
    🔗 افتح محاكي SWISH Prolog أونلاين
</a>
""", unsafe_allow_html=True)

st.info("💡 نصيحة: انسخ كود 'شجرة العائلة' من التمرين الأول وجربه هناك!")
