from tkinter import *
from  cPetrol import petrol_daily_selling_amount


class daily_selling_amount_petrol:
    def __init__(self):
        daily_selling_amount_petrol = Tk()
        daily_selling_amount_petrol.title("Petrol Daily selling")
        daily_selling_amount_petrol.state('zoomed')

        daily_selling_amount_petrol_label = Label(daily_selling_amount_petrol, text=" Petrol Daily selling ",
                                                  font=("time new roman", 30, "bold"), relief=GROOVE, height=2,
                                                  width=50, bg="red", fg="white").pack(side=TOP, fill=X)

        label_day = Label(daily_selling_amount_petrol, text="Enter DD").pack()
        enter_day = Entry(daily_selling_amount_petrol).pack()

        label_Month = Label(daily_selling_amount_petrol, text="Enter MM").pack()
        enter_Month = Entry(daily_selling_amount_petrol).pack()

        label_year = Label(daily_selling_amount_petrol, text="Enter YYYY").pack()
        enter_Year = Entry(daily_selling_amount_petrol).pack()

        label_liter = Label(daily_selling_amount_petrol, text="Enter Petrol Amount in Liters").pack()
        enter_liter = Entry(daily_selling_amount_petrol).pack()

        label_price = Label(daily_selling_amount_petrol, text="Enter Purchasing Price").pack()
        enter_price = Entry(daily_selling_amount_petrol).pack()

        making_button = Button(daily_selling_amount_petrol, text="Save Data", font=("time new roman", 10, "bold"),
                               bg="red", fg="white",relief=GROOVE, height=1,
                               width=7, command=lambda:
            [
                petrol_daily_selling_amount(enter_day.get(), enter_Month.get(), enter_Year.get(), enter_liter.get()
                                            , enter_price.get())
            ]).pack()

        daily_selling_amount_petrol.mainloop()



# obj = daily_selling_amount_petrol()