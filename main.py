import tkinter as tk #basically what imports tkinter

root = tk.Tk() #declare the root (your window)
root.title("My Calculator") # gives your window a title
root.resizable(width=False, height=False)

class Calculator: # defining the calculator class
    def __init__(self, root): #default constructor
        self.e = tk.Entry(root, width=50) #declares the entry
        self.e.grid(row=0, column=0, columnspan=4,padx=10, pady=10) #returns the entry

        buttons = [("AC",0,0), ("+/-",0,1), ('%',0,2), ('/',0,3),
               ('7',1,0), ('8',1,1), ('9',1,2), ('*',1,3),
               ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
               ('1',3,0), ('2',3,1), ('3',3,2), ('+',3,3),
               ('0',4,0), ('.',4,1), ('=',4,2), ("BACK",4,3)]

        for button in buttons:
            text, row, col = button
            self.create_button(root, text, row + 1, col)

    def create_button(self, root, text, row, col):
        btn = tk.Button(root, text=text,width=2,height=4,command=lambda t=text: self.clicker(t))
        btn.grid(row=row, column=col,sticky=tk.W+tk.E)

    def clicker(self, btn_text):
        if btn_text == "AC":
            self.e.delete(0, tk.END)
        elif btn_text == "+/-":
            try:
                current_num = self.e.get()
                if "." in current_num:
                    new_num = float(current_num) * -1
                else:
                    new_num = int(current_num) * -1
                self.e.delete(0, tk.END)
                self.e.insert(tk.END, str(new_num))
            except Exception as el:
                self.e.delete(0, tk.END)
                self.e.insert(tk.END, "Error")
        elif btn_text == "%":
            try:
                current_num = self.e.get()
                new_num = int(current_num) / 100
                self.e.delete(0, tk.END)
                self.e.insert(tk.END, str(new_num))
            except Exception as el:
                self.e.delete(0, tk.END)
                self.e.insert(tk.END, "Error")
        elif btn_text == "BACK":
                size = len(self.e.get())
                self.e.delete(size-1, tk.END)
        elif btn_text == '=':
            try:
                result = eval(self.e.get())
                self.e.delete(0, tk.END)
                self.e.insert(tk.END, result)
            except Exception as el:
                self.e.delete(0, tk.END)
                self.e.insert(tk.END, "Error")
        else:
            self.e.insert(tk.END, str(btn_text))

calculator = Calculator(root)

root.mainloop()
