import tkinter as tk
import pygubu
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import pyaudio
import wave
import vlc
from pygame import mixer
CHUNK = 256


class Application:
	def __init__(self,master):
		self.builder = builder = pygubu.Builder()
		
		mixer.init()

		builder.add_from_file('teamProj.ui')

		self.mainwindow = builder.get_object('main-frame',master)

		builder.connect_callbacks(self) # Creates the call backs for the gui operations


		self.should_play=True

		self.pa = pyaudio.PyAudio()



		



#	def playingCallback(in_data, frame_count, time_info, status):
#		data = self.file_imported.readframes(frame_count)
#		return (data, pyaudio.paContinue)

		self.play_pause=False
		self.started=False

	def on_play_button_click(self):
		if not self.started:
			mixer.music.play()
			self.started = True
		else:	
			if self.play_pause:
				mixer.music.unpause()
				self.play_unpause=False
			else:
				mixer.music.pause()
				self.play_pause=True


	def on_ff_button_click(self):
		print("hello")

	def on_import_click(self):
		self.fileName = askopenfilename(filetypes=[("MP3 files" ,"*.mp3"),("Wave files" , "*.wav")])
		self.loadFile()

	def on_record_click(self):
		print("hello this wokrs")

	def on_stop_button_click(self):
		print("hello this wokrs")

	def on_click_save(self):
		print("hello this wokrs")

	def on_rewind_button_click(self):
		mixer.music.rewind()


	def on_process_click(self):
		print("yep")






	def loadFile(self):

		if self.fileName:
			#try:
			print(self.fileName)
			self.canRun = True
			#self.file_imported = vlc.MediaPlayer(self.fileName)
			mixer.music.load(self.fileName)
			#except:
				#showerror("Cant open this type of File")

if __name__ == '__main__':
	root = tk.Tk()
	app = Application(root)
	root.mainloop()
