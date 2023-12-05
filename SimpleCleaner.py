import gc
import threading
import sys
import psutil
import ctypes
import customtkinter as ctk
import pywinstyles
import PIL, PIL.Image
import pystray
import tkthread
import pyglet
import json
import os
import tkinter.messagebox as msg

def setlang(var):
    a = var.lower()
    with open('language.txt', 'w') as kd:
        kd.write(a)
        kd.close()
    msg.showinfo("The language has been changed", "Restart the app!")
    close()


if not os.path.isfile("translate.json"):
    msg.showerror("Error", "File 'translate.json' missing")
    sys.exit()
if not os.path.isfile("language.txt"):
    with open("language.txt", "w+") as f:
        f.write("english")
        f.close()
else:
    with open("language.txt", "r") as f:
        a = f.read()
        if a == "russian":
            with open("translate.json", "r", encoding='utf-8') as d:
                ma = json.load(d)
                aw = ma["russian"]["MainTAB"]
                bw = ma["russian"]["Settings"]
                cw = ma["russian"]["MemoryUsage"]
                dw = ma["russian"]["Clean"]
                ew = ma["russian"]["CleanWhenAbove"]
                fw = ma["russian"]["NotifyWhenAbove"]
                gw = ma["russian"]["DangerousThreshold"]
                iw = ma["russian"]["CriticalThreshold"]
                ij = ma["russian"]["Language"]
                lang = "Russian"
                d.close()
        elif a == "english":
            with open("translate.json", "r", encoding='utf-8') as d:
                ma = json.load(d)
                aw = ma["english"]["MainTAB"]
                bw = ma["english"]["Settings"]
                cw = ma["english"]["MemoryUsage"]
                dw = ma["english"]["Clean"]
                ew = ma["english"]["CleanWhenAbove"]
                fw = ma["english"]["NotifyWhenAbove"]
                gw = ma["english"]["DangerousThreshold"]
                iw = ma["english"]["CriticalThreshold"]
                ij = ma["english"]["Language"]
                lang = "English"
                d.close()
        else:
            with open("translate.json", "r", encoding='utf-8') as d:
                ma = json.load(d)
                aw = ma["english"]["MainTAB"]
                bw = ma["english"]["Settings"]
                cw = ma["english"]["MemoryUsage"]
                dw = ma["english"]["Clean"]
                ew = ma["english"]["CleanWhenAbove"]
                fw = ma["english"]["NotifyWhenAbove"]
                gw = ma["english"]["DangerousThreshold"]
                iw = ma["english"]["CriticalThreshold"]
                ij = ma["english"]["Language"]
                lang = "English"
                d.close()


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



def playnotify():
    try:
        music = pyglet.resource.media('MemNotify.mp3')
        music.play()
    except:
        pass

def valid(inp):
    return inp.isdigit()


class GUI:
    def __init__(self):
        ctk.set_default_color_theme("theme.json")
        ctk.set_appearance_mode("dark")

        self.window = ctk.CTk()
        self.window.title("Simple Cleaner")
        pywinstyles.apply_style(self.window, 'mica')
        self.window.resizable(False, False)

        self.xa = ctk.StringVar(value="off")
        self.xa2 = ctk.StringVar(value="off")
        self.xa3 = ctk.StringVar()
        self.xa4 = ctk.StringVar()
        self.xa5 = ctk.StringVar()
        self.xa6 = ctk.StringVar()
        self.vad = ctk.StringVar()
        self.validcmd = self.window.register(valid)

        self.tabview = ctk.CTkTabview(self.window, border_width=1)
        self.tabview.pack()

        self.tab_1 = self.tabview.add(aw)
        self.tab_2 = self.tabview.add(bw)


        self.window.iconbitmap("logo1.ico")
        self.window.config()

        self.memory_label = ctk.CTkLabel(self.tab_1, text=cw)
        self.memory_label.pack()

        self.memory_bar = ctk.CTkCanvas(self.tab_1, width=300, height=20)
        self.memory_bar.pack()

        self.lablperc = ctk.CTkLabel(self.tab_1, text="")
        self.lablperc.pack()

        self.null1 = ctk.CTkLabel(self.tab_1, text="ㅤ")
        self.null1.pack()

        self.button = ctk.CTkButton(self.tab_1, text=dw, command=clean)
        self.button.pack()

        self.fr = ctk.CTkFrame(self.tab_2, height=20)
        self.fr.pack()

        self.inpp = ctk.CTkEntry(self.fr, width=50, validate='key', validatecommand=(self.validcmd,'%S'))
        self.inpp.grid(row=0, column=1)

        self.taucl = ctk.CTkCheckBox(self.fr, variable=self.xa, width=25, text=ew, onvalue="on", offvalue="off")
        self.taucl.grid(row=0, column=0)

        self.fr2 = ctk.CTkFrame(self.tab_2, height=20)
        self.fr2.pack()

        self.ntfe = ctk.CTkEntry(self.fr2, width=50, validate='key', validatecommand=(self.validcmd,'%S'))
        self.ntfe.grid(row=0, column=1)

        self.chkd = ctk.CTkCheckBox(self.fr2, variable=self.xa2, width=25, text=fw, onvalue="on", offvalue="off")
        self.chkd.grid(row=0, column=0)

        self.null2 = ctk.CTkLabel(self.tab_2, text="ㅤ")
        self.null2.pack()

        self.fr3 = ctk.CTkFrame(self.tab_2, height=40)
        self.fr3.pack()


        self.dangerpercl = ctk.CTkLabel(self.fr3, text=gw, text_color="orange")
        self.dangerpercl.grid(row=0, column=0)

        self.dangerperc = ctk.CTkEntry(self.fr3, width=35, validate='key', validatecommand=(self.validcmd,'%S'))
        self.dangerperc.grid(row=0, column=1)

        self.critpercl = ctk.CTkLabel(self.fr3, text=iw, text_color="red")
        self.critpercl.grid(row=1, column=0)

        self.critperc = ctk.CTkEntry(self.fr3, width=35, validate='key', validatecommand=(self.validcmd,'%S'))
        self.critperc.grid(row=1, column=1)

        self.null3 = ctk.CTkLabel(self.tab_2, text="")
        self.null3.pack()

        self.fr4 = ctk.CTkFrame(self.tab_2)
        self.fr4.pack()

        self.langlbl = ctk.CTkLabel(self.fr4, text=ij)
        self.langlbl.grid(column=0, row=0)

        self.langsel = ctk.CTkComboBox(self.fr4, values=["Russian", "English"], width=90)
        self.langsel.configure(command=lambda var: setlang(self.langsel.get()))
        self.langsel.set(lang)
        self.langsel.grid(column=1, row=0)



        try:
            self.update_memory_bar()
        except:
            pass


    def cauto(self, a, b, c):
        if a == "on":
            if b >= c:
                clean()

    def notify(self, a, b, c):
        if a == "on":
            if b >= c:
                playnotify()


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

        aa = self.dangerperc.get()
        bb = self.critperc.get()


        if not aa:
            self.dangerperc.delete(0, 'end')
            self.dangerperc.insert(0, "60")
        else:
            if int(aa) <= 0:
                self.dangerperc.delete(0, 'end')
                self.dangerperc.insert(0, "60")
            elif int(aa) > 100:
                self.dangerperc.delete(0, 'end')
                self.dangerperc.insert(0, "60")

        if not bb:
            self.critperc.delete(0, 'end')
            self.critperc.insert(0, "90")
        else:
            if int(bb) <= 0:
                self.critperc.delete(0, 'end')
                self.critperc.insert(0, "90")
            elif int(bb) < 100:
                self.critperc.delete(0, 'end')
                self.critperc.insert(0, "90")


        try:
            if int(self.dangerperc.get()) <= memory_percent < int(self.critperc.get()):
                self.lablperc.configure(text_color="orange")
            elif int(self.dangerperc.get()) <= memory_percent >= int(self.critperc.get()):
                self.lablperc.configure(text_color="red")
            else:
                self.lablperc.configure(text_color="white")
        except:
            self.lablperc.configure(text_color="white")


        mer = str(round(memory_percent)) + "%" + " ({0}/{1} GB)".format(mem1, mem2)
        self.lablperc.configure(text=mer)

        self.memory_bar.create_rectangle(0, 0, bar_width, bar_height, fill='orange')

        self.memory_bar.create_rectangle(bar_width, 0, 300, bar_height, fill='green')

        try:
            self.window.after(1000, self.update_memory_bar)
        except:
            pass

        self.cauto(a=self.xa.get(), b=str(round(memory_percent)), c=str(self.inpp.get()))
        self.notify(a=self.xa2.get(), b=str(round(memory_percent)), c=str(self.ntfe.get()))


    def run(self):
        self.window.mainloop()

    def stop(self):
        self.window.destroy()



def open_menu():
    g = GUI()
    tkthread.call(g.run)


def maid():
    global icon
    image = PIL.Image.open('logo1.png')
    icon = pystray.Icon("Simple Cleaner", image, menu=pystray.Menu(
            pystray.MenuItem("Open", open_menu, default=True),
            pystray.MenuItem("Clean", clean),
            pystray.MenuItem("Close", close)
    ))
    icon.run()

def close():
    global icon
    g = GUI()
    icon.stop()
    g.stop()
    sys.exit()



if __name__ == "__main__":
    maid()
