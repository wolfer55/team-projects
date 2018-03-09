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



    def on_play_button_click(self):
        print("hello this wokrs")

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

            except:
                showerror("Cant open this type of File")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
