import pywhatkit as kit
import time

# Your WhatsApp contact (with country code)
phone_number = "+918511419142"  # Replace with recipient's number

# Message to send
message = "Hello love!"

# How many times to send
count = 2

for i in range(count):
    try:
        kit.sendwhatmsg_instantly(phone_number,message, wait_time=10, tab_close=True)
        print(f"Message {i+1} sent!")
        time.sleep(15)  # Wait 15 seconds before sending the next message
    except Exception as e:
        print(f"Error sending message {i+1}: {e}")
