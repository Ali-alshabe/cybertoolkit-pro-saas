import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات الصفحة
st.set_page_config(page_title="Ali Cyber Toolkit", page_icon="🛡️")

# 2. الهوية الشخصية (الاسم والصورة)
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("my_photo.jpg", width=200) 
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("---")
except:
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)

# 3. إنشاء التبويبات (Tabs)
tab1, tab2 = st.tabs(["🔍 فاحص الروابط", "🔑 مولد كلمات المرور"])

# --- التبويب الأول: فحص الروابط ---
with tab1:
    st.title("Ali's URL Scanner")
    API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"
    url_input = st.text_input("أدخل الرابط للفحص:")
    
    if st.button("بدء الفحص 🔍"):
        if url_input:
            headers = {"x-apikey": API_KEY}
            with st.spinner("جاري التحليل..."):
                url_id = base64.urlsafe_b64encode(url_input.encode()).decode().strip("=")
                report_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
                response = requests.get(report_url, headers=headers)
                
                if response.status_code == 200:
                    stats = response.json()['data']['attributes']['last_analysis_stats']
                    st.metric("خبيث (Malicious)", stats['malicious'])
                    if stats['malicious'] > 0:
                        st.error("⚠️ هذا الرابط خطر!")
                    else:
                        st.success("✅ الرابط يبدو آمناً.")
                else:
                    st.info("رابط جديد، جاري الطلب...")
                    requests.post("https://www.virustotal.com/api/v3/urls", data={"url": url_input}, headers=headers)
                    st.warning("يرجى المحاولة بعد قليل لاكتمال الفحص.")

# --- التبويب الثاني: مولد كلمات المرور ---
with tab2:
    st.title("🔑 Password Generator")
    st.write("قم بتوليد كلمات مرور قوية ومستحيلة الاختراق.")
    
    length = st.slider("طول كلمة المرور:", min_value=8, max_value=32, value=16)
    use_symbols = st.checkbox("إضافة رموز خاصة (!@#$%^&*)", value=True)
    use_numbers = st.checkbox("إضافة أرقام (123456)", value=True)
    
    if st.button("توليد كلمة مرور ✨"):
        chars = string.ascii_letters
        if use_numbers: chars += string.digits
        if use_symbols: chars += string.punctuation
        
        password = ''.join(random.choice(chars) for i in range(length))
        
        st.success("تم توليد كلمة المرور بنجاح:")
        st.code(password) # عرضها في مربع قابل للنسخ
        
        # تقييم قوة كلمة المرور
        if length >= 12 and use_symbols and use_numbers:
            st.info("💪 تقييم القوة: مستحيلة الاختراق (Strong)")
        else:
            st.warning("💡 نصيحة: زد الطول وأضف رموزاً لزيادة الأمان.")

# التذييل
st.markdown("---")
st.caption("© 2026 Developed by Ali Al-Murtadha Yassin")
