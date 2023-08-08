import threading
import sys
import psutil
import ctypes
import customtkinter as ctk
import pywinstyles
import PIL, PIL.Image
import pystray
import tkthread


def clean():
    try:
        process_list = psutil.process_iter()
        for process in process_list:
            if process.pid != psutil.Process().pid:
                handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, process.pid)
                if handle:
                    ctypes.windll.psapi.EmptyWorkingSet(handle)
                    ctypes.windll.kernel32.CloseHandle(handle)
    except:
        pass




class GUI:
    def __init__(self):
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("dark")

        self.window = ctk.CTk()
        self.window.title("Simple Cleaner")

        self.window.geometry("320x200")
        pywinstyles.apply_style(self.window, 'mica')

        self.window.iconbitmap("logo1.ico")
        self.window.config()

        self.memory_label = ctk.CTkLabel(self.window, text="Memory Usage:")
        self.memory_label.pack()

        self.memory_bar = ctk.CTkCanvas(self.window, width=300, height=20)
        self.memory_bar.pack()

        self.lablperc = ctk.CTkLabel(self.window, text="")
        self.lablperc.pack()

        self.null1 = ctk.CTkLabel(self.window, text="ㅤ")
        self.null1.pack()

        self.button = ctk.CTkButton(self.window, text="Clean", command=clean)
        self.button.pack()

        self.update_memory_bar()

    def update_memory_bar(self):
        memory = psutil.virtual_memory()
        used_memory = memory.total - memory.available
        memory_percent = (used_memory / memory.total) * 100

        self.memory_bar.delete("all")

        bar_width = (memory_percent / 100) * 300
        bar_height = 20

        KB = float(1024)
        GB = float(KB ** 3)

        mem1 = round(number=used_memory / GB, ndigits=1)
        mem2 = round(number=memory.total / GB, ndigits=1)

        mer = str(round(memory_percent)) + "%" + " ({0}/{1} GB)".format(mem1, mem2)
        self.lablperc.configure(text=mer)

        self.memory_bar.create_rectangle(0, 0, bar_width, bar_height, fill='orange')


        self.memory_bar.create_rectangle(bar_width, 0, 300, bar_height, fill='green')

        self.window.after(1000, self.update_memory_bar)

    def run(self):
        self.window.mainloop()

    def stop(self):
        self.window.destroy()



def open_menu():
    g = GUI()
    a = tkthread.call(g.run)


def main():
    global icon
    image = PIL.Image.open('logo1.png')
    icon = pystray.Icon("Simple Optimizer", image, menu=pystray.Menu(
            pystray.MenuItem("Open", open_menu),
            pystray.MenuItem("Clean", clean),
            pystray.MenuItem("Close", close)
    ))
    icon.run()

def close():
    global icon
    g = GUI()
    icon.stop()
    tkthread.call_nosync(g.stop)
    sys.exit()



if __name__ == "__main__":
    main()
