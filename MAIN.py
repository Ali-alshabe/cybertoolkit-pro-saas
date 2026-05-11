import streamlit as st
import requests
import time
import base64
import random
import string

# 1. إعدادات المتصفح
st.set_page_config(page_title="Ali Cyber Toolkit", page_icon="🛡️", layout="centered")

# 2. الهوية الشخصية (الاسم والصورة)
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("my_photo.jpg", width=200) 
    
    st.markdown("<h1 style='text-align: center; color: white;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)
    st.markdown("---")
except:
    st.markdown("<h1 style='text-align: center;'>علي المرتضى ياسين</h1>", unsafe_allow_html=True)

# 3. إنشاء التبويبات (Tabs)
tab1, tab2 = st.tabs(["🔍 فاحص الروابط الذكي", "🔑 مولد كلمات المرور المطور"])

# --- التبويب الأول: فحص الروابط ---
with tab1:
    st.header("Ali's Advanced URL Scanner")
    st.write("أداة مدعومة بـ VirusTotal لفحص الروابط المشبوهة.")
    
    API_KEY = "05013f6fce2851d186d9f46955283590aa8122de0521257fb26f5099797aeabc"
    url_input = st.text_input("أدخل الرابط المراد فحصه هنا:", placeholder="https://example.com")
    
    if st.button("بدء الفحص الأمني 🚀"):
        if url_input:
            headers = {"x-apikey": API_KEY}
            with st.spinner("جاري التحليل السيبراني..."):
                url_id = base64.urlsafe_b64encode(url_input.encode()).decode().strip("=")
                report_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
                response = requests.get(report_url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()['data']['attributes']
                    stats = data['last_analysis_stats']
                    
                    st.subheader("📊 نتائج الفحص:")
                    c1, c2, c3 = st.columns(3)
                    c1.metric("خبيث", stats['malicious'], delta_color="inverse")
                    c2.metric("ممشبه", stats['suspicious'], delta_color="off")
                    c3.metric("آمن", stats['harmless'])
                    
                    if stats['malicious'] > 0:
                        st.error(f"⚠️ تحذير أمني: هذا الرابط تم تصنيفه كتهديد!")
                    else:
                        st.success("✅ الرابط يبدو آمناً للاستخدام.")
                else:
                    st.info("الرابط جديد، جاري إرساله للفحص...")
                    requests.post("https://www.virustotal.com/api/v3/urls", data={"url": url_input}, headers=headers)
                    st.warning("يرجى إعادة الضغط بعد 30 ثانية.")
        else:
            st.warning("الرجاء إدخال رابط أولاً.")

# --- التبويب الثاني المطور: مولد كلمات المرور مع "جو التصفيق" ---
with tab2:
    st.header("Smart Password Generator")
    st.write("قم بتوليد كلمات مرور قوية وتحليل مستوى أمانها.")
    
    length = st.slider("طول كلمة المرور:", min_value=8, max_value=64, value=16)
    use_symbols = st.checkbox("إضافة رموز خاصة (!@#$%^&*)", value=True)
    use_numbers = st.checkbox("إضافة أرقام (123456)", value=True)
    
    if st.button("توليد كلمة مرور ✨"):
        chars = string.ascii_letters
        if use_numbers: chars += string.digits
        if use_symbols: chars += string.punctuation
        
        password = ''.join(random.choice(chars) for i in range(length))
        
        st.success("تم التوليد بنجاح:")
        st.code(password)
        
        st.markdown("### 🛡️ تحليل قوة الأمان:")
        
        if length < 10:
            st.error("المستوى: ضعيف جداً ❌ (يمكن كسرها بسهولة)")
        elif 10 <= length < 14:
            st.warning("المستوى: متوسط ⚠️ (جيدة للاستخدام العادي)")
        elif length >= 14 and (use_symbols or use_numbers):
            # --- إضافة جو التصفيق والاحتفال ---
            st.success("المستوى: خارق 💪 (تحتاج لآلاف السنين لكسرها!)")
            st.snow() # إضافة تأثير الثلج
            
            # رسائل تصفيق منبثقة متتالية
            st.toast("كفووو يا بطل! 👏")
            time.sleep(0.4)
            st.toast("أمن سيبراني عالي المستوى! 👏👏")
            time.sleep(0.4)
            st.toast("عاشت إيدك يا علي! 👏👏👏", icon="🛡️")
        else:
            st.info("المستوى: جيد، ولكن يفضل زيادة الرموز.")

# 4. التذييل
st.markdown("---")
st.caption(f"© {time.strftime('%Y')} Developed by Ali Al-Murtadha Yassin | Cybersecurity Engineering Student")
