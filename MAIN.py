import streamlit as st
import hashlib
import re
from datetime import datetime

# إعدادات الواجهة
st.set_page_config(page_title="CyberToolkit Pro", page_icon="🛡️")

st.title("🛡️ Global Cyber Security Toolkit")
st.write("SaaS Project v1.2 | Developed by Ali Al-Murtadha")


# دالة فحص قوة كلمة المرور
def check_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password): score += 1
    if re.search("[0-9]", password): score += 1
    if re.search("[!@#$%^&*]", password): score += 1
    return score


# واجهة المستخدم
user_input = st.text_input("Enter password to analyze & encrypt:", type="password")

if user_input:
    # 1. تحليل القوة
    strength_score = check_password_strength(user_input)

    st.subheader("1. Security Analysis")
    status = ""
    if strength_score == 4:
        st.success("💪 Strong Password")
        status = "Strong"
    elif strength_score >= 2:
        st.warning("⚠️ Medium Password")
        status = "Medium"
    else:
        st.error("🚨 Weak Password")
        status = "Weak"

    # 2. التشفير
    st.subheader("2. Encryption (SHA-256)")
    hashed_result = hashlib.sha256(user_input.encode()).hexdigest()
    st.code(hashed_result, language='text')

    # 3. حفظ السجل (Logging) - الجزء الجديد
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{now}] Status: {status} | Hash: {hashed_result[:10]}...\n"

    with open("activity_log.txt", "a") as f:
        f.write(log_entry)

# عرض السجل في الشريط الجانبي
st.sidebar.header("📜 Activity History")
if st.sidebar.button("Show Recent Logs"):
    try:
        with open("activity_log.txt", "r") as f:
            logs = f.readlines()
            for log in logs[-5:]:  # عرض آخر 5 عمليات فقط
                st.sidebar.text(log)
    except FileNotFoundError:
        st.sidebar.write("No logs yet.")