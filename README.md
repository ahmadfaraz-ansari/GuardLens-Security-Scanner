GuardLens: Next-Gen Web Security Auditor

"GuardLens" is an automated web reconnaissance and vulnerability assessment suite designed for security professionals and ethical hackers. Built with Python and Streamlit, it provides a professional dashboard for scanning subdomains and auditing security headers.

---

✨ Key Features
* 🔍 **Subdomain Discovery:** High-speed scanning using custom wordlists.
* ⚠️ **Security Audit:** Analyzes HTTP response headers (X-Frame-Options, HSTS, etc.) to detect vulnerabilities like Clickjacking.
* 🔐 **Secure Access:** Built-in authentication system to prevent unauthorized use.
* 📩 **Real-time Alerts:** Integrated SMTP notification system that sends email alerts on every login attempt.
* 💻 **Professional UI:** Clean, interactive web interface powered by Streamlit.

---

🛠️ Technology Stack
* Language: Python 3.13
* Framework: Streamlit (Web UI)
* Networking: Requests, SMTPLib
* Design: Custom CSS & Markdown integration

---

🚀 Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/GuardLens-Scanner.git](https://github.com/your-username/GuardLens-Scanner.git)
   cd GuardLens-Scanner
2. Install Dependencies:

Bash
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the root folder and add your credentials:

Plaintext
SENDER_EMAIL=your-email@gmail.com
SENDER_PASS=your-app-password
Run the Application:

Bash
python -m streamlit run app.py
⚖️ License
Distributed under the MIT License. This project is for educational purposes only.

Developed with ❤️ by A.Faraz
