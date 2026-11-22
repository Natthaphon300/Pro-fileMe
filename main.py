import streamlit as st

# ตั้งค่าชื่อแท็บบนเบราว์เซอร์
st.set_page_config(page_title="แนะนำตัว", page_icon="👋")

# ส่วนหัวข้อหลัก
st.title("สวัสดีครับ! ยินดีต้อนรับสู่หน้าเว็บของผม 👋")
st.subheader("นักพัฒนาซอฟต์แวร์มือใหม่ (Python Beginner)")

st.divider()  # เส้นคั่นแบ่งส่วน

# ส่วนข้อมูลแนะนำตัว
st.header("เกี่ยวกับฉัน")
st.write("""
สวัสดีครับ ผมกำลังเริ่มต้นฝึกเขียนโปรแกรมด้วยภาษา Python 
สนใจการสร้างเว็บไซต์ แอปพลิเคชัน และเกมสนุกๆ 
""")

# แบ่งคอลัมน์ซ้าย-ขวา สำหรับความสนใจและทักษะ
col1, col2 = st.columns(2)

with col1:
  st.header("ทักษะที่กำลังฝึก")
  st.write("- 🐍 ภาษา Python")
  st.write("- 🎮 สร้างเกม 2D")
  st.write("- 🌐 สร้างเว็บแอปฯ")

with col2:
  st.header("งานอดิเรก")
  st.write("- เล่นเกม")
  st.write("- ฟังเพลง")
  st.write("- ฝึกเขียนโค้ด")

st.divider()

# ลูกเล่นปุ่มกดโต้ตอบบนหน้าเว็บ
st.header("ทักทายกันหน่อย!")
visitor_name = st.text_input("คุณชื่ออะไรครับ?")

if st.button("ส่งคำทักทาย"):
  if visitor_name:
    st.success(f"ยินดีที่ได้รู้จักครับคุณ {visitor_name}! ขอบคุณที่แวะเข้ามาเยี่ยมชมครับ 🎉")
  else:
    st.warning("พิมพ์ชื่อของคุณก่อนกดปุ่มนะครับ")
