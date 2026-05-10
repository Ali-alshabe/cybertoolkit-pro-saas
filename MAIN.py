import streamlit as st
import requests
import time
import base64
from PIL import Image

# 1. إعدادات الصفحة
st.set_page_config(page_title="Ali Al-Murtadha Lab", page_icon="🛡️")

# 2. إضافة الصورة والاسم الشخصي في البداية
# ملاحظة: تأكد من رفع ملف الصورة إلى GitHub بنفس الاسم المذكور أدناه
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2: # وضع الصورة في العمود الأوسط لتكون في المنتصف
        st.image("my_photo.jpg", width=200, caption="") 
    
    st.markdown(f"""
        <h1 style='text-align: center;'>علي المرتضى ياسين</h1>
        <h3 style='text-align: center; color: #4682B4;'>مهندس أمن سيبراني واعد</h3>
        <hr>
    """, unsafe_allow_html=True)
except:
    # في حال لم ترفع الصورة بعد، سيظهر الاسم فقط لتجنب الخطأ
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.info("نصيحة: ارفع صورتك باسم 'my_photo.jpg' لتظهر هنا!")

st.title("🌐 مختبر علي المرتضى ياسين لفحص الراوبط")
st.markdown("### Powered by VirusTotal API | v2.0")

# --- بقية كود الفحص ---
API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"

url_to_scan = st.text_input("أدخل الرابط المراد فحصه هنا:")

if st.button("بدء الفحص الأمني 🔍"):
    if url_to_scan:
        headers = {"x-apikey": API_KEY}
        with st.spinner("جاري التحليل..."):
            url_id = base64.urlsafe_b64encode(url_to_scan.encode()).decode().strip("=")
            report_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
            response = requests.get(report_url, headers=headers)
            
            if response.status_code != 200:
                requests.post("https://www.virustotal.com/api/v3/urls", data={"url": url_to_scan}, headers=headers)
                time.sleep(10)
                response = requests.get(report_url, headers=headers)

            if response.status_code == 200:
                data = response.json()['data']['attributes']
                stats = data['last_analysis_stats']
                
                st.subheader("📊 تقرير فحص الأمان:")
                c1, c2, c3 = st.columns(3)
                c1.metric("خبيث", stats['malicious'])
                c2.metric("مشبوه", stats['suspicious'])
                c3.metric("آمن", stats['harmless'])
                
                if stats['malicious'] > 0:
                    st.error(f"⚠️ تحذير: الرابط خطر!")
                else:
                    st.success("✅ الرابط سليم.")
            else:
                st.error("فشل جلب البيانات.")
    else:
        st.warning("الرجاء إدخال رابط.")

st.markdown("---")
st.caption("© 2026 Developed by Ali Al-Murtadha Yassin")
