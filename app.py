import streamlit as st
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import time
from recon import find_subdomains
from vuln_scanner import check_security

# Load secrets from .env file
load_dotenv()
S_EMAIL = os.getenv("SENDER_EMAIL")
S_PASS = os.getenv("SENDER_PASS")
R_EMAIL = os.getenv("RECEIVER_EMAIL")

# --- EMAIL ALERT FUNCTION ---
def send_login_alert(user_mail):
    try:
        msg = EmailMessage()
        msg.set_content(f"Security Alert: New user {user_mail} logged into GuardLens.")
        msg['Subject'] = 'GuardLens Access Notification'
        msg['From'] = S_EMAIL
        msg['To'] = R_EMAIL
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(S_EMAIL, S_PASS)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        st.sidebar.error(f"Alert Failed: Check .env settings")

# --- UI SETUP ---
st.set_page_config(page_title="GuardLens Web Security", page_icon="🛡️")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN PAGE ---
if not st.session_state.logged_in:
    st.title("🔐 GuardLens Access Control")
    email = st.text_input("Corporate Email")
    password = st.text_input("Access Token", type="password")
    
    if st.button("Authenticate"):
        # Secret Password for Practical: IBM_Student_2026
        if email and password == "student_2026":
            st.session_state.logged_in = True
            send_login_alert(email)
            st.success("Access Granted! Initializing Suite...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Invalid Credentials.")

# --- MAIN SCANNER PAGE ---
else:
    st.sidebar.title("🛡️ GuardLens Pro")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🌐 Automated Web Security Auditor")
    target = st.text_input("Target Domain", placeholder="example.com")
    
    if st.button("Launch Audit"):
        if target:
            with st.spinner("Scanning... Check terminal for real-time logs."):
                # Backend logic calls
                find_subdomains(target)
                check_security(f"http://{target}")
            st.success(f"Audit for {target} finished. Check your folder for reports!")
            st.balloons()