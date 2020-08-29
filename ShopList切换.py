import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import configparser
import os
import re
from shutil import copyfile

path_current=os.getcwd()+'\\Config.ini'
shoplist_path=os.getcwd()+'\\shoplist'

Config=configparser.ConfigParser()#读取Config.ini文件内容，读取path内容，读取当前shoplist
Config.read(path_current)
path=Config.get('path','current')
shoplist=Config.get('path','shoplist')
init=Config.getboolean('path','init')

window=tk.Tk()#创建window窗体
window.title('ShopList select')
window.geometry('720x600')
window.minsize(720,600)

prompt=tk.Label(window,text='当前选择的ShopList为:'+shoplist,font=('Arial',16),width=30,height=1)#Label提升框
prompt.pack(side='top')
if init:
    prompt.config(text='使用前请先设置路径')

frame_select_path=tk.Frame()#facility目录设置器frame
frame_select_path.pack(side='bottom')

def button_path():      #打开目录选择器，更新目录，写入ini文件
    global path
    tmp=path
    print(tmp)
    path=filedialog.askdirectory()
    print(path)
    if path=='':     #知识点：当文件选择器未选时，返回值为‘’
        return 0
    else:
        right_path=re.search('/nativePC/common/facility',path)
        if right_path==None:
            if init:
                tk.messagebox.showwarning(title='路径错误',
                                          message='该路径不是商店mod的存放路径,请重新选择,如果common目录中没有facility目录，请手动创建并重新选择')
                return 0
            else:  #TODO:
                tk.messagebox.showwarning(title='路径错误',
                                          message='该路径不是商店mod的存放路径,已经设置好了就不要乱改啦,如果要更换新的游戏路径请选择正确的路径哦,求求各位大侠们不要乱玩我啦')
    text_path.delete(0.0,'end')
    text_path.insert('end',path)
    Config.set('path','current',path)
    Config.set('path','init','False')
    Config.write(open(path_current,'w+'))
    if init:
        prompt.config(text='设置成功!可以愉快的开搞了!')
        init=False

text_path=tk.Text(frame_select_path,font=('Arial,12'),height=1)#路径文本显示
text_path.pack(side='left',fill='x')
if init:
    text_path.insert('end','请选择商店mod存放的facility文件夹,该文件夹位于游戏根目录/nativePC/common中')
else:
    text_path.insert('end',path)

button_path=tk.Button(frame_select_path,text='选择目录',font=('Arial',12),width=14,height=1,command=button_path)#路径选择按钮
button_path.pack(after=text_path)

frame_radiobutton=tk.Frame(window)#radiobutton组frame
frame_radiobutton.pack(fill='x')

var_filename=tk.StringVar()#radiobutton关联变量
var_filename.set(shoplist)#初始选项

def select_shoplist():       #radiobutton选择函数
    prompt.config(text='当前选择的ShopList为:'+var_filename.get())

#radiobutton数据
MODES=[('00: Potion - Aqua Sac (1 - 255)','shopList_00.slt'),
       ('01: Torrent Sac - Vaal Hazak Talon (256 - 510)','shopList_01.slt'),
       ('02: Vaal Hazak Wing - Critical Jewel 2 (511 - 765)','shopList_02.slt'),
       ('03: Tenderized Jewel 2 - Unavailable (766 - 1020)','shopList_03.slt'),
       ('04: Unavailable - Acidic Glavenus Spineshell (1021 - 1275)','shopList_04.slt'),
       ('05: Acidic Glavenus Tailedge - Simple Urn (1276 - 1530)','shopList_05.slt'),
       ('06: Grimalkyne Doll - Protectors: Dried Goldenfish (1531 - 1785)','shopList_06.slt'),
       ('07: Troupers: Horned Urchin - Friendship/Physique Jewel 4 (1786 - 2040)','shopList_07.slt'),
       ('08: Satiated/Physique Jewel 4 - Unavailable (2041 - 2295)','shopList_08.slt'),
       ('09: Unavailable - Unavailable (2296 - 2550)','shopList_09.slt'),
       ('10: Unavailable - Unavailable (2251 - 2774)','shopList_10.slt')]

for test,value in MODES:#批量创建radiobutton
    r=tk.Radiobutton(frame_radiobutton,text=test,font=('Arial',14),variable=var_filename,value=value,command=select_shoplist,justify='left',indicatoron=False)
    r.pack(fill='x',anchor='w')

def button_yes():          #确定按钮点击函数
    #文件复制
    if init:
        tk.messagebox.showwarning(title='未设置商店mod存放目录',
                                  message='请先设置好路径')
        return 0
    shoplist_path_now=shoplist_path+'\\'+var_filename.get()
    copyfile(shoplist_path_now,path+'\\shopList.slt')
    Config.set('path','shoplist',var_filename.get())
    Config.write(open(path_current,'w+'))
    tk.messagebox.showinfo(title='切换成功!',message='按确定返回')

button_yes=tk.Button(window,text='确定',font=('Arial',15),width=6,height=1,command=button_yes)#确定按钮
button_yes.pack()

window.mainloop()
