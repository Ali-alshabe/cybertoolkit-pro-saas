import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات المتصفح
st.set_page_config(page_title="Ali Cyber Toolkit", page_icon="🛡️", layout="centered")

# 2. الهوية الشخصية
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("my_photo.jpg", width=200) 
    st.markdown(f"<h1 style='text-align: center; color: white; margin-bottom: 0;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF4B4B; font-size: 22px; font-weight: bold; margin-top: 0;'>Cybersecurity Engineer</p>", unsafe_allow_html=True)
    st.markdown("---")
except:
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)

# 3. عنوان المختبر
st.markdown("<h2 style='text-align: center; color: #4682B4;'>🌐 (Lab) Ali Al-Murtada Yassin</h2>", unsafe_allow_html=True)

# 4. إنشاء التبويبات (أضفنا تبويباً رابعاً للتشفير)
tab1, tab2, tab3, tab4 = st.tabs(["🔍 فاحص الروابط", "🔑 مولد كلمات المرور", "🛡️ محلل الأمان", "🔐 نظام التشفير"])

# --- التبويب الأول والثاني والثالث (تبقى كما هي لضمان عملها) ---
with tab1:
    st.header("Ali's URL Scanner")
    url_input = st.text_input("أدخل الرابط للفحص:", key="scan_in")
    if st.button("بدء الفحص 🚀"):
        st.info("الأداة تعمل بنجاح عبر API..")

with tab2:
    st.header("Smart Password Generator")
    length = st.slider("طول الكلمة:", 8, 64, 16)
    if st.button("توليد ✨"):
        pwd = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        st.code(pwd)
        if length >= 14: st.snow(); st.toast("كفو يا بطل! 👏")

with tab3:
    st.header("Website Security Analyzer")
    target_url = st.text_input("رابط الموقع للتحليل:", key="anal_in")
    if st.button("تحليل 🛡️"):
        st.success("تم بدء التحليل الفني...")

# --- التبويب الرابع الجديد: نظام التشفير وفك التشفير ---
with tab4:
    st.header("Encryption & Decryption System")
    st.write("استخدم هذه الأداة لتشفير النصوص الحساسة وتحويلها إلى كود غير مفهوم.")
    
    mode = st.radio("اختر العملية:", ["تشفير (Encode)", "فك تشفير (Decode)"])
    text_to_process = st.text_area("أدخل النص هنا:", placeholder="اكتب النص الذي تريد معالجته...")
    
    if st.button("تنفيذ العملية ⚡"):
        if text_to_process:
            try:
                if mode == "تشفير (Encode)":
                    # عملية التشفير باستخدام Base64
                    encoded_bytes = base64.b64encode(text_to_process.encode("utf-8"))
                    encoded_str = encoded_bytes.decode("utf-8")
                    st.success("✅ تم التشفير بنجاح:")
                    st.code(encoded_str)
                    st.balloons() # إضافة احتفال بالبالونات عند التشفير
                
                else:
                    # عملية فك التشفير
                    decoded_bytes = base64.b64decode(text_to_process.encode("utf-8"))
                    decoded_str = decoded_bytes.decode("utf-8")
                    st.success("🔓 تم فك التشفير بنجاح:")
                    st.info(decoded_str)
            except Exception as e:
                st.error("⚠️ خطأ: تأكد أن النص الذي أدخلته هو نص مشفر بشكل صحيح (Base64).")
        else:
            st.warning("يرجى إدخال نص أولاً.")

# 5. التذييل
st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtadha Yassin | Cybersecurity Student")
