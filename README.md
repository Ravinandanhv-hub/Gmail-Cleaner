# Gmail Unstarred Email Cleaner (Python Automation)

A simple Python tool that automatically deletes all unstarred Gmail emails using the Gmail API, while keeping your important starred emails safe.

This script uses OAuth authentication, fetches up to 500 unstarred emails per request, and continuously loops until your entire inbox is cleaned.

---

## 🚀 Features

- ✅ Deletes only unstarred emails
- ✅ Safely preserves starred/important emails
- ✅ Fetches 500 emails per batch
- ✅ Runs in a loop until everything is deleted
- ✅ OAuth-based secure authentication
- ✅ No password sharing, fully safe

---

## 🛠️ Requirements

- Python 3.8+
- A Google Account
- Gmail API enabled
- OAuth credentials (`credentials.json`)

---

## ✅ Installation & Setup

### 1. Clone or Download the Project

```bash
git clone repo
cd gmail-cleaner
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Activate it:**

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Enable Gmail API & Download Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Go to **APIs & Services** → **Library**
4. Search **Gmail API** → **Enable**
5. Go to **Credentials** → **Create Credentials** → **OAuth Client ID**
6. Choose **Desktop App**
7. Click **Download JSON**
8. Copy paste the content of downloaded json file into `credentials.json`

### ▶️ 5. Run the Script

```bash
python main.py
```

- **First run** → opens a browser for Google login
- **After authorization** → deletes all unstarred emails in batches of 500

---

## 🧹 Script Logic

The script:

1. Authenticates with OAuth
2. Fetches 500 unstarred emails using Gmail search query: `-is:starred`
3. Moves each message to Trash
4. Loops until no unstarred emails remain

---

## ⚠️ Disclaimer

- ⚠️ Use at your own risk
- ⚠️ Double-check starred emails before running
- ⚠️ Deleted emails go to Trash, recoverable for 30 days
