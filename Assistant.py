import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib

Owner="My lord"

#browser_path='C://Program Files//Mozilla Firefox//firefox.exe %s'    
browser_path='C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'

songs_dir="F:\\songs\\new"

myeid="fidf4601@gmail.com"      
pwd="FIDF4601@gmail.com"
l=["google","youtube","stackoverflow","reddit","instagram","codeforces","hackerrank","geeksforgeeks","W3schools"]
print("Initializing.............Your voice Assistant.....")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
def speak(text):
	engine.say(text)
	engine.runAndWait() 
def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening>>>>>>")
		audio=r.listen(source)
	try:
		print("Recognizing.......")
		querry= r.recognize_google(audio,language ="en-in")
		print(f"user said: {querry}\n")
	except Exception as e:
		print("Can't regonize")
		querry=None
	return querry
def sendMail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(myeid,pwd)
	server.sendmail(myeid,to,content)
	server.close()

def wish():
	hour=int(datetime.datetime.now().hour)
	if(hour>=0 and hour<12):
		x="Good Morning " + Owner
	elif hour>=12 and hour<18:
		x="Good Afternoon " + Owner
	else:
		x="Good Evening "+ Owner
	return x

print("Hello!!! "+wish()+" How can I help You")
speak("Hello!!! "+wish()+" How can I help You")

while(True):
	querry = takeCommand();speak(querry)
	try:
		if(querry==None or querry.lower()=="exit"):
			print("Happy to help you!!! Good Bye....")
			speak("Happy to help you!!! Good Bye....")
			break
		else:
			querry=querry.lower()
			if 'wikipedia' in querry:
				speak('searching on wikipedia...')
				querry=querry.replace('wikipedia',"" )
				results=wikipedia.summary(querry,sentences =2)
				print(results)
				speak(results)
			elif(('calculate' in querry) or ('+' in querry) or ('-' in querry) or ('x' in querry) or ('*' in querry) or ('/' in querry) or ('divided by' in querry) or ('multiplied by' in querry)):
				try:
					if('calculate' in querry):
						querry=querry.replace('calculate','')
					if('x' in querry):
						querry=querry.replace('x','*')
					elif('multiplied by' in querry):
						querry=querry.replace('multiplied by','*')
					elif('divided by' in querry):
						querry=querry.replace('di vided by','/')
					print(querry)
					z=eval(querry)
					print(z)
					speak(z)
				except Exception as e:
					print(e)
					speak("Can't " + str(e))
			elif ('play music' in querry) or ('open music' in querry) or ('play song' in querry):
				songs=os.listdir(songs_dir)
				os.startfile(os.path.join(songs_dir,songs[0]))
			elif 'the time' in querry:
				strTime=datetime.datetime.now().strftime("%H:%M:%S")
				speak(f"{Owner} the time is {strTime}")
				print(f"{Owner} the time is {strTime}")
			elif ('send email' in querry or 'send an email' in querry or 'send mail' in querry or 'send a mail' in querry) :
				print()
				print("To Which Email-id you wanna send message? :-")
				speak("To Which Email-id you wanna send message?")
				eid=""
				eid = takeCommand();
				f=0
				if(eid==None):
					print("You said nothing or we can't recognize you")
					speak("You said nothing or we can't recognize you")
					f=1
				else:
					f=0
					while(' ' in eid):
						eid=eid.replace(' ','')
					speak(eid); print(eid)
					print("Is this right email-id?YES or NO:-")
					speak("Is this right email-id???? YES or NO???")
					querry = takeCommand();
					if(querry==None):
						print("You said nothing or we can't recognize you")
						speak("You said nothing or we can't recognize you")
						f=1	
					elif('y' in querry.lower()):
						f=0
					else:
						f=1
				if(f==1):
					print("Enter via keyboard")
					eid=input()	
				f=0
				print("Tell me the messege you wanna send")
				speak("Tell me the messege you wanna send")
				msg=""
				msg = takeCommand(); speak(msg);
				if(msg==None):
					print("You said nothing or we can't recognize you")
					speak("You said nothing or we can't recognize you")
					f=1
				else:
					print("Is this right msg???   YES or NO")
					speak("Is this right msg???   YES or NO")
					querry = takeCommand(); print(querry)
					if(querry==None):
						print("You said nothing or we can't recognize you")
						speak("You said nothing or we can't recognize you")
						f=1	
					elif('y' in querry.lower()):
						f=0
					else:
						f=1
				if(f==1):
					print("Enter via Message via keyboard")
					msg=input()
				print("My email id is",myeid)
				sendMail(eid,msg)
				print("Email has been sent!!!!")
			elif ('open' in querry):
				querry=querry.replace('open','')
				f=0
				for querry in l:
					url=querry+'.com'
					f=1
					break
				if f==1:
					webbrowser.open(url)
				else:
					google = querry
					webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)	
			else:
				google = querry
				webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)
	except Exception as e:
		speak("Exception occured ")
		print("Exception occured := ",e)			

			
				
				
		

		
	