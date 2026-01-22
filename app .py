import streamlit as st
import pdfplumber

st.title("🔎 জন্ম তারিখ অনুসন্ধান")
gender = st.radio("তালিকা বেছে নিন:", ("পুরুষ", "মহিলা"))
dob = st.text_input("জন্ম তারিখ লিখুন (যেমন: 01/01/1995)")

if st.button("খুঁজুন"):
    file_name = "purus.pdf" if gender == "পুরুষ" else "mohila.pdf"
    try:
        with pdfplumber.open(file_name) as pdf:
            found = False
            for page in pdf.pages:
                text = page.extract_text()
                if dob in text:
                    st.success("✅ তথ্য পাওয়া গেছে!")
                    st.info(text) 
                    found = True
                    break
            if not found:
                st.error("❌ এই তারিখের কিছু পাওয়া যায়নি।")
    except:
        st.error("ফাইল খুঁজে পাওয়া যায়নি!")
