import streamlit as st

st.set_page_config(page_title="تعلم البرولوج | Prolog Path", page_icon="🧩")

st.title("🧩 رحلتك في عالم المنطق: لغة Prolog")
st.write("""
أهلاً بك في المساق التعليمي التفاعلي للغة البرولوج. 
هذا الموقع صُمم ليكون مرجعك الشامل من البداية وحتى الاحتراف بأسلوب بسيط وواضح.
""")

st.info("استخدم القائمة الجانبية للتنقل بين الوحدات التعليمية.")

# إضافة صورة توضيحية لمنطق البرولوج
st.image("https://upload.wikimedia.org/wikipedia/commons/2/22/Prolog_logo.png", width=200)

st.subheader("ماذا ستتعلم هنا؟")
st.markdown("""
* **الأساسيات:** الحقائق، القواعد، والاستعلامات.
* **المنطق:** كيف يفكر البرولوج؟ (Backtracking & Unification).
* **التطبيق:** بناء أنظمة خبيرة بسيطة.
""")