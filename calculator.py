#import tkinter and ttk for the GUI
#import math for functions
import tkinter as tk
from tkinter import ttk
import math

#Creating the Principal Window
window = tk.Tk()
window.geometry("575x375")
window.title("Calculator")
window.configure(background="grey50")

#creating 2 variables, one for the math functions
#and other for the shown equation on label
equation = tk.StringVar()
simplified_equation=tk.StringVar()
mode=tk.StringVar()
mode.set("RAD")


# Principal label where the equation is shown
Exit = tk.Entry(window, font=("Arial", 20, "bold"), width=22, textvariable=simplified_equation, bd=20, insertwidth=4,bg="powder blue", justify="right")
Exit.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="ew")

# Clear (C)
def clear():
    equation.set(" ")
    simplified_equation.set(" ")

# Result (=)
def resultado():
    try:
        result = round(eval(equation.get()), 2)
        equation.set(result)
        simplified_equation.set(result)
    except:
        equation.set("ERROR")
        simplified_equation.set("ERROR")

#Main Button class
class Button(ttk.Button):
    def __init__(self, master, digit, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.digit = digit
        self.width = 5
        self.style = ttk.Style()
        self.style.configure('My.TButton', font=("Arial", 20))
        self.config(text=str(self.digit))
        self.config(width=self.width, style='My.TButton')
        self.config(command=lambda: self.button_clicked(master, self.digit))
        self.grados = True
    # Click Button Actions and different outputs
    def button_clicked(self, master, input_value):
        global current_input
        global equation
        global mode
        try:
            if input_value == "=":
                open_parentheses = equation.get().count("(")
                close_parentheses = equation.get().count(")")
            # Add the necessary number of closing parentheses
                for i in range(open_parentheses - close_parentheses):
                    equation.set(equation.get() + ")")
                    simplified_equation.set(simplified_equation.get() + ")")
                resultado()
            elif input_value == "C":
                clear()
            elif input_value == "π":
                equation.set(equation.get() + str(math.pi))#used for math function
                simplified_equation.set(simplified_equation.get()+str("π"))#used for window function
            elif input_value == "x":
                equation.set(equation.get() + "*")
                simplified_equation.set(simplified_equation.get()+str("x"))
            elif input_value == "EXP":
                equation.set(equation.get()+"**")
                simplified_equation.set(simplified_equation.get()+str("EXP"))
            elif input_value == "√":
                equation.set(equation.get() + "math.sqrt(")
                simplified_equation.set(simplified_equation.get()+str("√"))
            elif input_value == "sin":
                if mode.get()=="RAD":
                    equation.set(equation.get()+"math.sin(")
                    simplified_equation.set(simplified_equation.get()+str("sin("))
                else:#if mode is DEG
                    equation.set(equation.get()+"math.sin(math.radians(")
                    simplified_equation.set(simplified_equation.get()+str("sin("))
            elif input_value == "cos":
                if mode.get()=="RAD":
                    equation.set(equation.get()+"math.cos(")
                    simplified_equation.set(simplified_equation.get()+str("cos("))
                else:
                    equation.set(equation.get()+"math.cos(math.radians(")
                    simplified_equation.set(simplified_equation.get()+str("cos("))
            elif input_value == "tan":
                if mode.get()=="RAD":
                    equation.set(equation.get()+"math.tan(")
                    simplified_equation.set(simplified_equation.get()+str("tan("))
                else:
                    equation.set(equation.get()+"math.tan(math.radians(")
                    simplified_equation.set(simplified_equation.get()+str("tan("))
            elif input_value == "ln":
                equation.set(equation.get() + "math.log(")
                simplified_equation.set(simplified_equation.get()+str("ln("))
            else:
                equation.set(equation.get() + self.digit)
                simplified_equation.set(simplified_equation.get()+ self.digit)
        except Exception as e:
            equation.set("Error! Not Valid!")
            simplified_equation.set("Error! Not Valid!")

current_input = tk.StringVar()
current_input.set("0")

btn_exp = Button(window, digit="EXP")
btn_exp.grid(row=1, column=1, padx=5, pady=5)

btn_cos = Button(window, digit="cos")
btn_cos.grid(row=2, column=1, padx=5, pady=5)

btn_sin = Button(window, digit="sin")
btn_sin.grid(row=3, column=1, padx=5, pady=5)

btn_tan = Button(window, digit="tan")
btn_tan.grid(row=4, column=1, padx=5, pady=5)

btn_ln = Button(window, digit="ln")
btn_ln.grid(row=5, column=1, padx=5, pady=5)

btn_open = Button(window, digit="(")
btn_open.grid(row=1, column=2, padx=5, pady=5)

btn_7 = Button(window, digit="7")
btn_7.grid(row=2, column=2, padx=5, pady=5)

btn_4 = Button(window, digit="4")
btn_4.grid(row=3, column=2, padx=5, pady=5)

btn_1 = Button(window, digit="1")
btn_1.grid(row=4, column=2, padx=5, pady=5)

btn_dot = Button(window, digit=".")
btn_dot.grid(row=5, column=2, padx=5, pady=5)

btn_pi = Button(window, digit="π")
btn_pi.grid(row=1, column=3, padx=5, pady=5)

btn_8 = Button(window, digit="8")
btn_8.grid(row=2, column=3, padx=5, pady=5)

btn_5 = Button(window, digit="5")
btn_5.grid(row=3, column=3, padx=5, pady=5)

btn_2 = Button(window, digit="2")
btn_2.grid(row=4, column=3, padx=5, pady=5)

btn_0 = Button(window, digit="0")
btn_0.grid(row=5, column=3, padx=5, pady=5)

btn_close = Button(window, digit=")")
btn_close.grid(row=1, column=4, padx=5, pady=5)

btn_9 = Button(window, digit="9")
btn_9.grid(row=2, column=4, padx=5, pady=5)

btn_6 = Button(window, digit="6")
btn_6.grid(row=3, column=4, padx=5, pady=5)

btn_3 = Button(window, digit="3")
btn_3.grid(row=4, column=4, padx=5, pady=5)

btn_equal = Button(window, digit="=")
btn_equal.grid(row=5, column=4, padx=5, pady=5)

btn_clear = Button(window, digit="C")
btn_clear.grid(row=1, column=5, padx=5, pady=5)

btn_div = Button(window, digit="/")
btn_div.grid(row=2, column=5, padx=5, pady=5)

btn_mult = Button(window, digit="x")
btn_mult.grid(row=3, column=5, padx=5, pady=5)

btn_sub = Button(window, digit="-")
btn_sub.grid(row=4, column=5, padx=5, pady=5)

btn_sum = Button(window, digit="+")
btn_sum.grid(row=5, column=5, padx=5, pady=5)
#GRAD and RAD configuration
btn_RAD = Button(window, digit="RAD")
btn_RAD.config(command=lambda: mode.set("RAD"))
btn_RAD.grid(row=2, column=0, padx=5, pady=5)

btn_DEG = Button(window, digit="DEG")
btn_DEG.config(command=lambda: mode.set("DEG"))
btn_DEG.grid(row=1, column=0, padx=5, pady=5)

#Run the Window Loop
window.mainloop()
