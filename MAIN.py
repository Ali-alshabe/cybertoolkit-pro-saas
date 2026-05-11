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
        # تأكد أن اسم الملف في GitHub هو my_photo.jpg وليس my_photo.jpg.jpeg
        st.image("my_photo.jpg", width=200) 
    
    st.markdown(f"<h1 style='text-align: center; color: white;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("---")
except:
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)

# 3. إنشاء التبويبات الثلاثة (لضمان بقاء كل الأدوات)
tab1, tab2, tab3 = st.tabs(["🔍 فاحص الروابط الذكي", "🔑 مولد كلمات المرور", "🛡️ محلل أمان المواقع"])

# --- التبويب الأول: فحص الروابط (يبقى كما هو) ---
with tab1:
    st.header("Ali's URL Scanner")
    st.write("أداة فحص الروابط المشبوهة عبر VirusTotal.")
    
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
                    
                    if stats['malicious'] > 0:
                        st.error("⚠️ هذا الرابط خطر!")
                    else:
                        st.success("✅ الرابط يبدو آمناً.")
                else:
                    st.info("الرابط جديد، جاري الطلب... أعد المحاولة بعد ثوانٍ.")

# --- التبويب الثاني: مولد كلمات المرور (يبقى كما هو) ---
with tab2:
    st.header("Smart Password Generator")
    length = st.slider("طول كلمة المرور:", 8, 64, 16)
    use_symbols = st.checkbox("إضافة رموز", value=True)
    use_numbers = st.checkbox("إضافة أرقام", value=True)
    
    if st.button("توليد كلمة المرور ✨", key="btn_gen"):
        chars = string.ascii_letters
        if use_numbers: chars += string.digits
        if use_symbols: chars += string.punctuation
        
        pwd = ''.join(random.choice(chars) for _ in range(length))
        st.code(pwd)
        
        if length >= 14:
            st.snow()
            st.toast("عاشت إيدك! 👏")

# --- التبويب الثالث: محلل أمان المواقع (الإضافة الجديدة) ---
with tab3:
    st.header("Website Security Analyzer")
    st.write("تحليل بروتوكولات الحماية الفنية (Security Headers).")
    
    target_url = st.text_input("رابط الموقع للتحليل:", placeholder="https://google.com", key="analyzer_input")
    
    if st.button("تحليل جدار الحماية 🛡️", key="btn_analyze"):
        if target_url:
            if not target_url.startswith("http"):
                target_url = "https://" + target_url
            
            try:
                with st.spinner("جاري الفحص..."):
                    res = requests.get(target_url, timeout=10)
                    h = res.headers
                    
                    st.subheader("📊 التحليل الفني:")
                    
                    # فحص HTTPS
                    if target_url.startswith("https"):
                        st.success("🔒 اتصال مشفر (HTTPS): مفعل")
                    else:
                        st.warning("🔓 اتصال غير مشفر (HTTP): خطر")

                    # فحص HSTS
                    if 'Strict-Transport-Security' in h:
                        st.success("🛡️ بروتوكول HSTS: مفعل")
                    else:
                        st.error("❌ بروتوكول HSTS: غير مفعل (ثغرة محتملة)")

                    # فحص الحماية من Clickjacking
                    if 'X-Frame-Options' in h:
                        st.success("🚫 حماية Clickjacking: مفعلة")
                    else:
                        st.info("ℹ️ حماية Clickjacking: غير موجودة")
                    
                    st.info(f"نوع السيرفر المكتشف: {h.get('Server', 'مخفي')}")
            except:
                st.error("تعذر الوصول للموقع.")

# التذييل
st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtadha Yassin")
