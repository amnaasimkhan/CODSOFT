from tkinter import *
import string
import random

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))

root=Tk()
root.title("Password Generator")
root.geometry("570x490+500+100")
root.resizable(False,False)
root.config(bg="black")
choice=IntVar()

passwordLabel=Label(root,text="Password Generator",font=("times new roman",20,"bold"),bg="gray20",fg="white")
passwordLabel.grid(padx=160,pady=15)

weakradioButton=Radiobutton(root,text="Weak",value=1,variable=choice,font=("arial",13,"bold"),bg="gray20",fg="orange")
weakradioButton.grid(pady=15)

mediumradioButton=Radiobutton(root,text="Medium",value=2,variable=choice,font=("arial",13,"bold"),bg="gray20",fg="orange")
mediumradioButton.grid(pady=15)

strongradioButton=Radiobutton(root,text="Strong",value=3,variable=choice,font=("arial",13,"bold"),bg="gray20",fg="orange")
strongradioButton.grid(pady=15)

lengthLabel=Label(root,text="Password Length",font=("arial",13,"bold"),bg="gray20",fg="orange")
lengthLabel.grid(pady=15)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=("arial",13,"bold"))
length_Box.grid(pady=15)

generateButton=Button(root,text="Generate",font=("arial",13,"bold"),bg="gray20",fg="white",command=generator)
generateButton.grid(pady=15)

passwordField=Entry(root,width=20,bd=2,font=("arial",13))
passwordField.grid(pady=15)

root.mainloop()







