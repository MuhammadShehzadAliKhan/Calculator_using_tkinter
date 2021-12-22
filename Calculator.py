import tkinter
from tkinter import *

window = tkinter.Tk()
#window title
window.title("Calculator")
# window.geometry("300x350")
entry1 = Entry(window,state = 'normal', font = ('Ariel',10,'bold'),readonlybackground='white',justify= RIGHT,width=40)
entry1.grid(row = 0, column = 0,padx = 10,pady = 10, ipady = 30,columnspan = 4)


#Function for add_button

def add_button(number):
    if (number =='='):
        num = eval(entry1.get())
        entry1.delete(0,len(entry1.get()))
        entry1.insert(0,num)
    elif (number == 'C'):
        entry1.delete(0,len(number))
    else:
        entry1.insert(len(entry1.get()),number)



#Define buttons


button_1  =  Button(window, text = "1" ,padx = 30, pady = 20, command = lambda:add_button('1'))
button_2  =  Button(window, text = "2" ,padx = 30, pady = 20, command = lambda:add_button('2'))
button_3  =  Button(window, text = "3" ,padx = 30, pady = 20, command = lambda: add_button('3'))
button_4  =  Button(window, text = "4" ,padx = 30, pady = 20, command = lambda: add_button('4'))
button_5  =  Button(window, text = "5" ,padx = 30, pady = 20, command = lambda:add_button('5'))
button_6  =  Button(window, text = "6" ,padx = 30, pady = 20, command = lambda:add_button('6'))
button_7  =  Button(window, text = "7" ,padx = 30, pady = 20, command = lambda:add_button('7'))
button_8  =  Button(window, text = "8" ,padx = 30, pady = 20, command = lambda:add_button('8'))
button_9  =  Button(window, text = "9" ,padx = 30 ,pady = 20, command = lambda:add_button('9'))
button_0  =  Button(window, text = "0" ,padx = 72, pady = 20, command = lambda:add_button('0'))
button_add = Button(window, text = "+" ,padx = 30, pady = 20, bg ='grey', command = lambda:add_button('+'))
button_divide = Button(window, text = "÷" ,padx = 30, pady = 20,bg ='grey',command = lambda: add_button('/'))
button_multiply = Button(window, text = "x" ,padx = 30, pady = 20,bg ='grey', command = lambda:add_button('*'))
button_subtract = Button(window, text = "-" ,padx = 30, pady = 20,bg ='grey', command = lambda: add_button('-'))
button_dot = Button(window, text = "." ,padx = 30, pady = 20, command = lambda:add_button('.'))
button_equal = Button(window, text = "=" ,padx = 30, pady = 20, command = lambda:add_button('='))
button_clear = Button(window, text = "Clear" ,padx = 107, pady = 20,bg ='teal', command = lambda:add_button('C'))



#Button on the screen
button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)
button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)
button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_0.grid(row = 5, column = 0,columnspan = 2)
button_add.grid(row = 4, column = 3)
button_divide.grid(row = 1, column = 3)
button_multiply.grid(row = 2, column = 3)
button_subtract.grid(row = 3, column = 3)
button_dot.grid(row = 5, column = 2)
button_equal.grid(row = 5, column = 3)
button_clear.grid(row = 1,column = 0,columnspan = 3)
window.mainloop()