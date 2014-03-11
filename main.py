import tkinter as tk
from tkinter import ttk
import datetime
import time
import threading
import export_session


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        '''Maps window geometry with all fields and buttons'''
        self.paused = False

        self.new_button = tk.ttk.Button(self, text="New session",
                                        command=self.new_session)
        self.new_button.grid(column=0, row=0)

        self.export_button = tk.ttk.Button(self, text="Export session",
                                           command=self.export_text)
        self.export_button.grid(column=1, row=0)

        self.session_notes = tk.Text(self)
        self.session_notes.grid(column=0, row=1, columnspan=4, rowspan=3)

        self.session_time = tk.StringVar()
        self.session_time_field = tk.ttk.Entry(self,
                                               textvariable=self.session_time)
        self.session_time_field.grid(column=4, row=0)

        self.progress_bar = tk.ttk.Progressbar(self, length=300)
        self.progress_bar.grid(column=0, row=4, columnspan=3)

        self.time_label_text = tk.StringVar()
        self.time_label = tk.ttk.Label(self, textvariable=self.time_label_text)
        self.time_label.grid(column=3, row=4)

        self.start_button = tk.ttk.Button(self, text="Start session",
                                          command=self.start_session)
        self.start_button.grid(column=4, row=4)

        self.pause_button = tk.ttk.Button(self, text="Pause session",
                                          command=self.pause_session)
        self.pause_button.config(state="disabled")
        self.pause_button.grid(column=4, row=5)

    def start_session(self):
        '''Starts set_progress() thread, initializing session time by
        reading session_time_field'''
        self.time = self.session_time_field.get()
        if (self.time.isdigit()):
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.session_time_field.config(state="disabled")

            self.time = int(self.time)
            self.time = self.time * 60

            if self.paused is True:
                self.current_time = self.saved_time
                self.paused = False
            else:
                self.current_time = 0
                self.progress_bar["value"] = 0

            self.progress_bar["maximum"] = self.time
            self.t = threading.Thread(target=self.set_progress)
            self.t.daemon = True
            self.t.start()

    def set_progress(self):
        '''Counts the time, changing progress bar to current progress.
        Label is used to countdown session time.
        Start button becomes inactive on start'''
        while (self.current_time < self.time):
            if self.paused is False:
                time.sleep(1)
            else:
                break
            if self.paused is False:
                self.current_time = self.current_time + 1
                self.progress_bar["value"] = self.current_time
                self.time_to_go = self.time - self.current_time
                self.clock = datetime.time(minute=(self.time_to_go // 60),
                                           second=(self.time_to_go % 60))
                self.time_label_text.set(str(self.clock))
        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.session_time_field.config(state="normal")

    def export_text(self):
        self.text = self.session_notes.get('1.0', 'end')
        if self.text:
            export_session.export_session_to_html(self.text)

    def pause_session(self):
        self.saved_time = self.current_time
        self.paused = True

    def new_session(self):
        self.paused = True
        self.saved_time = 0
        self.pause_button.config(state="disabled")
        self.progress_bar["value"] = 0
        self.time_label_text.set("")
        self.session_time.set("")
        self.session_notes.delete('1.0', 'end')


root = tk.Tk()
app = Application(master=root)
app.master.title("PySessionTester")
app.mainloop()
