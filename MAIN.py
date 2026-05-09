import streamlit as st
import hashlib
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="CyberToolkit Pro", page_icon="🛡️")

# الهوية البصرية والاسم
st.title("🛡️ Global Cyber Security Toolkit")
st.markdown("### SaaS Project v1.2 | Developed by Ali Al-Murtadha")

# التأكد من وجود سجل في الذاكرة
if 'logs' not in st.session_state:
    st.session_state.logs = []

# خانة الإدخال
password = st.text_input("Enter password to analyze & encrypt:", type="password")

if password:
    # 1. تحليل القوة (بسيط)
    st.markdown("### 1. Security Analysis")
    if len(password) < 8:
        st.error("🚨 Weak Password (Too short)")
    else:
        st.success("✅ Strong Password")

    # 2. التشفير باستخدام SHA-256
    st.markdown("### 2. Encryption (SHA-256)")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    st.code(hashed_password)

    # حفظ العملية في السجل (تعديل: إظهار الكلمة الأصلية)
    now = datetime.now().strftime("%H:%M:%S")
    log_entry = f"[{now}] Input: '{password}' | Hash: {hashed_password[:15]}..."
    
    # إضافة السجل إذا لم يكن مضافاً مسبقاً لمنع التكرار عند إعادة التحميل
    if not st.session_state.logs or st.session_state.logs[-1] != log_entry:
        st.session_state.logs.append(log_entry)

# القائمة الجانبية للسجلات
with st.sidebar:
    st.title("📑 Activity History")
    if st.button("Show Recent Logs"):
        if st.session_state.logs:
            for log in reversed(st.session_state.logs):
                st.write(log)
        else:
            st.info("No activity recorded yet.")

# تذييل الصفحة
st.divider()
st.caption("Secure Encryption Tool - Academic Purpose 2026")
