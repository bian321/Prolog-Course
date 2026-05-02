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

# نصيحة للمستقبل: محاكي البرولوج
st.info("💡 نصيحة: بتقدري تضيفي رابط لـ **SWI-Prolog Online** عشان الطلاب يجربوا الكود تبعهم فوراً في المتصفح!")

if st.button("🔗 افتح محاكي البرولوج أونلاين"):
    st.markdown("[اضغط هنا للذهاب إلى SWISH Prolog](https://swish.swi-prolog.org/)")
