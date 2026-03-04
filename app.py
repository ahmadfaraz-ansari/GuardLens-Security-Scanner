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
# --- LOGIN PAGE (Updated with Form for 'Enter' Key) ---
if not st.session_state.logged_in:
    st.title("🔐 GuardLens Access Control")
    
    # Form ka use karne se "Enter" key kaam karne lagegi
    with st.form("login_form"):
        email = st.text_input("Corporate Email")
        password = st.text_input("Access Token", type="password")
        submit_button = st.form_submit_button("Authenticate") # Ye "Enter" support karta hai
        
        if submit_button:
            # Apne naya wala password yahan check karo
            if email and password == "student_2026": # Jo tune change kiya tha
                st.session_state.logged_in = True
                send_login_alert(email)
                st.success("Access Granted! Initializing Suite...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Credentials.")

# --- MAIN SCANNER PAGE ---
# --- MAIN SCANNER PAGE (Updated for Enter Key) ---
else:
    st.sidebar.title("🛡️ GuardLens Pro")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🌐 Automated Web Security Auditor")
    
    # Dashboard ko bhi Form mein daal dete hain
    with st.form("audit_form"):
        target = st.text_input("Target Domain", placeholder="example.com")
        launch_button = st.form_submit_button("Launch Audit") # Ab ye Enter se chalega!
        
        if launch_button:
            if target:
                log_area = st.empty() # Ek khali jagah banao logs ke liye
                with st.spinner("Scanning..."):
                    # Ab terminal ki jagah screen pe dikhao
                    log_area.info(f"[*] Starting audit for {target}...")
                    
                    # Backend calls
                    find_subdomains(target)
                    log_area.info("[+] Subdomain discovery finished.")
                    
                    check_security(f"http://{target}")
                    log_area.info("[+] Header analysis finished.")
                    
                st.success(f"Audit for {target} completed!")
                st.balloons()
