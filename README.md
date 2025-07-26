# Whatsend 📱💬

**Whatsend** is an educational Python tool that automates sending WhatsApp messages using WhatsApp Web. Simple CLI-based interaction with message scheduling and batch sending capability.

> **⚠️ DISCLAIMER**
>
> This tool is created strictly for **educational** and **ethical** use only. The developer is **not responsible** for any misuse, abuse, or illegal activities performed with this tool. By using Whatsend, you agree to comply with WhatsApp’s terms of service and any applicable local laws.

---

## ✨ Features

- Send automated WhatsApp messages via WhatsApp Web
- Choose the number of messages and schedule time
- Works with international number formats
- Simulates human typing for additional messages

---

## 📦 Installation

### Prerequisites

- Python 3.x installed
- Google Chrome (WhatsApp Web must be signed in)

### Install required libraries

```bash
pip install pywhatkit pyautogui
```

---
## 🖥️ OS-Specific Setup Commands

### 🌗 Linux

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install pywhatkit pyautogui
sudo apt install scrot python3-tk python3-dev xclip -y
```

### 🪠 Windows

```cmd
pip install pywhatkit pyautogui
```

### 🍎 macOS

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
pip3 install pywhatkit pyautogui
```

## 🚀 Usage

```bash
python whatsend.py
```

### Input Flow

1. Enter recipient's phone number (e.g., `771234567`)
2. Enter your message
3. Set how many times to send
4. Choose to send immediately or schedule it
5. WhatsApp Web will open and send the first message
6. Remaining messages are typed automatically

---

## ⚖️ Legal Notice

- Whatsend is designed for **testing** and **learning purposes only**.
- Use responsibly. Do **not** use this for spamming or harassing individuals.
- The author takes **no responsibility** for any consequences resulting from misuse.
- Use of this tool is entirely at your own risk.

---

## 🧭 Future Plans

- GUI version with message templates
- Multiple recipient scheduling
- Logging and error handling improvements

---

## 💡 Example

```text
Enter recipient's phone number (e.g., 771234567): 771234567
Enter the message to send: Hello from Whatsend!
How many times should the message be sent? 5
Use current time for immediate sending? (y/n): y
```

```
[•] Opening WhatsApp Web...
[•] Sending 4 additional messages...
✅ All messages sent successfully!
```
