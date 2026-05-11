import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات المتصفح
st.set_page_config(page_title="Ali Cyber Toolkit", page_icon="🛡️", layout="centered")

# 2. الهوية الشخصية (الاسم والصورة)
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("my_photo.jpg", width=200) 
    
    st.markdown(f"<h1 style='text-align: center; color: white;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("---")
except:
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)

# --- العبارة التي طلبتها (تمت إعادتها هنا) ---
st.markdown("<h2 style='text-align: center; color: #4682B4;'>🌐 مختبر علي المرتضى ياسين للأمن السيبراني</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>Powered by VirusTotal API & Advanced Security Protocols</p>", unsafe_allow_html=True)

# 3. إنشاء التبويبات الثلاثة
tab1, tab2, tab3 = st.tabs(["🔍 فاحص الروابط الذكي", "🔑 مولد كلمات المرور", "🛡️ محلل أمان المواقع"])

# --- التبويب الأول: فحص الروابط ---
with tab1:
    st.header("Ali's URL Scanner")
    API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"
    url_input = st.text_input("أدخل الرابط للفحص:", placeholder="https://example.com", key="scanner_input")
    
    if st.button("بدء الفحص 🚀", key="btn_scan"):
        if url_input:
            headers = {"x-apikey": API_KEY}
            with st.spinner("جاري التحليل..."):
                url_id = base64.urlsafe_b64encode(url_input.encode()).decode().strip("=")
                response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)
                if response.status_code == 200:
                    stats = response.json()['data']['attributes']['last_analysis_stats']
                    st.subheader("📊 النتيجة:")
                    c1, c2 = st.columns(2)
                    c1.metric("خبيث", stats['malicious'])
                    c2.metric("آمن", stats['harmless'])
                    if stats['malicious'] > 0: st.error("⚠️ رابط خطر!")
                    else: st.success("✅ الرابط آمن.")
                else: st.info("يرجى الانتظار ثواني وإعادة المحاولة.")

# --- التبويب الثاني: مولد كلمات المرور ---
with tab2:
    st.header("Smart Password Generator")
    length = st.slider("طول كلمة المرور:", 8, 64, 16)
    if st.button("توليد ✨", key="btn_gen"):
        chars = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(random.choice(chars) for _ in range(length))
        st.code(pwd)
        if length >= 14:
            st.snow()
            st.toast("كفووو يا بطل! 👏")

# --- التبويب الثالث: محلل أمان المواقع ---
with tab3:
    st.header("Website Security Analyzer")
    target_url = st.text_input("رابط الموقع للتحليل:", placeholder="https://google.com", key="analyzer_input")
    if st.button("تحليل جدار الحماية 🛡️", key="btn_analyze"):
        if target_url:
            if not target_url.startswith("http"): target_url = "https://" + target_url
            try:
                res = requests.get(target_url, timeout=10)
                h = res.headers
                st.subheader("📊 التحليل الفني:")
                if target_url.startswith("https"): st.success("🔒 HTTPS: مفعل")
                if 'Strict-Transport-Security' in h: st.success("🛡️ HSTS: مفعل")
                else: st.error("❌ HSTS: غير مفعل")
                st.info(f"نوع السيرفر: {h.get('Server', 'مخفي')}")
            except: st.error("تعذر الوصول للموقع.")

# 4. التذييل
st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtadha Yassin")
