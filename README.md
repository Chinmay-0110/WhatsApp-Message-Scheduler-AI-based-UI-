# WhatsApp-Message-Scheduler-AI-based-UI-
A simple web-based application to schedule WhatsApp messages using a clean UI.  
Users can input a phone number, a message, select the time, and the system automatically opens WhatsApp Web and sends the message at the scheduled time.

---

## 🚀 Features

- ✅ Schedule WhatsApp messages by selecting time
- ✅ Country selector with flag & code
- ✅ Clean, user-friendly UI (HTML, CSS, JS)
- ✅ Python Flask backend for scheduling logic
- ✅ Simulated message sending in online deployments (Render)

---

## 🧠 How It Works

- The user enters the phone number, message, and time.
- On real/local machines, it uses `pywhatkit` to:
  - Open WhatsApp Web
  - Locate the recipient
  - Send the message automatically
- On cloud deployments (Render), the system **simulates** the message sending (because real browser-based sending is not allowed in cloud).

---

## 🧪 Technologies Used

- 🔙 Python 3 (Flask)
- 🌐 HTML + CSS + Vanilla JavaScript
- 📦 pywhatkit (for local WhatsApp automation)
- 🌍 Render.com (for cloud hosting the UI)

---

## ⚙️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/whatsapp-scheduler.git
cd whatsapp-scheduler
