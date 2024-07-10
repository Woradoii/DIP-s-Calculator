import tkinter as tk

class MyCalculator :
    def __init__(self) :
        
        self.root =tk.Tk()

        self.root.geometry("500x500")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello Worada", font=('Arial',18))

        self.button = tk.Button(self.root, text="The clique!!!",height=4)
        self.button.place(x=20,y=50)

        self.root.mainloop()

MyCalculator()