import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home")
        self.root.geometry("900x600")
        self.create_tabs()
    #Kreianje koliko tabova nam treba
    def create_tabs(self):
        tab_control = ttk.Notebook(self.root)

        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)

        tab_control.add(tab1, text='Overview')
        tab_control.add(tab2, text='Meteo')

        tab_control.pack(expand=1, fill='both')

        self.labels_overview(tab1)
        self.labels_meteo(tab2)
    #Kreiranje labela za overview tab SmartHome applikacije
    def labels_overview(self, tab):
        label1 = ttk.Label(tab, text="Label 1", font=("Helvetica", 12))
        label1.grid(column=0, row=0, padx=5, pady=5)

        label2 = ttk.Label(tab, text="Label 2", font=("Helvetica", 12))
        label2.grid(column=0, row=1, padx=5, pady=5)

        label3 = ttk.Label(tab, text="Label 3", font=("Helvetica", 12))
        label3.grid(column=1, row=0, padx=5, pady=5)

        label4 = ttk.Label(tab, text="Label 4", font=("Helvetica", 12))
        label4.grid(column=1, row=1, padx=5, pady=5)
    #Kreiranje labela za Meteo tab SmartHome aplikacije
    def labels_meteo(self, tab):
        label1 = ttk.Label(tab, text="Label 1", font=("Helvetica", 12))
        label1.grid(column=0, row=0, padx=5, pady=5)

        label2 = ttk.Label(tab, text="Label 2", font=("Helvetica", 12))
        label2.grid(column=0, row=1, padx=5, pady=5)
        
        object1_text = "Object 1 Text"
        object2_text = "Object 2 Text"
        object3_text = "Object 3 Text"

        label_object1 = ttk.Label(tab, text=object1_text, font=("Helvetica", 12))
        label_object1.grid(column=1, row=0, padx=10, pady=10)

        label_object2 = ttk.Label(tab, text=object2_text, font=("Helvetica", 12))
        label_object2.grid(column=1, row=1, padx=10, pady=10)

        label_object3 = ttk.Label(tab, text=object3_text, font=("Helvetica", 12))
        label_object3.grid(column=1, row=2, padx=10, pady=10)


