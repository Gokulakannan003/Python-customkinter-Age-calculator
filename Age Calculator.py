from customtkinter import *
from datetime import datetime

root = CTk()
root.title("Age Calculator")
root.geometry("480x400")
root.resizable(False, False)
root.configure(fg_color="azure")


def calculate_age():
    birthdate_input = input1.get()
    birthdate = datetime.strptime(birthdate_input, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year

    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    label2.configure(text=f"You are {age} years old")


label1 = CTkLabel(root, text="A g e  c a l c u l a t o r", font=("ROG FONTS", 20, "bold"))
label1.place(x=95, y=10)

frame1 = CTkFrame(root, width=501, height=356, corner_radius=0, fg_color="ivory4")
frame1.place(x=0, y=45)

CTkLabel(frame1, text="Enter your", font=("Arial black", 20, "bold")).place(x=185, y=30)
CTkLabel(frame1, text="date of birth", font=("Arial black", 20, "bold")).place(x=173, y=60)

input1 = CTkEntry(frame1,
                  width=190,
                  corner_radius=2,
                  font=("Arial black", 20, "bold"))
input1.place(x=145, y=100)

submit = CTkButton(frame1,
                   text="Submit",
                   font=("Arial black", 20, "bold"),
                   hover_color="orange",
                   fg_color="orangered",
                   command=calculate_age)
submit.place(x=170, y=170)


label2 = CTkLabel(frame1,
                  font=("Arial black", 20, "bold"),
                  text="Format YYYY-MM-DD")
label2.place(x=125, y=220)


label2 = CTkLabel(frame1,
                  font=("Arial black", 20, "bold"),
                  text="")
label2.place(x=126, y=275)

root.mainloop()
