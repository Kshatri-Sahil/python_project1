from tkinter import*
import random
from tkinter import Tk

root: Tk=Tk()
root.geometry("400x600")
root.title("DICE SIMLUTOR")
label = Label(root,text='',font=("Bauhaus 93",200),bg='white',padx=200,pady=200)

a=''' _______\n|       |\n|   .   |\n|       |\n|_______|'''

b=''' _______\n|   .   |\n|       |\n|   .   |\n|_______|'''

c=''' _______\n|.      |\n|   .   |\n|      .|\n|_______|'''

d=''' _______\n|.     .|\n|       |\n|.     .|\n|_______|'''

e=''' _______\n|.     .|\n|   .   |\n|.     .|\n|_______|'''

f=''' _______\n|.     .|\n|.     .|\n|.     .|\n|_______|'''

def roll_dice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}',foreground='orange',bg='black')
    label.pack()
def one():
    one = ['\u2680', ]
    label.configure(text=(one))
    label.pack()
def two():
    two = ['\u2681', ]
    label.configure(text=(two))
    label.pack()
def three():
    three = ['\u2682', ]
    label.configure(text=(three))
    label.pack()
def four():
    four = ['\u2683', ]
    label.configure(text=(four))
    label.pack()
def five():
    five = ['\u2684', ]
    label.configure(text=(five))
    label.pack()
def six():
    six = ['\u2685', ]
    label.configure(text=(six))
    label.pack()
def dice2():
    root.state(newstate='iconic')
    lis = [a, b, c, d, e, f]

    turn = int(input("Enter how many times the dice to be rolled: "))
    score = 0
    chturn = 0
    while (turn > chturn):
        n = int(input("Enter the no what the dice will rolled now: "))
        s = random.choice(lis)
        chturn = chturn + 1
        print(s)
        if n == (lis.index(s) + 1):
            print("******Hurry you are correct*******")
            print("\n")
            score = score + 1
        else:
            print("******Oops! It is not correct Please Try again********")
            print("\n")
    print("Your score is {0}".format(score))
    w = input("press y to roll again and n to exit:")
    if w == ('y'):
        print(dice2())
    else:
        print("Have a nice day...")
        root.state(newstate='normal')
def dice():
    root2: Tk = Tk()
    root2.geometry("220x190")
    root2.title("Choice")
    label = Label(root2, text='', font=("Bauhaus 93", 200), bg='black', padx=200, pady=200)

    button1 = Button(root2, text='\u2680', foreground='black', command=one, bg='white', font=("Bauhaus 93", 11))
    button1.pack()

    button2 = Button(root2, text='\u2681', foreground='black', command=two, bg='white', font=("Bauhaus 93", 11))
    button2.pack()

    button3 = Button(root2, text='\u2682', foreground='black', command=three, bg='white', font=("Bauhaus 93", 11))
    button3.pack()

    button4= Button(root2, text='\u2683', foreground='black', command=four, bg='white', font=("Bauhaus 93", 11))
    button4.pack()

    button5= Button(root2, text='\u2684', foreground='black', command=five, bg='white', font=("Bauhaus 93", 11))
    button5.pack()

    button6= Button(root2, text='\u2685', foreground='black', command=six, bg='white', font=("Bauhaus 93", 11))
    button6.pack()

    button7= Button(root2, text='Exit', foreground='black', command=root2.destroy, bg='white', font=("Bauhaus 93", 11))
    button7.pack()

    root2.mainloop()

button=Button(root,text='Roll Dice', foreground='black',command=roll_dice,bg='skyblue', font=("Bauhaus 93",20))
button0=Button(root,text='Dice Choice', foreground='white',command=dice,bg='black', font=("Bauhaus 93",10))
button00=Button(root,text='Play game', foreground='black',command=dice2,bg='gray', font=("Bauhaus 93",10))

button.pack(ipadx=400,ipady=10)
button0.pack(padx=100,pady=0)
button00.pack()

root.mainloop()