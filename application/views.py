import smtplib
from django.shortcuts import render
from rest_framework.views import APIView

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rest_framework.response import Response
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class SendEmail(APIView):
    def post(self,request):
        try:
            username = request.data.get('username')
            send_to = request.data.get('send_to')


            MESSAGE = MIMEMultipart('alternative')
            MESSAGE['subject'] = "Sample"
            MESSAGE['To'] = send_to
            MESSAGE['From'] = "panku526154@gmail.com"
            MESSAGE.preamble = """
        Your mail reader does not support the report format.
        Please visit us online!"""
            html= """
            <img src="static 'images/email_logo.jpg'" alt="">
            <img src="https://www.nidirect.gov.uk/sites/default/files/styles/nigov_full_620_x1/public/images/email_logo.jpg?itok=ifUhNgCT" alt="Image" height="50%" width=50%>
        <h2>Welcome to {}</h2>

            """.format(username)
            HTML_BODY = MIMEText(html, 'html')
            MESSAGE.attach(HTML_BODY)
            server = smtplib.SMTP('smtp.gmail.com:587')
            if __name__ == "__main__":
                server.set_debuglevel(1)

            password = ""

            server.starttls()
            server.login('panku526154',password)
            server.sendmail('panku526154', send_to, MESSAGE.as_string())
            server.quit()

            return Response({"message":"Message sent successfully"})
        except Exception as e:
            return Response({"error":True,"message":f"{e}"})
    
