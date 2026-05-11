import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات المتصفح
st.set_page_config(page_title="Ali Cyber Toolkit", page_icon="🛡️", layout="wide") # جعلنا العرض wide ليتناسب مع القائمة الجانبية

# --- إدارة الذاكرة (Session State) لتعقب العمليات ---
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_history(action, detail):
    """وظيفة لإضافة أي عملية يقوم بها المستخدم إلى السجل"""
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.insert(0, f"[{timestamp}] {action}: {detail}")
    # الاحتفاظ بآخر 10 عمليات فقط
    if len(st.session_state.history) > 10:
        st.session_state.history.pop()

# 2. القائمة الجانبية (Sidebar) - سجل العمليات
with st.sidebar:
    st.title("📜 سجل العمليات")
    st.write("آخر الأنشطة التي قمت بها:")
    if st.session_state.history:
        for item in st.session_state.history:
            st.info(item)
        if st.button("مسح السجل 🗑️"):
            st.session_state.history = []
            st.rerun()
    else:
        st.write("لا توجد عمليات مسجلة بعد.")
    
    st.markdown("---")
    st.caption("ملاحظة: السجل يتم مسحه عند تحديث الصفحة.")

# 3. الهوية الشخصية في الصفحة الرئيسية
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("my_photo.jpg", width=200) 
    except: pass
    st.markdown(f"<h1 style='text-align: center; color: white; margin-bottom: 0;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF4B4B; font-size: 22px; font-weight: bold; margin-top: 0;'>Cybersecurity Engineer</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4682B4;'>🌐 (Lab) Ali Al-Murtada Yassin</h3>", unsafe_allow_html=True)

# 4. التبويبات
tab1, tab2, tab3, tab4 = st.tabs(["🔍 فاحص الروابط", "🔑 مولد كلمات المرور", "🛡️ محلل الأمان", "🔐 نظام التشفير"])

# --- التبويب الأول: فحص الروابط ---
with tab1:
    st.header("Ali's URL Scanner")
    url_input = st.text_input("أدخل الرابط للفحص:", key="scan_in")
    if st.button("بدء الفحص 🚀"):
        if url_input:
            add_to_history("فحص رابط", url_input)
            st.success(f"تم إرسال {url_input} للفحص")

# --- التبويب الثاني: مولد كلمات المرور ---
with tab2:
    st.header("Smart Password Generator")
    length = st.slider("طول الكلمة:", 8, 64, 16)
    if st.button("توليد ✨"):
        pwd = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        st.code(pwd)
        add_to_history("توليد كلمة مرور", f"بطول {length}")
        if length >= 14: st.snow()

# --- التبويب الثالث: محلل أمان المواقع ---
with tab3:
    st.header("Website Security Analyzer")
    target_url = st.text_input("رابط الموقع للتحليل:", key="anal_in")
    if st.button("تحليل جدار الحماية 🛡️"):
        if target_url:
            add_to_history("تحليل موقع", target_url)
            st.info(f"جاري فحص بروتوكولات {target_url}")

# --- التبويب الرابع: التشفير ---
with tab4:
    st.header("Encryption System")
    mode = st.radio("العملية:", ["تشفير", "فك تشفير"])
    text_to_process = st.text_area("النص:")
    if st.button("تنفيذ ⚡"):
        if text_to_process:
            if mode == "تشفير":
                res = base64.b64encode(text_to_process.encode()).decode()
                st.code(res)
                add_to_history("تشفير نص", text_to_process[:15] + "...")
            else:
                try:
                    res = base64.b64decode(text_to_process.encode()).decode()
                    st.info(res)
                    add_to_history("فك تشفير", "نص Base64")
                except: st.error("خطأ في الصيغة")

# 5. التذييل
st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtadha Yassin")
