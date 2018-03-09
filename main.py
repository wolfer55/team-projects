import tkinter as tk
import pygubu
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import pyaudio
import wave




class Application:
	def __init__(self,master):
		self.builder = builder = pygubu.Builder()


		builder.add_from_file('teamProj.ui')

		self.mainwindow = builder.get_object('main-frame',master)

		builder.connect_callbacks(self) # Creates the call backs for the gui operations

		self.chunk = 1024

	def on_play_button_click(self):
		self.aud = pyaudio.PyAudio()
		if self.canRun:
			self.stream = self.aud.open(format = self.aud.get_format_from_width(self.file_imported.getsampwidth()),channels = self.file_imported.getnchannels(),rate = self.file_imported.getframerate(), output = True)

			self.data = self.file_imported.readframes(self.chunk)

			while self.data:
				self.stream.write(self.data)
				self.data = self.file_imported.readframes(self.chunk)

	def on_ff_button_click(self):
		print("hello this wokrs")

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
		print("hello this wokrs")

	def on_process_click(self):
		print("yep")






	def loadFile(self):

		if self.fileName:
			try:
				print(self.fileName)
				self.canRun = True
				self.file_imported = wave.open(self.fileName,"rb")
			except:
				showerror("Cant open this type of File")


if __name__ == '__main__':
	root = tk.Tk()
	app = Application(root)
	root.mainloop()
