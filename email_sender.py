import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv()

# Function to send email with attachment
def send_email(to_email, to_name, attachment_path):
    from_email = os.getenv('SENDER_EMAIL')
    from_password = os.getenv('GOOGLE_APP_PASSOWRD')
    subject = "Inquiry About Job Opportunities"
    bcc_email="manyamvenkatesh@gmail.com"
    
    # Email body
    body = f"""
    Dear {to_name},
    
    I hope this email finds you well.
    
    My name is Naga Venkatesh Manyam, and I am a software engineer with extensive experience in React, JavaScript, Node.js, and other JavaScript-based technologies. I am currently seeking a full-time position where I can leverage my skills to contribute to a forward-thinking and dynamic team.
    
    I am particularly interested in opportunities within your esteemed organization. With a strong background in developing and deploying robust web applications, I am confident that my expertise aligns well with the needs of your team. My experience includes:
    
    - React and JavaScript: Proficient in developing dynamic, responsive, and user-friendly web applications using React and JavaScript.
    - Node.js: Skilled in building and maintaining scalable back-end services and APIs with Node.js.
    - Full-Stack Development: Comprehensive experience in full-stack development, ensuring seamless integration and high performance across front-end and back-end systems.
    - Project Leadership: Demonstrated ability to lead and collaborate on projects, ensuring timely delivery and high-quality outcomes.
    - React Native: Experience in creating cross-platform mobile applications using React Native.
    
    I am passionate about utilizing my technical skills to drive innovation and efficiency. I have attached my resume for your review and would be grateful for the opportunity to discuss how my background and expertise can contribute to the success of your organization. Please let me know if there are any current or upcoming vacancies that match my profile.
    
    Thank you very much for your time and consideration. I look forward to the possibility of discussing any potential opportunities with you.
    
    Warm regards,
    
    Naga Venkatesh Manyam
    Phone: +971 568142039
    Email: manyam.venkatesh@gmail.com
    LinkedIn: https://www.linkedin.com/in/nagavenkatesh-manyam
    Website: https://nvenkat.dev/
    """
    
    # Set up the email content
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message['Bcc'] = bcc_email
    message.attach(MIMEText(body, 'plain'))
    
    # Attach resume file
    attachment_filename = attachment_path.split('/')[-1]
    attachment = open(attachment_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {attachment_filename}")
    message.attach(part)
    
    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your email provider's SMTP server
    server.starttls()
    server.login(from_email, from_password)
    
    # Send the email
    server.send_message(message)
    server.quit()
    print(f"Email sent to {to_name} at {to_email}")

# Read CSV file with HR contacts
def main():
    df = pd.read_csv('hr_contacts.csv')  # Update with your CSV file path
    
    # Send email to each contact
    for index, row in df.iterrows():
        send_email(row['Email'], row['first_name'], 'Naga_Venkatesh_Manyam_Resume.pdf')  # Update with your resume file path

if __name__ == "__main__":
    main()
