from tkinter import *
from tkinter import messagebox as mbox
import serial
import time

#membuat jendela
window = Tk()
window.geometry("300x400")
window.resizable(0,0)

# atur ukuran window dan menempatkan window di tengah layar PC/Laptop
lebar = 300
tinggi = 400 
setTengahX = (window.winfo_screenwidth()-lebar)//2
setTengahY = (window.winfo_screenheight()-tinggi)//2
window.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))

# atur Judul Window
window.title("Control LED")

#membuat judul
judul = Label(window,text="KOMUNIKASI SERIAL\n PYTHON DAN ARDUINO",font='Helvetica 16 bold').place(x=25,y=0)

#fungsi tombol
kondisi1 = -1
kondisi2 = -1


def tombolku1():
    global kondisi1
    kondisi1 *= -1
    if kondisi1 == 1:
        tombol1 = Button(window,text = 'TOMBOL 1 = ON',fg='black',bg = "#4c8cbc",font = 'Helvetica 12',command = tombolku1).place(x=10,y=180)
    else :
        tombol1 = Button(window,text = 'TOMBOL 1=OFF',fg='black',bg = "#4c8cbc",font = 'Helvetica 12',command = tombolku1).place(x=10,y=180)

def tombolku2():
    global kondisi2
    kondisi2 *= -1
    if kondisi2 == 1:
        tombol2 = Button(window,text = 'TOMBOL 2 = ON',fg='black',bg = "#fcd43c",font = 'Helvetica 12',command = tombolku2).place(x=160,y=180)
    else:
        tombol2 = Button(window,text = 'TOMBOL 2=OFF',fg='black',bg = "#fcd43c",font = 'Helvetica 12',command = tombolku2).place(x=160,y=180)

#membuat textbox
def hapusTbox():
    Tbox.delete(1.0,END)

#membuat serial port
serialKu = serial.Serial(port='com6',baudrate = 9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)

#membuat indikator
I1 = Text(height=2, width=5,fg = 'blue',bg='white')
I1.place(x=20,y=100)
I2 = Text(height=2, width=5,fg = 'blue',bg='white')
I2.place(x=80,y=100)
I3 = Text(height=2, width=5,fg = 'blue',bg='white')
I3.place(x=150,y=100)
I4 = Text(height=2, width=5,fg = 'blue',bg='white')
I4.place(x=220,y=100)

#fungsi bacaData 
def readData():
    dataHasil = serialKu.readline()
    print(dataHasil)
    if dataHasil == b'A\r\n':
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        mbox.showinfo('info','INDIKATOR I1 NYALA')
        time.sleep(2)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        time.sleep(2)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I2, I3, dan I4 NYALA')
        time.sleep(2)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)
        
    elif dataHasil == b'B\r\n':
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)
        time.sleep(2)
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        mbox.showinfo('info','INDIKATOR I1 dan I2 NYALA')
        time.sleep(2)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        time.sleep(2)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I3 dan I4 NYALA')
        time.sleep(2)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

    elif dataHasil == b'C\r\n':
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        mbox.showinfo('info','INDIKATOR I1 dan I3 NYALA')
        time.sleep(2)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I2 dan I4 NYALA') 
        time.sleep(2)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

    elif dataHasil == b'D\r\n':
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','SEMUA INDIKATOR NYALA')
        time.sleep(2)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)        
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)
        

    elif dataHasil == b'E\r\n':
        #A
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        mbox.showinfo('info','INDIKATOR I1 NYALA')
        time.sleep(1)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        time.sleep(1)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I2, I3, dan I4 NYALA')
        time.sleep(1)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

        #B
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)
        time.sleep(1)
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        mbox.showinfo('info','INDIKATOR I1 dan I2 NYALA')
        time.sleep(1)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        time.sleep(1)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I3 dan I4 NYALA')
        time.sleep(1)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

        #C
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        mbox.showinfo('info','INDIKATOR I1 dan I3 NYALA')
        time.sleep(1)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I2 dan I4 NYALA')
        time.sleep(1)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

        #D
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','SEMUA INDIKATOR NYALA')
        time.sleep(1)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)        
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)


    elif dataHasil == b'F\r\n':
       #A
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        mbox.showinfo('info','INDIKATOR I1 NYALA')
        time.sleep(3)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        time.sleep(3)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I2, I3, dan I4 NYALA')
        time.sleep(3)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

        #B
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)
        time.sleep(3)
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        mbox.showinfo('info','INDIKATOR I1 dan I2 NYALA')
        time.sleep(3)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        time.sleep(3)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I3 dan I4 NYALA')
        time.sleep(3)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

        #C
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        mbox.showinfo('info','INDIKATOR I1 dan I3 NYALA')
        time.sleep(3)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','INDIKATOR I2 dan I4 NYALA')
        time.sleep(3)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

        #D
        I1 = Text(height=2, width=5,fg = 'blue',bg='red')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='yellow')
        I2.place(x=80,y=100)
        I3 = Text(height=2, width=5,fg = 'blue',bg='green')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='blue')
        I4.place(x=220,y=100)
        mbox.showinfo('info','SEMUA INDIKATOR NYALA')
        time.sleep(3)
        I1 = Text(height=2, width=5,fg = 'blue',bg='white')
        I1.place(x=20,y=100)
        I2 = Text(height=2, width=5,fg = 'blue',bg='white')
        I2.place(x=80,y=100)        
        I3 = Text(height=2, width=5,fg = 'blue',bg='white')
        I3.place(x=150,y=100)
        I4 = Text(height=2, width=5,fg = 'blue',bg='white')
        I4.place(x=220,y=100)

def kirimData():
    if (kondisi1 == -1) & (kondisi2 == -1) :
        serialKu.write(b'A')
        mbox.showinfo('info','data A terkirim')
         
    elif (kondisi1 == -1) & (kondisi2 == 1) :
        serialKu.write(b'B')
        mbox.showinfo('info','data B terkirim')
        
    elif (kondisi1 == 1) & (kondisi2 == -1) :
        serialKu.write(b'C')
        mbox.showinfo('info','data C terkirim')
        
    elif (kondisi1 == 1) & (kondisi2 == 1) :
        serialKu.write(b'D')
        mbox.showinfo('info','data D terkirim')
        
    
 
#membuat widget
tombol1 = Button(window,text = 'TOMBOL 1=OFF',fg='black',bg = "#4c8cbc",font = 'Helvetica 12',command = tombolku1).place(x=10,y=180)
tombol2 = Button(window,text = 'TOMBOL 2=OFF',fg='black',bg = "#fcd43c",font = 'Helvetica 12',command = tombolku2).place(x=160,y=180)
tomboldel = Button(window,text = "CLEAR",fg = 'black',bg = 'white',font = 'Verdana 10 bold',command = hapusTbox).place(x=230, y=370)
tombolBacaData = Button(window,text="READ ARDUINO",fg = 'black',bg = 'white',font = 'Verdana 10 bold',command = readData).place(x=10,y=370)
tombolKirim = Button(window,text = 'KIRIM DATA',fg='black',bg = 'white',font = 'Verdana 10 bold',command = kirimData).place(x=132,y=370)

window.mainloop()