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

# 2. القائمة الجانبية
with st.sidebar:
    st.title("📜 Action History")
    if st.session_state.history:
        for item in st.session_state.history:
            st.info(item)
        if st.button("Clear History 🗑️"):
            st.session_state.history = []
            st.rerun()
    else:
        st.write("No activities yet.")
    st.markdown("---")
    st.caption("Developed by Ali Al-Murtada")

# 3. الهوية البصرية
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("my_photo.jpg", width=200) 
    except: pass
    st.markdown(f"<h1 style='text-align: center; color: white; margin-bottom: 0;'>Ali Al-Murtada</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FF4B4B; font-size: 24px; font-weight: bold; margin-top: 0;'>Cyber Security Engineer</p>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #4682B4;'>🌐 (Lab) Ali Al-Murtada Yassin</h4>", unsafe_allow_html=True)

# 4. التبويبات
tabs = st.tabs(["🔍 URL Scanner", "🔑 Passwords", "🛡️ Analyzer", "🔐 Encryption", "🌍 IP Lookup"])

# --- التبويبات 1-4 (مختصرة للعمل) ---
with tabs[0]:
    u = st.text_input("Enter URL:", key="u_scan")
    if st.button("Scan 🚀"):
        add_to_history("Scan URL", u); st.success("Scanning...")

with tabs[1]:
    l = st.slider("Length:", 8, 32, 16)
    if st.button("Generate ✨"):
        res = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l))
        st.code(res); add_to_history("Gen Pass", f"Len {l}")

with tabs[2]:
    s = st.text_input("Website:", key="s_anal")
    if st.button("Analyze 🛡️"):
        add_to_history("Analyze", s); st.info("Analyzing...")

with tabs[3]:
    mode = st.radio("Mode:", ["Encode", "Decode"], horizontal=True)
    txt = st.text_area("Text:", key="enc_txt")
    if st.button("Execute ⚡"):
        if mode == "Encode":
            res = base64.b64encode(txt.encode()).decode()
            st.code(res); add_to_history("Enc", txt[:10])
        else:
            try:
                res = base64.b64decode(txt.encode()).decode()
                st.success(res); add_to_history("Dec", "Base64")
            except: st.error("Error")

# --- التبويب الخامس: فحص الـ IP المتطور ---
with tabs[4]:
    st.header("Advanced IP Geolocation")
    ip = st.text_input("Enter IP Address (Public or Local):", placeholder="e.g. 8.8.8.8 or 10.0.2.15")
    
    if st.button("Start Lookup 🔍"):
        if ip:
            # التحقق من العناوين المحلية (Private/Local IPs)
            private_ips = ["10.", "192.168.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.31.", "127.0.0.1"]
            
            if any(ip.startswith(prefix) for prefix in private_ips):
                st.warning(f"⚠️ Local/Private IP Detected: {ip}")
                st.info("""
                **Analysis for Ali Al-Murtada:**
                This is a **Private IP Address**. It is used only within your internal network (like a Virtual Machine or Home WiFi).
                - **Location:** Invisible to the public internet.
                - **Status:** Secure/Internal.
                - **Note:** It cannot be mapped globally because it doesn't leave your local router.
                """)
                add_to_history("Check Local IP", ip)
            else:
                # محاولة فحص العناوين العامة (Public IPs)
                try:
                    with st.spinner("Searching global databases..."):
                        r = requests.get(f"http://ip-api.com/json/{ip}").json()
                        if r.get('status') == 'success':
                            st.success(f"🌐 Public IP Located!")
                            add_to_history("Public IP Map", ip)
                            
                            c1, c2, c3 = st.columns(3)
                            c1.metric("Country", r.get('country'))
                            c2.metric("City", r.get('city'))
                            c3.metric("ISP", r.get('isp'))
                            
                            st.map(data={"lat": [r.get('lat')], "lon": [r.get('lon')]})
                        else:
                            st.error("Invalid IP: This address does not exist on the public internet.")
                except:
                    st.error("Connection Error: API server is busy.")

st.markdown("---")
st.caption(f"© 2026 Developed by Ali Al-Murtada | Cyber Security Student")
