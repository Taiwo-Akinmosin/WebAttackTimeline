# 🛡️ Web App Attack Timeline Dashboard

This is a simple and educational dashboard that shows how a real-life web application attack happens step-by-step — from phishing to privilege escalation.

---

## 🔧 Technologies Used

- Python 🐍  
- Streamlit (for the web app)  
- Plotly (for the timeline chart)  
- JSON (to store the attack stages)

---

## 📖 What This Project Does

This dashboard helps users **visualize a simulated attack** on a website. It shows each stage an attacker follows, such as:

1. **Phishing Email** – Sends fake login link to the victim  
2. **SQL Injection** – Attacker extracts usernames and passwords  
3. **Login as Victim** – Attacker logs in with stolen credentials  
4. **File Upload** – Attacker uploads a malicious file (web shell)  
5. **Remote Shell** – Gets access to the web server  
6. **Privilege Escalation** – Gains full control (root access)

Each step is shown on a **colorful timeline**, so beginners can easily follow the attack flow.

---

## 💡 Why This Matters

> Web apps are not hacked in just one step — it's a **chain of small vulnerabilities**. This dashboard helps people understand how those attacks happen in sequence.

---

## 🚀 Submission Info

This project was created by **Taiwo Samson**, a 3MTT cybersecurity student, for the **3MTT July Knowledge Showcase** under the **General Learning** category.

---

## 📷 Screenshots

Here’s what the dashboard looks like:

### 🟦 Timeline View
![Timeline](assets/Screenshot_2025-07-11_08_06_23.png)

### 📋 Event Table View
![Event Table](assets/Screenshot_2025-07-11_08_06_32.png)


---

## 📦 How to Run This Project

```bash
git clone https://github.com/Taiwo-Akinmosin/WebAttackTimeline.git
cd WebAttackTimeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

