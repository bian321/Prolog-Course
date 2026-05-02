import streamlit as st

st.set_page_config(page_title="الحقائق والقواعد - البرولوج", page_icon="🏗️")

st.title("🏗️ اللبنات الأساسية: الحقائق والقواعد")

st.markdown("""
في البرولوج، البرمجة عبارة عن بناء **قاعدة معرفة (Knowledge Base)**. هذه القاعدة تتكون من نوعين من الجمل:
""")

# القسم الأول: الحقائق
st.header("1. الحقائق (Facts)")
st.info("الحقيقة هي علاقة بسيطة بين الأشياء، وتعتبر دائماً صحيحة.")

st.code("""
# أمثلة على الحقائق في البرولوج:
parent(bayan, sanaatha).    % بيان هي أم (مؤسسة) مشروع "صنعتها"
likes(ali, prolog).         % علي يحب البرولوج
female(sara).               % سارة أنثى
""", language="prolog")

st.warning("⚠️ ملاحظة هامة: في البرولوج، يجب أن تنتهي كل جملة بنقطة `.` والأسماء تبدأ بحروف صغيرة (lowercase) إذا كانت ثوابت.")

st.divider()

# القسم الثاني: القواعد
st.header("2. القواعد (Rules)")
st.write("القاعدة هي حقيقة تعتمد على شرط معين. نستخدم الرمز `:-` ليعني 'إذا كان' (if).")



st.code("""
# مثال على قاعدة:
is_happy(X) :- likes(X, prolog).
# الترجمة: X يكون سعيداً "إذا كان" X يحب البرولوج.
""", language="prolog")

st.divider()

# القسم الثالث: الاستعلامات
st.header("3. الاستعلامات (Queries)")
st.write("بعد بناء قاعدة المعرفة، نسأل البرولوج أسئلة لنحصل على إجابات (True/False) أو قيم.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**السؤال:**")
    st.code("?- likes(ali, prolog).")
with col2:
    st.markdown("**إجابة البرولوج:**")
    st.success("true.")

st.divider()

# تحدي بسيط للطالب
st.subheader("🧩 تحدي سريع")
st.write("كيف نكتب بالبرولوج حقيقة تقول أن 'أحمد يلعب كرة القدم'؟")
if st.button("عرض الحل"):
    st.code("plays(ahmed, football).")
