from tkinter import Tk, Label, Button, Entry

from ozon_neuro import assert_auto
class Draw:
    def __init__(self, master, title, labelText, buttonText, Data):
        self.master = master
        master.title = title
        self.Data = Data

        self.label = Label(master, text=labelText)
        self.label.pack()

       # main_dep, second_dep, learning_rate, accur, epoch

        self.main_dep = Entry()
        self.main_dep.pack()

        self.second_dep = Entry()
        self.second_dep.pack()

        self.learning_rate = Entry()
        self.learning_rate.pack()

        self.accur = Entry()
        self.accur.pack()


        self.epoch = Entry()
        self.epoch.pack()





        self.greet_button = Button(master, text=buttonText, command=self.asser)
        self.greet_button.pack()


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def asser(self):
        assert_auto(int(self.main_dep.get()), int(self.second_dep.get()), float(self.learning_rate.get()), float(self.accur.get()), int(self.epoch.get()))
        self.label.pack()

# root = Tk()
# my_gui = Draw(root,"Класcнная программа", "Первые данные", "Вычислить", 145 )
# root.geometry("400x400")
# root.mainloop()