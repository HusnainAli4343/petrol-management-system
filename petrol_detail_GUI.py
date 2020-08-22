from tkinter import *
from cPetrol import read_total_petrol_amount


class read_petrol_details:
    def __init__(self):
        self.read_petrol_detail_window = Tk()
        self.read_petrol_detail_window.title("Full Details of Petrol")
        self.read_petrol_detail_window.state('zoomed')

        making_text_box = Text(self.read_petrol_detail_window, height=120, width=120, bg="Black", fg="White")

        read_petrol_detal_window_label = Label(self.read_petrol_detail_window, text=" Full Details of Petrol",
                                               font=("time new roman", 30, "bold"), relief=GROOVE, height=2, width=50,
                                               bg="red", fg="white").pack(side=TOP, fill=X)

        read_petrol_detal_window_button = Button(self.read_petrol_detail_window, text="Read Details",
                                                 font=("time new roman", 10, "bold"), bg="red", fg="white", relief=GROOVE,
                                                 height=1, width=15, command=lambda: read_total_petrol_amount()).pack()

        making_text_box.pack()
        self.read_petrol_detail_window.mainloop()


# obj = read_petrol_details()