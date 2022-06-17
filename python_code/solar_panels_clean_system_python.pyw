from tkinter import *
import random
from datetime import datetime
from time import sleep
from threading import Thread
import re
from tkinter import ttk
import pyfirmata

# На плате Arduino Uno задействованы следующие цифровы пины:
# 5 - реле;
# 7 - реле

'Подключи Arduino к порту номер 3'
board = pyfirmata.Arduino('COM3')
board.digital[5].write(0)
board.digital[7].write(0)
'---------------------------------'

'________________________________________________________Параметры окна'
root = Tk()
root.title("Движение ВПРАВО/ВЛЕВО")
root.geometry('800x530')
root["bg"] = "tan2"
root.resizable(width=False, height=False)
'________________________________________________________Параметры окна'


def avtomat():
    poliv = IntVar()
    i_checkbutton_1 = Checkbutton(text="Автоматическая очистка ВЛЕВО", variable=poliv, onvalue=1,
                                offvalue=0, bg='tan2', font="Helvetica 11 bold", selectcolor='plum2',
                                cursor='dotbox')
    i_checkbutton_1.place(relx=0.02, rely=0.23)
    svet = IntVar()
    i_checkbutton = Checkbutton(text="Автоматическая очситка ВПРАВО", variable=svet,
                                onvalue=1, offvalue=0, bg='tan2', font="Helvetica 11 bold",
                                selectcolor='plum2', cursor='dotbox')
    i_checkbutton.place(relx=0.02, rely=0.3)
    x1 = 0
    x2 = 0
    polival_yes = 0
    svetil = 0


    while True:
        file = open('./config_tech.txt', 'r', encoding='utf8')
        a = file.read()
        x = re.findall(r'\d{2}[.]\d{2}[.]\d{4}', a)
        y = re.findall(r'\d{2}[:]\d{2}', a)
        c = re.findall(r'\d+', a)
        file.close()

        a1 = poliv.get()
        sleep(2)

        if (a1 == 1):
            print('Автомат ВЛЕВО')
            if ((((x[1][6:] + '-' + x[1][3:5] + '-' + x[1][0:2]) == str(datetime.now())[:10]) and (
                    str(datetime.now())[11:16] == y[1])) and (polival_yes == 0)):
                a_time = int(c[13])
                board.digital[5].write(1)
                sleep(a_time)
                board.digital[5].write(0)
                polival_yes = polival_yes + 1
                print('Автомат ВЛЕВО НАЧАЛ!')

            if x1 == 0:
                settings_1()
                x1 = x1 + 1
            else:
                x1 = x1
        else:
            polival_yes = 0

        if a1 == 0:
            x1 = 0

        a2 = svet.get()
        if (a2 == 1):
            print('Автомат ВПРАВО')
            if ((((x[0][6:] + '-' + x[0][3:5] + '-' + x[0][0:2]) == str(datetime.now())[:10]) and (
                    str(datetime.now())[11:16] == y[0])) and (svetil == 0)):
                a_time = int(c[7])
                board.digital[7].write(1)
                sleep(a_time)
                board.digital[7].write(0)
                svetil = svetil + 1
                print('Автомат ВПРАВО НАЧАЛ')


            if x2 == 0:
                settings_1()
                x2 = x2 + 1
            else:
                x2 = x2
        else:
            svetil = 0



'________________________________________________________Задний фон'
photo = PhotoImage(file='10.gif')
w = Label(root, image=photo)
w.place(relx=0.38, rely=0.04)
'________________________________________________________Задний фон'


'///////////////////ФУНКЦИИ////////////////////////'
def settings_1():
    roote = Tk()
    roote.title("Панель настроек")
    roote.geometry('600x300')
    roote.resizable(width=False, height=False)


    def read_parametrs():
        file = open('./config_tech.txt', 'r', encoding='utf8')
        a = file.read()

        x = re.findall(r'\d+', a)
        date_my = re.findall(r'\d{2}\.\d{2}\.\d{4}', a)
        time_my = re.findall(r'\d{2}[:]\d{2}', a)

        a_time = int(x[0])
        a_2_hour = a_time // 3600
        t1.insert(1.0, a_2_hour)
        a_2_minutes = (a_time % 3600) // 60
        t2.insert(1.0, a_2_minutes)
        a_2_sec = (a_time % 3600) % 60
        t3.insert(1.0, a_2_sec)

        t4.insert(1.0, int(x[1]))

        t9.insert(0, date_my[0])
        t14.insert(0, date_my[1])

        t10.insert(0, time_my[0])
        t16.insert(0, time_my[1])

        svet_hour = int(x[7]) // 60
        t21.insert(1.0, svet_hour)
        svet_min = int(x[7]) % 60
        t23.insert(1.0, svet_min)

        poliv_hour = int(x[13]) // 60
        t25.insert(1.0, poliv_hour)
        poliv_min = int(x[13]) % 60
        t27.insert(1.0, poliv_min)



        file.close()


    def save_in_txt():
        a_hour = int(t1.get(1.0, END))
        a_min = int(t2.get(1.0, END))
        a_sec = int(t3.get(1.0, END))
        water_time = int(t4.get(1.0, END))
        light_time = (a_hour * 3600) + (a_min * 60) + a_sec

        a_hour_2 = int(t21.get(1.0, END))
        a_sec_2 = int(t23.get(1.0, END))

        a_hour_3 = int(t25.get(1.0, END))
        a_sec_3 = int(t27.get(1.0, END))


        file = open('./config_tech.txt', 'r', encoding='utf8')
        file.close()
        file_1 = open('./config_tech.txt', 'w', encoding='utf8')

        new_time_1 = str(light_time)
        new_time_2 = str(water_time)
        poliv_time_3 = str((a_hour_3 * 60) + (a_sec_3))
        light_time_2 = str((a_hour_2 * 60) + (a_sec_2))
        svet_date = str(t9.get())
        pol_date = str(t14.get())
        svet_time = str(t10.get())
        pol_time = str(t16.get())

        file_1.write(new_time_1 + '\t\t\t\t\t\t\ttime for RIGTH, sec\n'
                     + new_time_2 + '\t\t\t\t\t\t\ttime for LEFT, sec\n'
                     + svet_date + '\t\t\t\t\t\tdate for start RIGHT\n'
                     + svet_time + '\t\t\t\t\t\t\ttime for start RIGHT\n'
                     + light_time_2 + '\t\t\t\t\t\t\tperiod LEFT\n'
                     + pol_date + '\t\t\t\t\t\tdate for start LEFT\n'
                     + pol_time + '\t\t\t\t\t\t\ttime for start LEFT\n'
                     + poliv_time_3 + '\t\t\t\t\t\t\tperiod RIGHT'
                     )



    l_1 = Label(roote, text='Введите новое время ВПРАВО:', fg='black', font="Helvetica 10 bold")
    l_1.place(relx=0.02, rely=0.05)
    t1 = Text(roote, width=3, height=1, font="Helvetica 15 bold", bg="orange", fg="green")
    t1.place(relx=0.42, rely=0.05)
    l_2 = Label(roote, text='час', fg='black', font="Helvetica 10 bold")
    l_2.place(relx=0.48, rely=0.05)
    t2 = Text(roote, width=3, height=1, font="Helvetica 15 bold", bg="gold2", fg="green")
    t2.place(relx=0.54, rely=0.05)
    l_3 = Label(roote, text='мин', fg='black', font="Helvetica 10 bold")
    l_3.place(relx=0.60, rely=0.05)
    t3 = Text(roote, width=3, height=1, font="Helvetica 15 bold", bg="gold3", fg="green")
    t3.place(relx=0.66, rely=0.05)
    l_4 = Label(roote, text='сек', fg='black', font="Helvetica 10 bold")
    l_4.place(relx=0.72, rely=0.05)
    l_5 = Label(roote, text='Введите новое время ВЛЕВО:', fg='black', font="Helvetica 10 bold")
    l_5.place(relx=0.02, rely=0.2)
    t4 = Text(roote, width=9, height=1, font="Helvetica 15 bold", bg="tan2", fg="green")
    t4.place(relx=0.42, rely=0.2)
    l_6 = Label(roote, text='сек', fg='black', font="Helvetica 10 bold")
    l_6.place(relx=0.6, rely=0.2)
    l_7 = Label(roote, text='Выберите порт подключения:', fg='black', font="Helvetica 10 bold")
    l_7.place(relx=0.02, rely=0.35)
    lst = ['COM1', 'COM2', 'COM3',
           'COM4', 'COM5','COM6',
           'COM7', 'COM8', 'COM9',
           'COM10', 'COM11', 'COM12',
           'COM13', 'COM14', 'COM15',
           'COM16', 'COM17', 'COM18',
           'COM19', 'COM20', 'COM21']
    combo = ttk.Combobox(roote, font="Helvetica 10 bold")
    combo['values'] = lst
    combo.place(relx=0.42, rely=0.35)
    l_8 = Label(roote, text='Автоматическое движение ВПРАВО', fg='green4', font="Helvetica 12 bold")
    l_8.place(relx=0.30, rely=0.45)
    l_9 = Label(roote, text='С какой даты начать:', fg='black', font="Helvetica 10 bold")
    l_9.place(relx=0.01, rely=0.53)
    t9 = Entry(roote, width=11, font="Helvetica 10 bold", bg="tan2", fg="green")
    t9.place(relx=0.27, rely=0.53)
    l_10 = Label(roote, text='С какого времени:', fg='black', font="Helvetica 10 bold")
    l_10.place(relx=0.42, rely=0.53)
    t10 = Entry(roote, width=11, font="Helvetica 10 bold", bg="tan2", fg="green")
    t10.place(relx=0.65, rely=0.53)
    l_11 = Label(roote, text='Переодичность:', fg='black', font="Helvetica 10 bold")
    l_11.place(relx=0.42, rely=0.60)
    t21 = Text(roote, width=5, height=1, font="Helvetica 10 bold",  bg="pink3", fg="green")
    t21.place(relx=0.75, rely=0.60)
    l_22 = Label(roote, text='мин', fg='black', font="Helvetica 10 bold")
    l_22.place(relx=0.80, rely=0.60)
    t23 = Text(roote, width=5, height=1, font="Helvetica 10 bold",  bg="pink3", fg="green")
    t23.place(relx=0.85, rely=0.60)
    l_24 = Label(roote, text='сек', fg='black', font="Helvetica 10 bold")
    l_24.place(relx=0.9, rely=0.60)
    l_12 = Label(roote, text='Автоматическое движение ВЛЕВО', fg='green4', font="Helvetica 12 bold")
    l_12.place(relx=0.30, rely=0.70)
    l_13 = Label(roote, text='С какой даты начать:', fg='black', font="Helvetica 10 bold")
    l_13.place(relx=0.01, rely=0.78)
    t14 = Entry(roote, width=11, font="Helvetica 10 bold", bg="tan2", fg="green")
    t14.place(relx=0.27, rely=0.78)
    l_15 = Label(roote, text='С какого времени:', fg='black', font="Helvetica 10 bold")
    l_15.place(relx=0.42, rely=0.78)
    t16 = Entry(roote, width=11, font="Helvetica 10 bold", bg="tan2", fg="green")
    t16.place(relx=0.65, rely=0.78)
    l_17 = Label(roote, text='Переодичность ВЛЕВО:', fg='black', font="Helvetica 10 bold")
    l_17.place(relx=0.42, rely=0.85)
    t25 = Text(roote, width=5, height=1, font="Helvetica 10 bold",  bg="pink3", fg="green")
    t25.place(relx=0.75, rely=0.85)
    l_26 = Label(roote, text='мин', fg='black', font="Helvetica 10 bold")
    l_26.place(relx=0.80, rely=0.85)
    t27 = Text(roote, width=5, height=1, font="Helvetica 10 bold", bg="pink3", fg="green")
    t27.place(relx=0.85, rely=0.85)
    l_28 = Label(roote, text='сек', fg='black', font="Helvetica 10 bold")
    l_28.place(relx=0.9, rely=0.85)

    Save_1 = Button(roote, width=10, text='Сохранить', bg='gold', fg='green', font=2, command=save_in_txt)
    Save_1.place(relx=0.82, rely=0.02)

    read_parametrs()
    roote.mainloop()

def function_2():
    x = 0
    while True:
        t.delete(1.0, END)
        S = str(datetime.now())[0:19]
        t.insert(1.0, S)
        sleep(1)
        x = x + 1

def rut_2():
    t1 = Thread(target=function_2, daemon=True)
    t1.start()

def rut_3():
    pot2 = Thread(target=avtomat, daemon=True)
    pot2.start()

def light_button_ON_potok():
    pot3 = Thread(target=light_button_ON, daemon=True)
    pot3.start()


def water_button_ON_potok():
    pot4 = Thread(target=water_button_ON, daemon=True)
    pot4.start()

def light_button_ON():
    file = open('./config_tech.txt', 'r', encoding='utf8')
    a = file.read()
    x = re.findall(r'\d+', a)
    a_time = int(x[0])
    board.digital[7].write(1)
    sleep(a_time)
    board.digital[7].write(0)

def light_button_OFF():
    board.digital[7].write(0)


def water_button_ON():
    file = open('./config_tech.txt', 'r', encoding='utf8')
    a = file.read()
    x = re.findall(r'\d+', a)
    a_time = int(x[1])
    board.digital[5].write(1)
    sleep(a_time)
    board.digital[5].write(0)

def water_button_OFF():
    board.digital[5].write(0)

'''_____________________________Потоки на автоматическое включение/отключение____________________________________'''
def light_button_ON_a():
    file = open('./config_tech.txt', 'r', encoding='utf8')
    a = file.read()
    x = re.findall(r'\d+', a)
    a_time = int(x[7])
    board.digital[7].write(1)
    sleep(a_time)
    board.digital[7].write(0)

def light_button_OFF_a():
    board.digital[7].write(0)


def water_button_ON_a():
    file = open('./config_tech.txt', 'r', encoding='utf8')
    a = file.read()
    x = re.findall(r'\d+', a)
    a_time = int(x[13])
    board.digital[5].write(1)
    sleep(a_time)
    board.digital[5].write(0)

def water_button_OFF_a():
    board.digital[5].write(0)

def rut_4():
    pot2 = Thread(target=water_button_ON_a, daemon=True)
    pot2.start()

def rut_5():
    pot2 = Thread(target=light_button_ON_a, daemon=True)
    pot2.start()
'''_____________________________Потоки на автоматическое включение/отключение____________________________________'''



'________________________________________________________Кнопка для полива растений'
Water_1 = Button(root, width=10, text='ВЛЕВО', bg='yellow', font=12, command=water_button_ON_potok)
Water_1.place(relx=0.02, rely=0.05)
'________________________________________________________Кнопка для полива растений'


'________________________________________________________Кнопка для включения света'
Svet_1 = Button(root, width=10, text='ВПРАВО', bg='yellow2', font=12, command=light_button_ON_potok)
Svet_1.place(relx=0.02, rely=0.15)
'________________________________________________________Кнопка для включения света'


'________________________________________________________Кнопка для не полива растений'
Water_1 = Button(root, width=12, text='Откл. ВЛЕВО', bg='orange red', font=12, command=water_button_OFF)
Water_1.place(relx=0.15, rely=0.05)
'________________________________________________________Кнопка для не полива растений'


'________________________________________________________Кнопка для выключения света'
Svet_2 = Button(root, width=12, text='Откл. ВПРАВО', bg='tomato', font=12, command=light_button_OFF)
Svet_2.place(relx=0.15, rely=0.15)
'________________________________________________________Кнопка для выключения света'


'________________________________________________________Кнопка настройки'
Water_1 = Button(root, width=10, text='Настройки', bg='tan1', fg='green4', font=2, command=settings_1)
Water_1.place(relx=0.85, rely=0.9)
'________________________________________________________Кнопка настройки'


t = Text(root, width=18, height=1, font="Helvetica 15 bold", bg="tan2", fg="green", cursor='watch')
t.place(relx=0.01, rely=0.93)

rut_2()
rut_3()

root.mainloop()




