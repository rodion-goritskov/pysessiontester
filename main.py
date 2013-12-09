import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import threading
import export_session


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.new_button = tk.Button(self, text="New session")
        self.new_button.grid(column=0, row=0)

        self.export_button = tk.Button(self, text="Export session",
                                       command=self.export_text)
        self.export_button.grid(column=1, row=0)

        self.session_notes = Text(self)
        self.session_notes.grid(column=0, row=1, columnspan=4, rowspan=3)

        self.session_time = StringVar()
        self.session_time_field = ttk.Entry(self,
                                            textvariable=self.session_time)
        self.session_time_field.grid(column=4, row=0)

        self.progress_bar = ttk.Progressbar(self, length=300)
        self.progress_bar.grid(column=0, row=4, columnspan=3)

        self.start_button = tk.Button(self, text="Start session",
                                      command=self.start_session)
        self.start_button.grid(column=4, row=4)

        self.pause_button = tk.Button(self, text="Pause session")
        self.pause_button.config(state="disabled")
        self.pause_button.grid(column=4, row=5)

    def start_session(self):
        self.time = self.session_time_field.get()
        if (self.time.isdigit()):
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")

            self.time = int(self.time)
            self.time = self.time * 60

            self.progress_bar["value"] = 0
            self.progress_bar["maximum"] = self.time

            self.current_time = 0

            self.t = threading.Thread(target=self.set_progress)
            self.t.daemon = True
            self.t.start()

    def set_progress(self):
        while (self.current_time < self.time):
            time.sleep(1)
            self.current_time = self.current_time + 1
            self.progress_bar["value"] = self.current_time
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")

    def export_text(self):
        self.text = self.session_notes.get('1.0', 'end')
        if self.text:
            export_session.export_session_to_html(self.text)


root = tk.Tk()
app = Application(master=root)
app.master.title("PySessionTester")
app.mainloop()
