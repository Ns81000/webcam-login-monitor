# 📷 Webcam Login Monitor for Windows

A Windows-focused Python script that silently captures an image from your webcam on login and emails it to you. Perfect for monitoring unauthorized access to your computer! 🔒

## ✨ Features

- 🤫 Runs completely silently using pythonw.exe (no visible windows or console)
- 📸 Captures an image from the webcam at login
- 📧 Sends the image via email with computer details
- 🧹 Automatically cleans up temporary files
- ⏰ Set up with Windows Task Scheduler for automatic execution

## 📋 Requirements

- 💻 Windows 10 or 11
- 🐍 Python 3.6 or higher
- 📹 Webcam (built-in or external)
- 🌐 Internet connection for sending emails

## 🚀 Step-by-Step Installation Guide

### 1️⃣ Install Python (if not already installed)

1. Download Python from [python.org](https://www.python.org/downloads/windows/)
2. During installation, make sure to check "✅ Add Python to PATH"
3. Complete the installation

### 2️⃣ Install Required Package

Open Command Prompt as administrator and run:
```bash
pip install opencv-python
```

### 3️⃣ Download the Script

Open Command Prompt and run:
```bash
git clone https://github.com/Ns81000/webcam-login-monitor.git
```

### 4️⃣ Configure Email Settings

1. Open the script in a text editor like Notepad
2. Find these lines and replace with your email details:
```python
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
receiver_email = "your_email@gmail.com"
```
> 💡 **Note:** You can use the same email address for both sending and receiving. Gmail is strongly recommended for best reliability and compatibility.

**📣 For Gmail Users:**
- You first need to enable 2-step verification 🔐
- Go to this link [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) ✨
- Type your app name and press create
- Copy and paste this password into the script

### 5️⃣ Set Up Task Scheduler for Silent Execution

1. Press `Win + R`, type `taskschd.msc` and press Enter to open Task Scheduler
2. Click "Create Basic Task" in the right panel
3. Enter a name (e.g., "Webcam Login Monitor") and description
4. Choose "When I log on" as the trigger ✅
5. Select "Start a program" as the action
6. For Program/script, browse to: `C:\Windows\System32\pythonw.exe`
7. For "Add arguments", enter the full path to the script in quotes:
   ```
   "C:\path\to\your\webcam_login_monitor.py"
   ```
8. Click "Next" and then "Finish"
9. Right-click on your newly created task and select "Properties"
10. Check "Run with highest privileges" ✓
11. Go to the "Conditions" tab and uncheck "Start the task only if the computer is on AC power"
12. Click "OK" to save changes

### 6️⃣ Testing Your Setup (Optional)

To test if the script works correctly:

1. Double-click the task in Task Scheduler
2. Select "Run" from the right-side panel
3. Check your email to see if you received the webcam image 📩

## 🔄 What Happens Under Different Conditions

The script is designed to handle various conditions silently. Here's what happens in different scenarios:

### 📹 Webcam Issues
- ❌ **No webcam detected**: The script tries camera indices 0, 1, and 2. If none work, no email is sent
- 🚫 **Failed image capture**: If the webcam can't capture an image, no email is sent
- 🕒 **Initialization delay**: The script allows the webcam a moment to adjust by taking 5 preliminary frames

### 🌐 Network Issues
- 📵 **No internet connection**: If the computer is offline, the script will fail to send the email but will still delete the captured image
- ⏰ **Email server timeout**: Any connectivity issues with the email server are caught and the image is still deleted
- 🔑 **Invalid email credentials**: If your email/password is incorrect, the authentication will fail, but cleanup still occurs

### 💾 File Operations
- 🧹 **Guaranteed cleanup**: The script uses a try-finally block to ensure temporary images are always deleted regardless of errors
- 🔄 **File handling**: If the image file can't be found during email attachment, the script continues execution and attempts to send email without attachment

## 🛠️ Advanced Configuration

### 🔎 Troubleshooting

If you're not receiving emails:

1. Check your email spam folder 📁
2. Verify your app password is correct 🔑
3. Make sure your webcam is working properly 📹

If your webcam light turns on but no image is captured:
- The script tries camera indices 0, 1, and 2
- If needed, modify the script to try other camera indices

## ⚠️ Security Considerations

- 🔒 This script runs silently and takes photos without user notification
- 👮 Use this tool only on your own computers
- ⚖️ Make sure you comply with privacy laws in your region
- 🔐 Secure your email credentials - consider using environment variables

## 🚫 Removing the Monitor

To disable the webcam monitoring:
1. Open Task Scheduler
2. Find your "Webcam Login Monitor" task
3. Right-click and select "Disable" or "Delete" ❌

## 🙋‍♂️ Need Help?

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Make sure all the requirements are installed correctly

Happy monitoring! 🕵️‍♂️
