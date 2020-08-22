from cPetrol import Petrol_inter
from tkinter import *


class petrol_data_inter:
    def __init__(self):
        self.window_Petrol_inter = Tk()
        self.window_Petrol_inter.title("About Petrol")
        self.window_Petrol_inter.state('zoomed')

        Petrol_inter_label = Label(self.window_Petrol_inter, text=" Petrol Inter in Filling Station",
                                   font=("time new roman", 30, "bold"), relief=GROOVE,
                                   height=2, width=50, bg="red", fg="white").pack(side=TOP, fill=X)

        label_day = Label(self.window_Petrol_inter, text="Enter DD").pack()
        enter_day = Entry(self.window_Petrol_inter).pack()

        label_Month = Label(self.window_Petrol_inter, text="Enter MM").pack()
        enter_Month = Entry(self.window_Petrol_inter).pack()

        label_year = Label(self.window_Petrol_inter, text="Enter YYYY").pack()
        enter_Year = Entry(self.window_Petrol_inter).pack()

        label_liter = Label(self.window_Petrol_inter, text="Enter Petrol Amount in Liters").pack()
        enter_liter = Entry(self.window_Petrol_inter).pack()

        label_price = Label(self.window_Petrol_inter, text="Enter Purchasing Price").pack()
        enter_price = Entry(self.window_Petrol_inter).pack()

        making_button = Button(self.window_Petrol_inter, text="Save Data", font=("time new roman", 10, "bold"), bg="red",
                               fg="white", relief=GROOVE, height=1, width=7, command=lambda:
            [
                Petrol_inter(enter_day.get(), enter_Month.get(),
                             enter_Year.get(), enter_liter.get(), enter_price.get())
            ]).pack()
        self.window_Petrol_inter.mainloop()


 # obj = petrol_data_inter()