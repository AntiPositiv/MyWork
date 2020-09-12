from tkinter import *
#
class Block:
    def __init__(self,master):
        self.e_1 = Entry(master, width = 30)
        self.e_2 = Entry(master, width = 30)
        self.l = Label(master,bg="black", fg = "white", width = 40)
        self.b_sum = Button(master, text = "+")
        self.b_den = Button(master, text = "-")
        self.b_div = Button(master, text = "/")
        self.b_mult = Button(master, text = "*")

        self.b_sum['command'] = self.operate('+')
        self.b_den['command'] = self.operate('-')
        self.b_div['command'] = self.operate('/')
        self.b_mult['command'] = self.operate('*')

        self.e_1.pack()
        self.e_2.pack()
        self.b_sum.pack()
        self.b_den.pack()
        self.b_div.pack()
        self.b_mult.pack()
        self.l.pack()

    def operate(self,oper):
        try:
            if oper is '+':
                self.l['text'] = str(float(self.e_1.get()) + float(self.e_2.get()))
            elif oper is '-':
                self.l['text'] = str(float(self.e_1.get()) - float(self.e_2.get()))
            elif oper is '/':
                self.l['text'] = str(float(self.e_1.get()) / float(self.e_2.get()))
            elif oper is '*':
                self.l['text'] = str(float(self.e_1.get()) * float(self.e_2.get()))
        except:
            self.l['text'] = 'Oooops!'
root = Tk()
calc = Block(root)
root.mainloop()