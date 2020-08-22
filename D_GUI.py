from tkinter import *
import tkinter.messagebox
from Diesel import Diesel_inter
from Diesel import read_D_C_T
from Diesel import Diesel_D_S_I
from cPetrol import read_D_S_i

class Diesel_code():

    def __init__(self):
        self.main_window = Tk()

        self.main_window.title("Filling station management system")

        # main_window.geometry("1000x1000")
        self.main_window.state('zoomed')

        hiding_label = Label(self.main_window, text=" PSO Filling Station", font=("time new roman", 30, "bold"),
                             relief=GROOVE, height=2, width=50, bg="red", fg="white").pack(side=TOP, fill=X)

        Diesel_detal_enter_button = Button(self.main_window, text="Diesel Purchasing", font=("time new roman", 10, "bold"),
                                           bg="red", fg="white", relief=GROOVE, height=1, width=15, command = lambda : making_new_window_1()).pack()

        total_Diesel_detail_button = Button(self.main_window, text="Total Diesel Details", font=("time new roman", 10, "bold"),
                                            bg="red", fg="white", relief=GROOVE, height=1, width=15, command = lambda : read_Diesel_detal() ).pack()

        D_S_F_button = Button(self.main_window, text="Diesel Daily Salling", font=("time new roman", 10, "bold"), bg="red",
                              fg="white", relief=GROOVE, height=1, width=15, command=lambda: D_S_F() ).pack()

        D_S_R_button = Button(self.main_window, text="Daily Salling Details", font=("time new roman", 10, "bold"), bg="red",
                              fg="white", relief=GROOVE, height=1, width=15, command=lambda: D_S_R()).pack()


        def making_new_window_1():
            window_Diesel_inter = Tk()
            window_Diesel_inter.title("About Diesel")
            # window_Petrol_inter.geometry("1000x1000")
            window_Diesel_inter .state('zoomed')

            Diesel_inter_label = Label(window_Diesel_inter, text=" Diesel Inter in Filling Station", font=("time new roman", 30, "bold"), relief=GROOVE,
                                 height=2, width=50, bg="red", fg="white").pack(side=TOP,fill=X)

            text_label_day = Label(window_Diesel_inter, text="Enter DD").pack()
            text_enter_day = Entry(window_Diesel_inter).pack()
            # get_text_day = enter_day.get()

            text_label_Month = Label(window_Diesel_inter, text="Enter MM").pack()
            text_enter_Month = Entry(window_Diesel_inter).pack()
            # get_text_Month = enter_Month.get()

            text_label_year = Label(window_Diesel_inter, text="Enter YYYY").pack()
            text_enter_Year = Entry(window_Diesel_inter).pack()
            # get_text_year = enter_Year.get()

            text_label_liter = Label(window_Diesel_inter, text="Enter Diesel Amount in Liters").pack()
            text_enter_liter = Entry(window_Diesel_inter).pack()
            # get_text_liter = enter_liter.get()

            text_label_price = Label(window_Diesel_inter, text="Enter Purchasing Price").pack()
            text_enter_price = Entry(window_Diesel_inter).pack()
            # get_text_price = enter_price.get()

            making_button = Button(window_Diesel_inter, text="Save Data",   font=("time new roman", 10, "bold"),
                                   bg="red", fg="white", relief=GROOVE, height=1, width=7, command = lambda :
            [
                    Diesel_inter(text_enter_day.get(), text_enter_Month.get(),
                                 text_enter_Year.get(), text_enter_liter.get(), text_enter_price.get())
            ]).pack()
            window_Diesel_inter.mainloop()


        def read_Diesel_detal():
            read_Diesel_detal_window = Tk()
            read_Diesel_detal_window.title("Full Details of Diesel")
            # read_Diesel_detal_window.geometry("1000x1000")
            read_Diesel_detal_window.state('zoomed')

            making_text_box = Text(read_Diesel_detal_window, height=120, width=120, bg="Black", fg="White")

            read_petrol_detal_window_label = Label(read_Diesel_detal_window, text=" Full Details of Diesel",font=("time new roman", 30, "bold"), relief=GROOVE,
                                       height=2, width=50, bg="red", fg="white").pack(side=TOP,fill=X)

            read_petrol_detal_window_button = Button(read_Diesel_detal_window, text="Read Details", font=("time new roman", 10, "bold"), bg="red", fg="white", relief=GROOVE, height=1, width=15, command = lambda :
            [
                making_text_box.delete('1.0', 'end'),
                making_text_box.insert('end', read_D_C_T())
            ]).pack()

            making_text_box.pack()
            read_Diesel_detal_window.mainloop()


        def  D_S_F():
            D_S_F = Tk()
            D_S_F.title("Diesel Daily Salling")
            # D_S_F.geometry("1000x1000")
            D_S_F.state('zoomed')

            D_S_F_label = Label(D_S_F, text="Diesel Daily Salling ", font=("time new roman", 30, "bold"), relief=GROOVE, height=2, width=50, bg="red", fg="white").pack(side=TOP,fill=X)

            label_day = Label(D_S_F, text="Enter DD").pack()
            enter_day = Entry(D_S_F).pack()
            # get_text_day = enter_day.get()

            label_Month = Label(D_S_F, text="Enter MM").pack()
            enter_Month = Entry(D_S_F).pack()
            # get_text_Month = enter_Month.get()

            label_year = Label(D_S_F, text="Enter YYYY").pack()
            enter_Year = Entry(D_S_F).pack()
            # get_text_year = enter_Year.get()

            label_liter = Label(D_S_F, text="Enter Diesel Amount in Liters").pack()
            enter_liter = Entry(D_S_F).pack()
            # get_text_liter = enter_liter.get()

            label_price = Label(D_S_F, text="Enter Purchasing Price").pack()
            enter_price = Entry(D_S_F).pack()
            # get_text_price = enter_price.get()

            making_button = Button(D_S_F, text="Save Data",  font=("time new roman", 10, "bold"), bg="red", fg="white",
                                   relief=GROOVE, height=1, width=7, command=lambda: Diesel_D_S_I()).pack()

            D_S_F.mainloop()


        def D_S_R():
            D_S_R = Tk()
            D_S_R.title("Read Daily Salling Details")
            # D_S_R.geometry("1000x1000")
            D_S_R.state('zoomed')

            making_text_box_1 = Text(D_S_R, height=120, width=120, bg="Black", fg="White")

            D_S_R_label = Label(D_S_R, text=" Read Daily Salling Details",font=("time new roman", 30, "bold"), relief=GROOVE,
                                       height=2, width=50, bg="red", fg="white").pack(side=TOP,fill=X)

            D_S_R_button = Button(D_S_R, text="Read details", font=("time new roman", 10, "bold"), bg="red", fg="white", relief=GROOVE, height=1, width=15, command = lambda :
            [
                making_text_box_1.delete('1.0', 'end'), making_text_box_1.insert('end', read_D_S_i())]).pack()
            making_text_box_1.pack()
            D_S_R.mainloop()


        self.main_window.mainloop()