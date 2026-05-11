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
    st.markdown("<h1 style='text-align: center; color: white;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("---")
except:
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)

# 3. إنشاء التبويبات (أضفنا تبويباً ثالثاً هنا)
tab1, tab2, tab3 = st.tabs(["🔍 فاحص الروابط", "🔑 مولد كلمات المرور", "🛡️ محلل أمان المواقع"])

# --- التبويب الأول: فحص الروابط ---
with tab1:
    st.header("Ali's URL Scanner")
    API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"
    url_input = st.text_input("أدخل الرابط للفحص:", key="url_scan")
    if st.button("بدء الفحص الأمني 🚀"):
        if url_input:
            headers = {"x-apikey": API_KEY}
            with st.spinner("جاري التحليل..."):
                url_id = base64.urlsafe_b64encode(url_input.encode()).decode().strip("=")
                response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)
                if response.status_code == 200:
                    stats = response.json()['data']['attributes']['last_analysis_stats']
                    st.metric("خبيث", stats['malicious'])
                    if stats['malicious'] > 0: st.error("⚠️ رابط خطر!")
                    else: st.success("✅ الرابط سليم.")
                else: st.info("يرجى الانتظار ثواني وإعادة المحاولة.")

# --- التبويب الثاني: مولد كلمات المرور ---
with tab2:
    st.header("Smart Password Generator")
    length = st.slider("طول الكلمة:", 8, 64, 16)
    use_symbols = st.checkbox("رموز", value=True)
    use_numbers = st.checkbox("أرقام", value=True)
    if st.button("توليد ✨"):
        chars = string.ascii_letters
        if use_numbers: chars += string.digits
        if use_symbols: chars += string.punctuation
        pwd = ''.join(random.choice(chars) for _ in range(length))
        st.code(pwd)
        if length >= 14:
            st.snow()
            st.toast("تصفيق حار! 👏")

# --- التبويب الثالث الجديد: محلل أمان المواقع (Security Headers) ---
with tab3:
    st.header("Website Security Analyzer")
    st.write("تفحص هذه الأداة بروتوكولات الحماية المشفرة للموقع (Security Headers).")
    
    target_url = st.text_input("أدخل رابط الموقع (مثال: https://google.com):", key="header_check")
    
    if st.button("تحليل جدار الحماية 🛡️"):
        if target_url:
            if not target_url.startswith("http"):
                target_url = "https://" + target_url
            
            try:
                with st.spinner("جاري فحص بروتوكولات الأمان..."):
                    response = requests.get(target_url, timeout=10)
                    headers = response.headers
                    
                    st.subheader("نتائج التحليل الفني:")
                    
                    # 1. فحص SSL/HTTPS
                    if target_url.startswith("https"):
                        st.success("🔒 اتصال مشفر (HTTPS): مفعل")
                    else:
                        st.warning("🔓 اتصال غير مشفر (HTTP): خطر")

                    # 2. فحص HSTS (حماية من الهجمات المتطورة)
                    if 'Strict-Transport-Security' in headers:
                        st.success("🛡️ بروتوكول HSTS: مفعل (حماية ممتازة)")
                    else:
                        st.error("❌ بروتوكول HSTS: غير مفعل (ثغرة محتملة)")

                    # 3. فحص X-Frame-Options (حماية من Clickjacking)
                    if 'X-Frame-Options' in headers:
                        st.success("🚫 حماية Clickjacking: مفعلة")
                    else:
                        st.info("ℹ️ حماية Clickjacking: غير موجودة")

                    st.info(f"الموقع يستخدم سيرفر من نوع: {headers.get('Server', 'غير معلن')}")
            
            except Exception as e:
                st.error(f"عذراً، تعذر الاتصال بالموقع. تأكد من الرابط.")
        else:
            st.warning("يرجى إدخال رابط.")

# 4. التذييل
st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtadha Yassin")
