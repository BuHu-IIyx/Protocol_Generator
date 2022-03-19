from Model.Company import Company
from Model.Protocol import generate_protocol
from Model.testInit import lab_ini, customer_ini
from View.MainWindow import MainWindow
import tkinter as tk

lab = lab_ini()
customer = customer_ini()
company = Company()
company.add_laboratories(lab)
company.add_customers(customer)
generate_protocol(lab, customer, "20 февраля 2022 г.", "14.02.2022 г.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainWindow(root)
#     app.pack()
#     root.mainloop()


