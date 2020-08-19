import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import configparser
import os

path_current=os.getcwd()+'\\shoplist_select\\Config.ini'

Config=configparser.ConfigParser()#读取Config.ini文件内容，读取path内容
Config.read(path_current)
path=Config.get('path','current')

window=tk.Tk()#创建window窗体
window.title('ShopList select')
window.geometry('720x600')

prompt=tk.Label(window,text='选择ShopList',font=('Arial',16),width=14,height=1)#Label提升框
prompt.pack(side='top')

frame_select_path=tk.Frame()#facility目录设置器frame
frame_select_path.pack(side='bottom')

def button_path():      #打开目录选择器，更新目录，写入ini文件
    global path
    tmp=path
    print(tmp)
    path=filedialog.askdirectory()
    print(path)
    if path!=None:
        text_path.delete(0.0,'end')
        text_path.insert('end',path)
        Config.set('path','current',path)
        Config.write(open(path_current,'w+'))

text_path=tk.Text(frame_select_path,font=('Arial,12'),height=1)#路径文本显示
text_path.pack(side='left')
text_path.insert('end',path)

button_path=tk.Button(frame_select_path,text='选择目录',font=('Arial',12),width=14,height=1,command=button_path)#路径选择按钮
button_path.pack(side='right')

frame_radiobutton=tk.Frame(window)#radiobutton组frame
frame_radiobutton.pack()

var_filename=tk.StringVar()#radiobutton关联变量
var_filename.set('00')#初始选项

def select_shoplist():       #radiobutton选择函数
    prompt.config(text='You select '+var_filename.get())

#radiobutton数据
MODES=[('00','00'),('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08'),('09','09'),('10','10')]

for test,value in MODES:#批量创建radiobutton
    r=tk.Radiobutton(frame_radiobutton,text=test,font=('Arial',14),variable=var_filename,value=value,command=select_shoplist)
    r.pack()

def button_yes():         #确定按钮点击函数
    tk.messagebox.showinfo(title='切换成功!',message='按确定关闭程序')

button_yes=tk.Button(window,text='确定',font=('Arial',15),width=6,height=1,command=button_yes)#确定按钮
button_yes.pack()

window.mainloop()
