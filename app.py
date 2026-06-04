import streamlit as st

# 1. ตั้งค่าหน้าเพจ
st.set_page_config(page_title="Boot Camp: DS & ML", layout="wide", page_icon="🏠")

# 2. ปรับแต่ง CSS ใหม่ (กำหนดสีตัวอักษรบนปุ่มให้เข้มชัดเจน และเปลี่ยนสีตามการ Hover)
st.markdown("""
    <style>
    /* ปรับแต่งปุ่มสากล */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 14px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.25s ease;
        
        /* แก้ปัญหาตัวหนังสือจาง: บังคับให้พื้นหลังเป็นสีอ่อน และตัวหนังสือเป็นสีมืด */
        background-color: #F8FAFC !important;
        color: #1E293B !important;
        border: 2px solid #E2E8F0 !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* เอฟเฟกต์เฉพาะปุ่มเมื่อเอาเมาส์ไปชี้ (Hover) ให้เปลี่ยนเป็นธีมสีฟ้าสดใส */
    div.stButton > button:hover {
        background-color: #3B82F6 !important;
        color: #FFFFFF !important;
        border-color: #2563EB !important;
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
        transform: translateY(-3px);
    }
    
    /* ตกแต่งหัวข้อหมวดหมู่ให้น่าอ่านขึ้น */
    .category-title {
        font-size: 20px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 12px;
        color: #F1F5F9; /* สีขาวนวลสำหรับ Dark mode */
    }
    </style>
""", unsafe_allow_html=True)

# 3. ส่วนหัวข้อ (Header)
st.title("🏠 หน้าหลัก")

header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.write("### Boot Camp: Data Science and Machine Learning")
    st.caption("🚀 7 Day Intensive Hands-on Workshop")
with header_col2:
    st.info("⚽ **Team:** LLVQ")

st.success("📘 **Day 1:** การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")
st.markdown("---")

# 4. ส่วนของปุ่มกดแยกตามหมวดหมู่
st.write("### 🗂️ เมนูระบบและแอปพลิเคชัน")

# --- หมวดหมู่ที่ 1: ระบบคำนวณพื้นฐาน ---
st.markdown('<p class="category-title">🧮 General Tools</p>', unsafe_style_html=False)
col_basic = st.columns(3)
with col_basic[0]:
    if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
        st.switch_page("pages/app1_discount_calc.py")

# --- หมวดหมู่ที่ 2: เครื่องมือจัดการข้อมูล (Data Preparation) ---
st.markdown('<p class="category-title">🧹 Data Cleaning & Transformation</p>', unsafe_style_html=False)
col_clean = st.columns(4)

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
st.markdown('<p class="category-title">🔮 Data Analysis & Prediction</p>', unsafe_style_html=False)
col_predict = st.columns(3)

with col_predict[0]:
    if st.button("☄️ การวิเคราะห์ข้อมูลเชิงสำรวจ (EDA)"):
        st.switch_page("pages/EDA_app.py")
with col_predict[1]:
    if st.button("🛍️ การพยากรณ์ยอดขายแบบง่าย"):
        st.switch_page("pages/sale_predict.py")
with col_predict[2]:
    if st.button("🚚 การพยากรณ์ระยะเวลาขนส่ง"):
        st.switch_page("pages/truck_predict.py")
