from tkinter import *

FONT = ('Arial', 10, "bold")

# INTERFACE
# screen
window = Tk()
window.minsize(width=300, height=200)
window.title("BMI Calculator")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')
# label
first_label = Label(text="Enter Your Weight (kg)", font=FONT)
first_label.place(x=150, y=40, anchor=CENTER)
second_label = Label(text="Enter Your Height (cm)", font=FONT)
second_label.place(x=150, y=80, anchor=CENTER)
third_label = Label(text="", font=FONT, anchor=CENTER)
third_label.place(x=150, y=160, anchor=CENTER)
# entry
first_entry = Entry(width=15)
first_entry.place(x=150, y=60, anchor=CENTER)
second_entry = Entry(width=15)
second_entry.place(x=150, y=100, anchor=CENTER)
# button
my_button = Button(text="Calculate", width=10)
my_button.place(x=150, y=130, anchor=CENTER)


# FUNCTIONS


def bmi_calc(w, h):
    height = (h / 100)
    sonuc = (w / (height * height))
    return sonuc


def is_not_blank(s):
    return bool(s and not s.isspace())


def result(d):
    sayi = round(d,2)
    if d < 18.5:
        return "Your BMI is {}. You are under weight".format(sayi)
    elif d < 25:
        return "Your BMI is {}. You are normal weight".format(sayi)
    elif d < 30:
        return "Your BMI is {}. You are over weight".format(sayi)
    else:
        return "Your BMI is {}. You are obese".format(sayi)


def button_click():
    third_label.config(text="")
    if (len(first_entry.get()) == 0) or (len(second_entry.get()) == 0):
        third_label.config(text="Enter both weight and height!")
    else:
        try:
            weight = int(first_entry.get())
            height = int(second_entry.get())
            res = bmi_calc(weight, height)
            third_label.config(text=result(res))
        except:
            third_label.config(text="Enter a valid number!")



my_button.config(command=button_click)
window.mainloop()
