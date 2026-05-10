import streamlit as st
import requests
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Ali Cyber Guard", page_icon="🛡️")

st.title("🛡️ Ali's Advanced URL Scanner")
st.markdown("### Powered by VirusTotal API | Cybersecurity Project")

# المفتاح الخاص بك الذي أرسلته
API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"

# 2. واجهة المستخدم
url_to_scan = st.text_input("إدخال الرابط المراد فحصه (مثال: http://example.com):")

if st.button("بدء الفحص السريع 🔍"):
    if url_to_scan:
        headers = {
            "x-apikey": API_KEY
        }
        
        with st.spinner("جاري الاتصال بمحركات الفحص العالمية..."):
            # إرسال الرابط للفحص
            api_url = "https://www.virustotal.com/api/v3/urls"
            data = {"url": url_to_scan}
            response = requests.post(api_url, data=data, headers=headers)
            
            if response.status_code == 200:
                analysis_id = response.json()['data']['id']
                
                # الانتظار قليلاً لتحليل النتائج
                st.info("تم إرسال الرابط بنجاح، جاري استخراج تقرير الأمان...")
                time.sleep(3) 
                
                # جلب نتائج التحليل
                report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
                report_response = requests.get(report_url, headers=headers)
                
                if report_response.status_code == 200:
                    stats = report_response.json()['data']['attributes']['stats']
                    
                    # 3. عرض النتائج بشكل احترافي
                    col1, col2, col3 = st.columns(3)
                    col1.metric("خبيث (Malicious)", stats['malicious'])
                    col2.metric("مشبوه (Suspicious)", stats['suspicious'])
                    col3.metric("آمن (Harmless)", stats['harmless'])
                    
                    if stats['malicious'] > 0:
                        st.error(f"⚠️ تحذير: هذا الرابط تم تصنيفه كخطر من قبل {stats['malicious']} محرك فحص!")
                    else:
                        st.success("✅ هذا الرابط يبدو آمناً للاستخدام بناءً على قواعد البيانات الحالية.")
            else:
                st.error("حدث خطأ في الاتصال. تأكد من صحة الرابط أو المفتاح.")
    else:
        st.warning("الرجاء إدخال رابط أولاً.")

st.markdown("---")
st.caption("Developed by Ali Al-Murtadha - Cyber Security Engineering Student")
