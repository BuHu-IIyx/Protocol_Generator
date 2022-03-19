import tkinter as tk
from tkinter import ttk

from Controller.MainController import get_labs_list, get_customer_list, get_factors_list


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title("Производственный контроль")
        root.geometry("650x450+300+200")
        root.resizable(False, False)
        self.init_main_window()

    def lab_checked(self, event):
        self.combo_cust.configure(values=get_customer_list(self.combo_labs.get()), state='normal')

    def customer_checked(self, event):
        self.combo_factor.configure(values=get_factors_list(self.combo_cust.get()), state='normal')

    def factor_checked(self, event):
        self.show_button.configure(state='normal')
        self.create_button.configure(state='normal')

    def show_button_click(self):
        self.generate_tree(self.combo_factor.get())

    def generate_tree(self, factor):
        if factor == 'Шум':
            self.tree.configure(columns=('ID', 'area', 'source', 'nature', 'lvl', 'max_lvl'))
            self.tree.column('ID', width=30, anchor=tk.CENTER)
            self.tree.column('area', width=160, anchor=tk.CENTER)
            self.tree.column('nature', width=115, anchor=tk.CENTER)
            self.tree.column('source', width=115, anchor=tk.CENTER)
            self.tree.column('lvl', width=115, anchor=tk.CENTER)
            self.tree.column('max_lvl', width=115, anchor=tk.CENTER)

            self.tree.heading('ID', text='ID')
            self.tree.heading('area', text='Место\nизмерений')
            self.tree.heading('nature', text='Источник\nшума')
            self.tree.heading('source', text='Характер\nшума')
            self.tree.heading('lvl', text='Уровень\nзвука')
            self.tree.heading('max_lvl', text='Максимальный\nуровень звука')

        elif factor == 'Вибрация общая':
            self.tree.configure(columns=('ID', 'area', 'izm_params', 'result'))
            self.tree.column('ID', width=30, anchor=tk.CENTER)
            self.tree.column('area', width=160, anchor=tk.CENTER)
            self.tree.column('izm_params', width=115, anchor=tk.CENTER)
            self.tree.column('result', width=115, anchor=tk.CENTER)

            self.tree.heading('ID', text='ID')
            self.tree.heading('area', text='Место\nизмерений')
            self.tree.heading('izm_params', text='Наименование измеряемых\nпараметров')
            self.tree.heading('result', text='Результат\nизмерений')

        elif factor == 'Вибрация локальная':
            self.tree.configure(columns=('ID', 'area', 'izm_params', 'result'))
            self.tree.column('ID', width=30, anchor=tk.CENTER)
            self.tree.column('area', width=160, anchor=tk.CENTER)
            self.tree.column('izm_params', width=115, anchor=tk.CENTER)
            self.tree.column('result', width=115, anchor=tk.CENTER)

            self.tree.heading('ID', text='ID')
            self.tree.heading('area', text='Место\nизмерений')
            self.tree.heading('izm_params', text='Наименование измеряемых\nпараметров')
            self.tree.heading('result', text='Результат\nизмерений')

        self.tree.grid(column=0, row=4, columnspan=3)

    def init_main_window(self):
        self.toolbar = tk.Frame(bd=2)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        lab_list = get_labs_list()

        tk.Label(self.toolbar, text="Лаборатория:").grid(column=0, row=0)
        self.combo_labs = ttk.Combobox(self.toolbar)
        self.combo_labs.configure(values=lab_list)
        self.combo_labs.grid(column=1, row=0)
        self.combo_labs.bind("<<ComboboxSelected>>", self.lab_checked)

        tk.Label(self.toolbar, text="Организация:").grid(column=0, row=1)
        self.combo_cust = ttk.Combobox(self.toolbar, state='disabled')
        self.combo_cust.grid(column=1, row=1)
        self.combo_cust.bind("<<ComboboxSelected>>", self.customer_checked)

        tk.Label(self.toolbar, text="Производственный фактор:").grid(column=0, row=2)
        self.combo_factor = ttk.Combobox(self.toolbar, state='disabled')
        self.combo_factor.grid(column=1, row=2)
        self.combo_factor.bind("<<ComboboxSelected>>", self.factor_checked)

        self.show_button = ttk.Button(self.toolbar, text='Показать данные', state='disable', width=20,
                                      command=self.show_button_click)
        self.show_button.grid(column=2, row=1)

        self.create_button = ttk.Button(self.toolbar, text='Создать протокол', state='disable', width=20)
        self.create_button.grid(column=2, row=2)

        tk.Label(self.toolbar, text="").grid(column=0, row=3)

        self.tree = ttk.Treeview(self.toolbar, height=15, show='headings')
