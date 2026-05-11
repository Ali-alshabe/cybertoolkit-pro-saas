import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات المتصفح (التي تظهر في التبويب العلوي)
st.set_page_config(page_title="Ali Cyber Toolkit", page_icon="🛡️", layout="centered")

# 2. الهوية الشخصية (الاسم والصورة في المنتصف)
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # تأكد من أن اسم ملف الصورة في GitHub هو my_photo.jpg
        st.image("my_photo.jpg", width=200) 
    
    st.markdown("<h1 style='text-align: center; color: white;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("---")
except:
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)

# 3. إنشاء التبويبات (Tabs) لتنظيم الأدوات
tab1, tab2 = st.tabs(["🔍 فاحص الروابط الذكي", "🔑 مولد كلمات المرور المطور"])

# --- التبويب الأول: فحص الروابط (نفس الكود السابق مع تحسينات) ---
with tab1:
    st.header("Ali's Advanced URL Scanner")
    st.write("أداة مدعومة بـ VirusTotal لفحص الروابط المشبوهة.")
    
    API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"
    url_input = st.text_input("أدخل الرابط المراد فحصه هنا:", placeholder="https://example.com")
    
    if st.button("بدء الفحص الأمني 🚀"):
        if url_input:
            headers = {"x-apikey": API_KEY}
            with st.spinner("جاري التحليل السيبراني..."):
                # تحويل الرابط إلى Base64 كما تطلب API الخاص بـ VirusTotal
                url_id = base64.urlsafe_b64encode(url_input.encode()).decode().strip("=")
                report_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
                response = requests.get(report_url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()['data']['attributes']
                    stats = data['last_analysis_stats']
                    
                    st.subheader("📊 نتائج الفحص:")
                    c1, c2, c3 = st.columns(3)
                    c1.metric("خبيث", stats['malicious'], delta_color="inverse")
                    c2.metric("مشبوه", stats['suspicious'], delta_color="off")
                    c3.metric("آمن", stats['harmless'])
                    
                    if stats['malicious'] > 0:
                        st.error(f"⚠️ تحذير أمني: هذا الرابط تم تصنيفه كتهديد من قبل {stats['malicious']} محرك فحص!")
                    else:
                        st.success("✅ الرابط يبدو آمناً للاستخدام بناءً على قواعد البيانات الحالية.")
                else:
                    st.info("الرابط جديد على النظام، جاري إرساله للفحص لأول مرة...")
                    requests.post("https://www.virustotal.com/api/v3/urls", data={"url": url_input}, headers=headers)
                    st.warning("تم إرسال الطلب، يرجى إعادة الضغط على الفحص بعد 30 ثانية.")
        else:
            st.warning("الرجاء إدخال رابط أولاً.")

# --- التبويب الثاني المطور: مولد كلمات المرور مع عداد القوة ---
with tab2:
    st.header("Smart Password Generator")
    st.write("قم بتوليد كلمات مرور قوية وتحليل مستوى أمانها ضد هجمات Brute Force.")
    
    # خيارات المستخدم
    length = st.slider("طول كلمة المرور:", min_value=8, max_value=64, value=16)
    use_symbols = st.checkbox("إضافة رموز خاصة (!@#$%^&*)", value=True)
    use_numbers = st.checkbox("إضافة أرقام (123456)", value=True)
    
    if st.button("توليد كلمة مرور ✨"):
        # بناء مجموعة الأحرف بناءً على الاختيارات
        chars = string.ascii_letters
        if use_numbers: chars += string.digits
        if use_symbols: chars += string.punctuation
        
        # التوليد العشوائي
        password = ''.join(random.choice(chars) for i in range(length))
        
        st.success("تم التوليد بنجاح (يمكنك النسخ من المربع أدناه):")
        st.code(password) # مربع قابل للنسخ بضغطة زر
        
        # --- تحليل مستوى الأمان (المرحلة 3) ---
        st.markdown("### 🛡️ تحليل قوة الأمان:")
        
        if length < 10:
            st.error("المستوى: ضعيف جداً ❌ (يمكن كسرها في ثوانٍ)")
        elif 10 <= length < 14:
            st.warning("المستوى: متوسط ⚠️ (جيدة للاستخدام العادي)")
       elif length >= 14 and (use_symbols or use_numbers):
            st.success("المستوى: خارق 💪")
            # تصفيق متتالي في الزاوية
            st.toast("كفووو! 👏")
            time.sleep(0.5)
            st.toast("أمن ممتاز! 👏👏")
            time.sleep(0.5)
            st.toast("عاشت إيدك يا بطل! 👏👏👏")
        else:
            st.info("المستوى: جيد، لكن زد الرموز لزيادة الأمان.")

# 4. التذييل (Footer)
st.markdown("---")
st.caption(f"© {time.strftime('%Y')} Developed by Ali Al-Murtadha Yassin | Cybersecurity Student")
