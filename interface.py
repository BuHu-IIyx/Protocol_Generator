import tkinter as tk
from tkinter import ttk


def interface(labs, customers, experts, measuring, methodologies):
    app = tk.Tk()
    label_lab = tk.Label(app, text="Выберите лабораторию:")
    label_lab.grid(column=0, row=0)
    combo_labs = ttk.Combobox(app, values=labs)
    combo_labs.grid(column=0, row=1)
    label_cust = tk.Label(app, text="Выберите организацию:")
    label_cust.grid(column=0, row=2)
    combo_cust = ttk.Combobox(app, values=customers)
    combo_cust.grid(column=0, row=3)
    label_zam = tk.Label(app, text="Выберите замерщика:")
    label_zam.grid(column=0, row=4)
    combo_zam = ttk.Combobox(app, values=experts)
    combo_zam.grid(column=0, row=5)
    label_oformit = tk.Label(app, text="Выберите оформителя:")
    label_oformit.grid(column=0, row=6)
    combo_oformit = ttk.Combobox(app, values=experts)
    combo_oformit.grid(column=0, row=7)
    label_measuring = tk.Label(app, text="Выберите приборы:")
    label_measuring.grid(column=0, row=8)
    combo_measuring = ttk.Combobox(app, values=measuring)
    combo_measuring.grid(column=0, row=9)
    label_methodologies = tk.Label(app, text="Выберите методики:")
    label_methodologies.grid(column=0, row=10)
    combo_methodologies = ttk.Combobox(app, values=methodologies)
    combo_methodologies.grid(column=0, row=11)

    app.mainloop()

# , customers, experts, measuring, methodologies