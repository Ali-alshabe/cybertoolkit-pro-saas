import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات المتصفح - (هنا غيرنا الأيقونة لتصبح درع 🛡️)
st.set_page_config(
    page_title="Ali Cyber Toolkit", 
    page_icon="🛡️", 
    layout="wide"
)

# --- إدارة الذاكرة (Session State) ---
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_history(action, detail):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.insert(0, f"[{timestamp}] {action}: {detail}")
    if len(st.session_state.history) > 10:
        st.session_state.history.pop()

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("📜 سجل العمليات")
    if st.session_state.history:
        for item in st.session_state.history:
            st.info(item)
        if st.button("مسح السجل 🗑️"):
            st.session_state.history = []
            st.rerun()
    else:
        st.write("لا توجد عمليات مسجلة.")
    st.markdown("---")
    st.caption("© 2026 Ali Al-Murtadha")

# 3. الهوية الشخصية
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("my_photo.jpg", width=200) 
    except: pass
    st.markdown(f"<h1 style='text-align: center; color: white; margin-bottom: 0;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF4B4B; font-size: 22px; font-weight: bold; margin-top: 0;'>Cybersecurity Engineer</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4682B4;'>🌐 (Lab) Ali Al-Murtada Yassin</h3>", unsafe_allow_html=True)

# 4. التبويبات (أضفنا تبويب فحص الـ IP)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 فاحص الروابط", 
    "🔑 مولد الكلمات", 
    "🛡️ محلل الأمان", 
    "🔐 نظام التشفير",
    "🌍 فحص الـ IP"
])

# --- التبويبات السابقة (تعمل كالمعتاد) ---
with tab1:
    st.header("URL Scanner")
    url_input = st.text_input("أدخل الرابط:", key="u1")
    if st.button("فحص 🚀"):
        add_to_history("فحص رابط", url_input)
        st.success("تم بدء الفحص..")

with tab2:
    st.header("Password Gen")
    length = st.slider("الطول:", 8, 32, 16)
    if st.button("توليد ✨"):
        p = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        st.code(p)
        add_to_history("توليد كلمة", f"بطول {length}")

with tab3:
    st.header("Security Analyzer")
    site = st.text_input("رابط الموقع:", key="s1")
    if st.button("تحليل 🛡️"):
        add_to_history("تحليل موقع", site)
        st.info("جاري فحص الـ Headers...")

with tab4:
    st.header("Encryption")
    text = st.text_area("النص:", key="t1")
    if st.button("تشفير ⚡"):
        res = base64.b64encode(text.encode()).decode()
        st.code(res)
        add_to_history("تشفير نص", text[:10]+"...")

# --- التبويب الخامس الجديد: فحص الـ IP ---
with tab5:
    st.header("IP Geolocation & Security")
    st.write("أدخل عنوان IP لمعرفة موقعه الجغرافي ومعلومات الشبكة.")
    ip_input = st.text_input("أدخل عنوان الـ IP (مثال: 8.8.8.8):", placeholder="8.8.8.8")
    
    if st.button("كشف المعلومات 🔍"):
        if ip_input:
            try:
                with st.spinner("جاري جلب البيانات..."):
                    # استخدام API مجاني لجلب معلومات الـ IP
                    response = requests.get(f"https://ipapi.co/{ip_input}/json/").json()
                    
                    if "error" not in response:
                        add_to_history("فحص IP", ip_input)
                        c1, c2, c3 = st.columns(3)
                        c1.metric("الدولة", response.get("country_name"))
                        c2.metric("المدينة", response.get("city"))
                        c3.metric("المزود (ISP)", response.get("org"))
                        
                        st.map(data={"lat": [response.get("latitude")], "lon": [response.get("longitude")]})
                        st.success(f"تم تحديد موقع السيرفر بنجاح في {response.get('country_name')}")
                    else:
                        st.error("عنوان IP غير صحيح أو غير موجود.")
            except:
                st.error("تعذر الاتصال بقاعدة بيانات الـ IP.")

# 5. التذييل
st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtadha Yassin | Cybersecurity Lab")
