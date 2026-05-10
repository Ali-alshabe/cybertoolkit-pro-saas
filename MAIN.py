import streamlit as st
import requests
import time
import base64

# 1. إعدادات الصفحة والواجهة
st.set_page_config(page_title="Ali Cyber Guard Pro", page_icon="🛡️")

st.title("🛡️ Ali's Advanced URL Scanner")
st.markdown("### Powered by VirusTotal API | Cybersecurity Project v2.0")

# مفتاح الـ API الخاص بك
API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"

# 2. مدخلات المستخدم
url_to_scan = st.text_input("أدخل الرابط المراد فحصه هنا:")

if st.button("بدء الفحص الأمني 🔍"):
    if url_to_scan:
        headers = {
            "x-apikey": API_KEY
        }
        
        with st.spinner("جاري إرسال الرابط وتحليله في قواعد البيانات العالمية..."):
            # الخطوة الأولى: تشفير الرابط بصيغة Base64 لجلب التقرير التاريخي (أكثر دقة)
            url_id = base64.urlsafe_b64encode(url_to_scan.encode()).decode().strip("=")
            report_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
            
            # محاولة جلب تقرير موجود مسبقاً
            response = requests.get(report_url, headers=headers)
            
            # إذا لم يكن الرابط مفحوصاً من قبل، نقوم بطلبه الآن
            if response.status_code != 200:
                st.info("رابط جديد! جاري الفحص لأول مرة...")
                post_url = "https://www.virustotal.com/api/v3/urls"
                requests.post(post_url, data={"url": url_to_scan}, headers=headers)
                time.sleep(10) # انتظار أطول للفحص الجديد
                response = requests.get(report_url, headers=headers)

            if response.status_code == 200:
                # استخراج البيانات
                data = response.json()['data']['attributes']
                stats = data['last_analysis_stats']
                
                # 3. عرض النتائج بشكل احترافي
                st.subheader("📊 تقرير فحص الأمان:")
                col1, col2, col3, col4 = st.columns(4)
                
                col1.metric("خبيث", stats['malicious'], delta_color="inverse")
                col2.metric("مشبوه", stats['suspicious'])
                col3.metric("آمن", stats['harmless'])
                col4.metric("غير مكتشف", stats['undetected'])
                
                st.markdown("---")
                
                if stats['malicious'] > 0:
                    st.error(f"⚠️ تحذير أمني: هذا الرابط تم تصنيفه كتهديد من قبل {stats['malicious']} محرك فحص!")
                    st.warning("ينصح بعدم الدخول إلى هذا الرابط أو إدخال أي بيانات شخصية فيه.")
                elif stats['suspicious'] > 0:
                    st.warning("🛡️ الرابط مشبوه: بعض المحركات تشير إلى وجود نشاط غير طبيعي.")
                else:
                    st.success("✅ الرابط سليم: لم يتم العثور على تهديدات نشطة في قواعد البيانات.")
                    
                # عرض تفاصيل إضافية لمحبي الأمن السيبراني
                with st.expander("تفاصيل تقنية إضافية"):
                    st.write(f"**العنوان النهائي:** {data.get('last_final_url', url_to_scan)}")
                    st.write(f"**تاريخ آخر فحص:** {time.ctime(data['last_analysis_date'])}")
            else:
                st.error("❌ فشل النظام في جلب البيانات. تأكد من أن الرابط صحيح.")
    else:
        st.warning("الرجاء إدخال رابط أولاً.")

# تذييل الصفحة
st.markdown("---")
st.caption("Developed by Ali Al-Murtadha - Cyber Security Student | 2026")
