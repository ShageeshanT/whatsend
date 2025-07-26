import pywhatkit as pwk
import pyautogui
import time

def show_banner():
    banner = r"""
   ███████╗██╗  ██╗ █████╗  ██████╗  ███████╗ ███████╗
   ██╔════╝██║  ██║██╔══██╗██╔════╝  ██╔════╝ ██╔════╝
   ███████╗███████║███████║██║  ███╗ █████╗   █████╗  
   ╚════██║██╔══██║██╔══██║██║   ██║ ██╔══╝   ██╔══╝  
   ███████║██║  ██║██║  ██║╚██████╔╝ ███████╗ ███████╗
   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚══════╝ ╚══════╝

     📱 [ SHAGEE WHATSAPP AUTOMATER] 💣
    """
    print(banner)

# Start the script
show_banner()

# Get user input
raw_number = input("Enter recipient's phone number (e.g., 771234567): ").strip()
if not raw_number.startswith("+"):
    phone_number = "+94" + raw_number.lstrip("0")  # Convert to international format
else:
    phone_number = raw_number

message = input("Enter the message to send: ").strip()
count = int(input("How many times should the message be sent? "))

# Ask user for timing option
use_current_time = input("Use current time for immediate sending? (y/n): ").strip().lower()

if use_current_time == 'y':
    current_time = time.localtime()
    send_hour = current_time.tm_hour
    send_minute = (current_time.tm_min + 2) % 60  # Add 2 minutes for safety
else:
    send_hour = int(input("Enter hour to send (24h format): "))
    send_minute = int(input("Enter minute to send: "))

# Open WhatsApp and send the first message
print(f"\n[•] Opening WhatsApp Web to send first message at {send_hour}:{send_minute:02d}...")
pwk.sendwhatmsg(phone_number, message, send_hour, send_minute)

# Wait until WhatsApp Web is open
print("[•] Waiting for WhatsApp Web to load...")
time.sleep(30)

# Send remaining messages
print(f"[•] Sending {count - 1} additional messages at 1-second intervals...\n")
for i in range(count - 1):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(1)

print("✅ All messages sent successfully!")
