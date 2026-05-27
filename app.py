import streamlit as st
import streamlit.components.v1 as components

# 1. ตั้งค่าพื้นฐาน: เปลี่ยนชื่อเป็น Slide2Life และขยายจอให้กว้างที่สุด
st.set_page_config(
    page_title="Slide2Life",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS Hack: สั่งซ่อนทุกอย่างที่เป็นของ Streamlit เพื่อให้แสดงผลได้คลีนที่สุด
st.markdown("""
    <style>
    /* ซ่อน Header และ Footer */
    header, footer {visibility: hidden !important;}
    
    /* ลบช่องว่างรอบๆ ตัวเว็บเพื่อให้ iframe ชิดขอบ */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    
    /* บังคับให้ส่วนเนื้อหาไม่มีระยะขอบด้านบน */
    [data-testid="stAppViewContainer"] > section:nth-child(2) > div:nth-child(1) {
        padding-top: 0rem !important;
    }

    /* ปรับแต่ง iframe ให้กว้างเต็มจอ */
    iframe {
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ดึงหน้าเว็บ Slide2Life (Lovable) มาแสดง
# ปรับ height เป็น 100vh ผ่านการคำนวณหรือตั้งค่าสูงพอสำหรับหน้าจอมาตรฐาน
components.iframe("https://slide2-vivid-path.lovable.app/", height=900, scrolling=True)
