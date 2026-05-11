import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات المتصفح والأيقونة 🛡️
st.set_page_config(page_title="Ali Cyber Toolkit", page_icon="🛡️", layout="wide")

# إدارة الذاكرة لسجل العمليات
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_history(action, detail):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.insert(0, f"[{timestamp}] {action}: {detail}")
    if len(st.session_state.history) > 10: st.session_state.history.pop()

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("📜 سجل العمليات | History")
    if st.session_state.history:
        for item in st.session_state.history:
            st.info(item)
        if st.button("مسح السجل | Clear 🗑️"):
            st.session_state.history = []
            st.rerun()
    else:
        st.write("لا توجد عمليات مسجلة.")
    st.markdown("---")
    st.caption("Developed by Ali Al-Murtada")

# 3. الهوية البصرية (الاسم والمسمى بالإنجليزية كما طلبت)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # تأكد من وجود الصورة بنفس المجلد بهذا الاسم
        st.image("my_photo.jpg", width=200) 
    except: pass
    
    # الاسم بالإنجليزية فقط
    st.markdown(f"<h1 style='text-align: center; color: white; margin-bottom: 0;'>Ali Al-Murtada</h1>", unsafe_allow_html=True)
    
    # المسمى الوظيفي مع المسافة (Cyber Security)
    st.markdown("<p style='text-align: center; color: #FF4B4B; font-size: 24px; font-weight: bold; margin-top: 0;'>Cyber Security Engineer</p>", unsafe_allow_html=True)
    
    # العنوان الفرعي
    st.markdown("<h4 style='text-align: center; color: #4682B4;'>🌐 (Lab) Ali Al-Murtada Yassin</h4>", unsafe_allow_html=True)

# 4. التبويبات ثنائية اللغة (العربية والإنجليزية معا) 🌍
tabs = st.tabs([
    "🔍 فحص الروابط | URL Scanner", 
    "🔑 كلمات المرور | Passwords", 
    "🛡️ محلل الأمان | Analyzer", 
    "🔐 التشفير | Encryption", 
    "🌍 فحص الـ IP | IP Lookup"
])

# --- التبويب الأول: فاحص الروابط ---
with tabs[0]:
    st.header("URL Security Scanner")
    u = st.text_input("أدخل الرابط للفحص | Enter URL:", key="u_scan")
    if st.button("فحص | Scan 🚀"):
        if u:
            add_to_history("Scan URL", u)
            st.success("جاري الاتصال بقواعد البيانات... | Connecting to DB...")

# --- التبويب الثاني: مولد كلمات المرور ---
with tabs[1]:
    st.header("Password Generator")
    l = st.slider("الطول | Length:", 8, 32, 16)
    if st.button("توليد | Generate ✨"):
        res = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(l))
        st.code(res)
        add_to_history("Gen Password", f"Length {l}")

# --- التبويب الثالث: محلل الأمان ---
with tabs[2]:
    st.header("Security Analyzer")
    s = st.text_input("رابط الموقع | Website URL:", key="s_anal")
    if st.button("تحليل الأمان | Analyze 🛡️"):
        if s:
            add_to_history("Analyze Site", s)
            st.info(f"جاري فحص بروتوكولات الحماية لـ {s}...")

# --- التبويب الرابع: نظام التشفير ---
with tabs[4-1]: # Encryption
    st.header("Encryption System")
    mode = st.radio("العملية | Operation:", ["تشفير | Encode", "فك تشفير | Decode"], horizontal=True)
    txt = st.text_area("النص | Input Text:", height=100, key="enc_txt")
    if st.button("تنفيذ | Execute ⚡"):
        if txt:
            if "تشفير" in mode:
                res = base64.b64encode(txt.encode()).decode()
                st.code(res)
                add_to_history("Encryption", txt[:10])
            else:
                try:
                    res = base64.b64decode(txt.encode()).decode()
                    st.success(res)
                    add_to_history("Decryption", "Base64")
                except: st.error("خطأ في الصيغة | Invalid Format")

# --- التبويب الخامس: فحص الـ IP المطور ---
with tabs[4]:
    st.header("Advanced IP Geolocation")
    ip = st.text_input("IP Address (Public/Local):", placeholder="8.8.8.8 or 10.0.2.15")
    
    if st.button("بدء الكشف | Start Lookup 🔍"):
        if ip:
            # قائمة الشبكات المحلية
            private_prefixes = ["10.", "192.168.", "172.16.", "127.0.0.1"]
            
            if any(ip.startswith(prefix) for prefix in private_prefixes):
                st.warning(f"⚠️ عنوان محلي مكتشف | Local IP Detected: {ip}")
                st.info("""
                **تحليل علي المرتضى | Analysis:**
                هذا العنوان محلي ولا يظهر على الخريطة العالمية.
                This is a Private IP, used for internal networks only.
                """)
                add_to_history("Local IP Check", ip)
            else:
                try:
                    with st.spinner("جاري جلب البيانات..."):
                        r = requests.get(f"http://ip-api.com/json/{ip}").json()
                        if r.get('status') == 'success':
                            add_to_history("Public IP Map", ip)
                            st.success(f"📍 الموقع | Location: {r.get('city')}, {r.get('country')}")
                            st.map(data={"lat": [r.get('lat')], "lon": [r.get('lon')]})
                        else:
                            st.error("عنوان غير صحيح | Invalid Public IP")
                except:
                    st.error("خطأ في الاتصال | Connection Error")

st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtada | Cyber Security Student")
