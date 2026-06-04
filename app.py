import streamlit as st

# 1. ตั้งค่าหน้าเพจ (ดึง layout="wide" ของเดิมมาใช้)
st.set_page_config(page_title="Boot Camp: DS & ML", layout="wide", page_icon="🏠")

# 2. ใส่ Custom CSS เล็กน้อยเพื่อตกแต่งปุ่มให้ดูสวยเด่นและสม่ำเสมอกัน
st.markdown("""
    <style>
    /* ปรับแต่งปุ่ม Streamlit ให้กว้างเต็มคอลัมน์และดูมีมิติ */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #E5E7EB;
        padding: 12px;
        font-size: 16px;
        transition: all 0.3s ease;
        background-color: #FFFFFF;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    /* เอฟเฟกต์ตอนเอาเมาส์ไปชี้ที่ปุ่ม */
    div.stButton > button:hover {
        border-color: #3B82F6;
        color: #3B82F6;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_style_html=True)

# 3. ส่วนหัวข้อ (Header) ปรับให้ดูเป็นระเบียบและโปรแกรมเมอร์สไตล์
st.title("🏠 หน้าหลัก")

# ใช้ columns ช่วยแบ่งพื้นที่ส่วนหัวให้ดูสมดุล
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.write("### Boot Camp: Data Science and Machine Learning")
    st.caption("🚀 7 Day Intensive Hands-on Workshop")
with header_col2:
    # นำโค้ดกลุ่มมาทำเป็นตั๋วเก๋ๆ มุมขวา
    st.info("⚽ **Team:** LLVQ")

# แถบแถลงเนื้อหาวันเรียน
st.success("📘 **Day 1:** การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")
st.markdown("---")

# 4. ส่วนของปุ่มกดแยกตามหมวดหมู่ (Navigation Menu)
st.write("### 🗂️ เมนูระบบและแอปพลิเคชัน")

# --- หมวดหมู่ที่ 1: ระบบคำนวณพื้นฐาน ---
st.markdown("#### 🧮 General Tools")
col_basic = st.columns(3) # แบ่งเป็น 3 บล็อกสั้นๆ
with col_basic[0]:
    if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
        st.switch_page("pages/app1_discount_calc.py")

# --- หมวดหมู่ที่ 2: เครื่องมือจัดการข้อมูล (Data Preparation) ---
st.markdown("#### 🧹 Data Cleaning & Transformation")
col_clean = st.columns(4) # แบ่งเป็น 4 คอลัมน์เรียงหน้ากระดาน

with col_clean[0]:
    if st.button("🧼 Customers Data Cleaner"):
        st.switch_page("pages/clean_customers.py")
with col_clean[1]:
    if st.button("📱 การทำความสะอาดข้อมูล APP"):
        st.switch_page("pages/clean_app.py")
with col_clean[2]:
    if st.button("📊 การทำความสะอาดข้อมูล"):
        st.switch_page("pages/cleaningbyLLVQ.py")
with col_clean[3]:
    if st.button("💫 การแปลงข้อมูล (Transform)"):
        st.switch_page("pages/transform_app.py")

# --- หมวดหมู่ที่ 3: การวิเคราะห์และพยากรณ์ (Data Analysis & Analytics) ---
st.markdown("#### 🔮 Data Analysis & Prediction")
col_predict = st.columns(3) # แบ่งเป็น 3 คอลัมน์ใหญ่ขึ้นมาหน่อย

with col_predict[0]:
    if st.button("☄️ การวิเคราะห์ข้อมูลเชิงสำรวจ (EDA)"):
        st.switch_page("pages/EDA_app.py")
with col_predict[1]:
    if st.button("🛍️ การพยากรณ์ยอดขายแบบง่าย"):
        st.switch_page("pages/sale_predict.py")
with col_predict[2]:
    if st.button("🚚 การพยากรณ์ระยะเวลาขนส่ง"):
        st.switch_page("pages/truck_predict.py")
