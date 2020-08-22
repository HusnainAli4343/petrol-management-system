from tkinter import *
from purchasing_GUI import petrol_data_inter
from petrol_detail_GUI import read_total_petrol_amount
from daily_selling_petrol import petrol_daily_selling_amount
from p_daily_selling_details import petrol_daily_selling_details


class petrol_code:

    def __init__(self):
        self.main_window = Tk()

        self.main_window.title("Filling station management system")

        self.main_window.state('zoomed')

        self.hiding_label = Label(self.main_window, text=" PSO Filling Station", font=("time new roman", 30, "bold"),
                                  relief=GROOVE,  height=2, width=50, bg="red", fg="white").pack(side=TOP, fill=X)

        self.petrol_detal_enter_button = Button(self.main_window, text="Petrol Purchasing",
                                                font=("time new roman", 10, "bold"), bg="red", fg="white", relief=GROOVE
                                                , height=1, width=15, command=lambda: petrol_data_inter()).pack()

        self.total_petrol_detail_button = Button(self.main_window, text="Total Petrol Details",
                                                 font=("time new roman", 10, "bold"), bg="red", fg="white",
                                                 relief=GROOVE, height=1, width=15,
                                                 command=lambda: read_total_petrol_amount()).pack()

        self.D_S_F_button = Button(self.main_window, text="Petrol Daily selling",
                                   font=("time new roman", 10, "bold"), bg="red", fg="white", relief=GROOVE, height=1,
                                   width=15, command=lambda: petrol_daily_selling_amount()).pack()

        self.D_S_R_button = Button(self.main_window, text="Daily selling Details", font=("time new roman", 10, "bold"),
                                   bg="red", fg="white", relief=GROOVE, height=1, width=15,
                                   command=lambda: petrol_daily_selling_details()).pack()

        self.main_window.mainloop()


obj = petrol_code()