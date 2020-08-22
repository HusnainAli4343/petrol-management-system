from tkinter import *
from cPetrol import petrol_daily_selling_details


class petrol_daily_selling_details:
    def __init__(self):
        pertol_daily_selling_details = Tk()
        pertol_daily_selling_details.title("Read Daily selling Details")
        pertol_daily_selling_details.state('zoomed')

        making_text_box_1 = Text(pertol_daily_selling_details, height=120, width=120, bg="Black", fg="White")

        D_S_R_label = Label(pertol_daily_selling_details, text=" Read Daily selling Details",
                            font=("time new roman", 30, "bold"), relief=GROOVE, height=2,
                            width=50, bg="red", fg="white").pack(side=TOP, fill=X)

        D_S_R_button = Button(pertol_daily_selling_details, text="Read details", font=("time new roman", 10, "bold"),
                              bg="red", fg="white", relief=GROOVE, height=1, width=15, command=lambda:
            [
                making_text_box_1.delete('1.0', 'end'),
                making_text_box_1.insert('end', petrol_daily_selling_details)])
        D_S_R_button.pack()
        making_text_box_1.pack()
        pertol_daily_selling_details.mainloop()


# obj = petrol_daily_selling_details()