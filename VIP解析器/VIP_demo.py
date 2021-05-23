import requests
import re
import webbrowser
import tkinter


def get_movie():
    entry_get = entry1.get()

    url_original = 'http://jx.cjw123.com/'
    req = requests.get(url=url_original)
    req.encoding = 'utf-8'
    text_get = req.text

    pattern1 = re.compile('value="(.*?)"')
    http_get = re.findall(pattern1, text_get)


    if v.get() == '0':
        url = http_get[0] + entry_get
        webbrowser.open(url)
    elif v.get() == '1':
        url = http_get[1] + entry_get
        webbrowser.open(url)
    elif v.get() == '2':
        url = http_get[2] + entry_get
        webbrowser.open(url)
    elif v.get() == '3':
        url = http_get[3] + entry_get
        webbrowser.open(url)


# GUI界面
screen = tkinter.Tk()
screen.title('VIP播放器')
screen.geometry('400x200')
screen.resizable(0, 0)
label1 = tkinter.Label(screen, text='输入视频播放链接')
label1.grid(row=0, columnspan=4)
entry1 = tkinter.Entry(screen, width=58)
entry1.grid(row=1, columnspan=4)
v = tkinter.StringVar()
radio_button1 = tkinter.Radiobutton(screen, text='端口1', variable=v, value='0')
radio_button2 = tkinter.Radiobutton(screen, text='端口2', variable=v, value='1')
radio_button3 = tkinter.Radiobutton(screen, text='端口3', variable=v, value='2')
radio_button4 = tkinter.Radiobutton(screen, text='端口4', variable=v, value='3')
v.set(0)
radio_button1.grid(row=3, column=0)
radio_button2.grid(row=3, column=1)
radio_button3.grid(row=3, column=2)
radio_button4.grid(row=3, column=3)
button1 = tkinter.Button(screen, text='播放', width=20, height=2, command=get_movie)
button1.grid(row=4, columnspan=4)
screen.mainloop()
