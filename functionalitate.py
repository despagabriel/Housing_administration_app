from interfata_bazaDate import Databases
from tkinter import *

root = Tk()

data1 = Databases("C:/Users/Gabi/PycharmProjects/despa/Gestionare_aplicatie/baza_date.json")
data_info = data1.read_data()
print(data_info)

root.title('                                                              - Gestionare01-')
root.geometry("600x500")
root.config(background="gray")


def autentification():
    username = user.get()
    pasword = password.get()
    for dictionar in data_info.values():
        if username in dictionar:
            if pasword == dictionar[username]["password"]:
                debt.config(text=f' Your debt is: {dictionar[username]["toPay"]} ron ')
                balance.config(text=f' Balance: {dictionar[username]["balance"]} ron ')
                status.config(text='Online')
                break
        else:
            status.config(text=" contact the administrator")


def pay():
    username = user.get()
    pasword = password.get()
    pay = payment.get()
    for dictionar in data_info.values():
        if username in dictionar:
            if int(pay) >= 0:
                if pasword == dictionar[username]["password"]:
                    dictionar[username]["toPay"] -= int(pay)
                    if dictionar[username]["toPay"] <= 0:
                        dictionar[username]["balance"] += (-(dictionar[username]["toPay"]))
                        dictionar[username]["toPay"] = 0
                        balance.config(text=f' Balance: {dictionar[username]["balance"]} ron ')
                        debt.config(text=f' Your debt is: {dictionar[username]["toPay"]} ron ')
                    else:
                        dictionar[username]["balance"] = 0
                        balance.config(text=f' Balance: {dictionar[username]["balance"]} ron ')
                        debt.config(text=f' Your debt is: {dictionar[username]["toPay"]} ron ')
            else:
                pay = 0
    data1.save_data(data_info)
    payment.delete(0, END)


def logout1():
    user.delete(0, END)
    password.delete(0, END)
    payment.delete(0, END)
    debt.config(text="Debt")
    status.config(text="Offline")
    balance.config(text="Balance")


# entry field

user = Entry(root, width=40, )
user.grid(row=1, column=1, padx=5, pady=5)
password = Entry(root, width=40, show="*")
password.grid(row=2, column=1)
payment = Entry(root, width=40)
payment.grid(row=4, column=2, padx=5, pady=5)

# labels

status = Label(root, font=30, width=30, bg="white", fg="green", text='Offline')
status.grid(row=5, column=1, padx=5, pady=5)
debt = Label(root, font=30, width=30, bg="white", fg="green", text="Debt")
debt.grid(row=1, column=2, padx=5, pady=5)
balance = Label(root, font=30, width=30, bg="white", fg="green", text='Balance')
balance.grid(row=2, column=2)

# buttons

login = Button(root, padx=20, pady=3, text="login", font=10, bg='green', fg='white',
               borderwidth=15, activebackground="green", activeforeground="white", command=autentification)
login.grid(row=4, column=1, padx=5, pady=5)
pay_button = Button(root, padx=20, pady=3, text="  pay  ", font=10, bg='green', fg='white', borderwidth=15, command=pay)
pay_button.grid(row=6, column=2)
logout = Button(root, padx=20, pady=3, text="Logout", font=10, bg='red', fg='white',
                borderwidth=15, activebackground="yellow", activeforeground="white", command=logout1)
logout.grid(row=7, column=2, pady=5, padx=5)

root.mainloop()
