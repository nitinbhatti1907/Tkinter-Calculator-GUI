# Title :- Basic Calculator
# Discription :- A calculator using Tkinter in Python is a software application that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The calculator is built using Tkinter, a GUI library for Python that makes it easy to create graphical interfaces for desktop applications.The calculator interface is created using Tkinter's widgets such as buttons, labels, and entry boxes. The buttons represent the numeric keys and the operations, while the entry box is used to display the results of the calculations.When a user presses a button, the corresponding action is performed, and the result is displayed in the entry box.

from tkinter import *

f_num=s_num=operator=None #--> Assign Global Variable

def get_digit(digit):
    '''
    This method is use to get the digit value those are user can entered for calculation
    '''

    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def get_operator(op):
    '''
    This method is identify the operator and perform task according to that operator
    '''

    global f_num,operator
    f_num = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    '''
    This method is display the result of the given value from the user
    '''

    global f_num,s_num,operator
    s_num = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(f_num+s_num))
    elif operator == '-':
        result_label.config(text=str(f_num-s_num))
    elif operator == '*':
        result_label.config(text=str(f_num*s_num))
    elif operator == '/':
        if s_num == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(f_num/s_num,3)))

def clear():
    '''
    This method is clear the display console on the calculator
    '''

    result_label.config(text='')

root = Tk()
root.title('Calculator')
root.geometry('240x350')
root.resizable(0,0)
root.config(bg='black')

# Code for display result on screen
result_label = Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,sticky='w',pady=(50))
result_label.config(font=('verdana',30,'bold'))

# Code for put the digits on the GUI screen
btn7 = Button(root,text='7',bg='#00a65a',fg='White',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',12))

btn8 = Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',12))

btn9 = Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',12))

btnadd = Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('+'))
btnadd.grid(row=1,column=3)
btnadd.config(font=('verdana',12))

btn4 = Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',12))

btn5 = Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',12))

btn6 = Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',12))

btnsub = Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btnsub.grid(row=2,column=3)
btnsub.config(font=('verdana',12))

btn1 = Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',12))

btn2 = Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',12))

btn3 = Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',12))

btnmul= Button(root,text='×',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('*'))
btnmul.grid(row=3,column=3)
btnmul.config(font=('verdana',12))

btn0= Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=0)
btn0.config(font=('verdana',12))

btnc=Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command=lambda :clear())
btnc.grid(row=4,column=1)
btnc.config(font=('verdana',12))

btnequal= Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
btnequal.grid(row=4,column=2)
btnequal.config(font=('verdana',12))

btndiv= Button(root,text='÷',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btndiv.grid(row=4,column=3)
btndiv.config(font=('verdana',12))

root.mainloop() #--> This is use for display the GUI on screen continully.