"""
Webcam Login Monitor for Windows

This script captures an image from the webcam when executed and emails it to a specified
email address. It's designed to be triggered on login attempts to monitor who is
accessing the computer. Runs silently without showing any window when using pythonw.exe.

Author: User
Date: 2023
"""

import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import datetime
import sys

def capture_and_email():
    """
    Main function that captures an image from the webcam and emails it.
    
    The function performs the following steps:
    1. Captures an image using the computer's webcam
    2. Saves the image temporarily with a timestamp
    3. Emails the image to the configured recipient
    4. Cleans up by deleting the temporary image file
    """
    # Set path to the script directory for file operations
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Generate unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image_filename = f"login_attempt_{timestamp}.jpg"
    image_captured = False
    
    # Removed log file creation code

    try:
        # Step 1: Capture Image from Webcam
        # Try multiple camera indices if the default doesn't work
        cam = None
        for cam_index in range(3):  # Try camera indices 0, 1, 2
            cam = cv2.VideoCapture(cam_index)
            if cam.isOpened():
                break
            cam.release()
        
        if not cam or not cam.isOpened():
            return
            
        # Give the webcam a moment to initialize
        for _ in range(5):  # Take multiple frames to allow camera to adjust
            cam.read()
        
        result, image = cam.read()
        if result:
            cv2.imwrite(image_filename, image)  # Save the captured image
            cam.release()  # Release the webcam
            image_captured = True
        else:
            cam.release()
            return  # Stop if image capture failed

        # Step 2: Email Configuration
        # NOTE: Replace these with your email details or use environment variables
        sender_email = "your_email@gmail.com"  # Replace with your email
        sender_password = "your_app_password"  # Replace with your app password
        receiver_email = "your_email@gmail.com"  # Replace with recipient email

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Laptop Login Attempt Detected"
        computer_name = os.environ.get('COMPUTERNAME', 'Unknown')
        username = os.environ.get('USERNAME', 'Unknown')
        body_text = f"A login attempt was detected on your laptop.\n\nComputer: {computer_name}\nUser: {username}\nTime: {timestamp}"
        msg.attach(MIMEText(body_text, 'plain'))

        # Attach the captured image to the email
        try:
            with open(image_filename, "rb") as attachment:  # Using with statement for proper file handling
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {image_filename}")
                msg.attach(part)
        except FileNotFoundError:
            # Continue without attachment instead of returning early
            pass

        # Step 3: Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail, use smtp.gmail.com and port 587
            server.starttls()  # Enable TLS for security
            server.login(sender_email, sender_password)  # Login to your email account
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)  # Send the email
            server.quit()  # Close the SMTP server connection
        except Exception:
            pass
            
    finally:
        # Step 4: Cleanup - Always delete the temporary image file if it was created
        if image_captured:
            try:
                os.remove(image_filename)
            except OSError:
                pass


if __name__ == "__main__":
    capture_and_email()
