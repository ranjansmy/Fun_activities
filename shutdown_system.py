import os
import pyttsx3 # pip install pyttsx3==2.7, https://pypi.org/project/pyttsx3/2.7/
import speech_recognition as sr

#Creating Class
class pythonSystem:
	#Method to take voice command as Input
	def takeCommands(self):
		#Using Recognizer and Microphone method for input voice
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('Listening..')
			#Number of seconds of non-speaking audio
			r.pause_threshold = 0.7
			audio = r.liste(source)
			# Voice input is idntified
			try:
				# Listening voice commnads
				print('Recognizing..')
				Query = r.recognize_google(audio, language='en-in')

				# Displaying the voice command
				print("the query is printed='", Query, "'")
			except Exception as e:
				# Displaying exception
				print(e)
				# Exception Handling
				print('Could you repeat, please.')
				return "None"
		return Query

	# Method for voice ouput
	def Speak(self, audio):
		# Constructor call for pyttsx3.init()
		engine = pyttsx3.init('sapi5')
		# Setting voice type and id
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[1].id)
		engine.say(audio)
		engine.runAndWait()

	# Method to self shutdown system
	def quitSelf(self):
		self.Speak("Do you want to switch off the computer !")
		#Input voice command
		take = self.takeCommands()
		choice = take
		if "yes" in choice:
			# Shutting Down
			print("Shutting down the system..")
			self.Speak("Shutting down the System.")
			os.system("shutdown /s /t 30")
		if "no" in choice:
			# Idle
			print("Thanking you")
			self.Speak("Thanking you again")

# Driver Code
if __name__ == '__main__':
	sir = pythonSystem()
	sir.quitSelf()
