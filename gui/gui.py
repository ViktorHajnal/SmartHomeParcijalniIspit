import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self, root, groceries):
        self.root = root
        self.root.title("Smart Home")
        self.root.geometry("900x600")
        self.create_tabs()
        self.groceries = groceries
        
    #Kreianje koliko tabova nam treba
    def create_tabs(self):
        tab_control = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(tab_control)
        self.tab2 = ttk.Frame(tab_control)

        tab_control.add(self.tab1, text='Fridge')
        tab_control.add(self.tab2, text='Meteo')

        tab_control.pack(expand=1, fill='both')

        self.labels_fridge(self.tab1)
        self.labels_meteo(self.tab2)
    #Kreiranje labela za overview tab SmartHome applikacije
    def labels_fridge(self, tab):
        
        # Create a label for groceries list
        groceries_label = ttk.Label(tab, text="Groceries:")
        groceries_label.grid(column=0, row=0, padx=5, pady=5, columnspan=2)

        # Create a text widget to display groceries
        groceries_text = tk.Text(tab, height=10, width=40)
        groceries_text.grid(column=0, row=1, padx=5, pady=5, columnspan=2)

        # Create a button to add groceries
        add_button = ttk.Button(tab, text="Add Groceries", command=self.add_groceries)
        add_button.grid(column=0, row=2, padx=5, pady=5)

        # Create a button to remove groceries
        remove_button = ttk.Button(tab, text="Remove Groceries", command=self.remove_groceries)
        remove_button.grid(column=1, row=2, padx=5, pady=5)
        

        self.groceries_text = groceries_text  # Store a reference to the text widget
        self.update_groceries_list()
        
    def add_groceries(self):
        self.entry_frame = tk.Frame(self.tab1, highlightbackground='black', highlightthickness=1)
        self.entry_frame.grid(column=0, row=3, padx=5, pady=5, columnspan=2)       
        
        frame_name = tk.Label(self.entry_frame, text="Enter required information", width=25)
        frame_name.grid(column=0, row=3, padx=5, pady=5)
        
        label_grocery_name = tk.Label(self.entry_frame, text="Grocery name", width=20)
        label_grocery_name.grid(column=0, row=4, padx=5, pady=5)
        
        self.entry_grocery_name = tk.Entry(self.entry_frame, width=25)
        self.entry_grocery_name.grid(column=1, row=4, padx=5, pady=5)
        
        label_grocery_qty = tk.Label(self.entry_frame, text="Grocery amount", width=20)
        label_grocery_qty.grid(column=0, row=5, padx=5, pady=5)
        
        self.entry_grocery_qty = tk.Entry(self.entry_frame, width=25)
        self.entry_grocery_qty.grid(column=1, row=5, padx=5, pady=5)
        
        label_grocery_date = tk.Label(self.entry_frame, text="Grocery expiry date", width=20)
        label_grocery_date.grid(column=0, row=6, padx=5, pady=5)
        
        self.entry_grocery_date = tk.Entry(self.entry_frame, width=25)
        self.entry_grocery_date.grid(column=1, row=6, padx=5, pady=5)        
                       
        submit_button = tk.Button(self.entry_frame, text='Submit', command=self.submit_add_remove_groceries)
        submit_button.grid(column=0, row=7, padx=5, pady=5)
        
        close_button = tk.Button(self.entry_frame, text='Close', command=self.close_add_remove_groceries)
        close_button.grid(column=1, row=7, padx=5, pady=5)
            
    def remove_groceries(self):
        self.entry_frame = tk.Frame(self.tab1, highlightbackground='black', highlightthickness=1)
        self.entry_frame.grid(column=0, row=3, padx=5, pady=5, columnspan=2)       
        
        frame_name = tk.Label(self.entry_frame, text="Enter required information", width=25)
        frame_name.grid(column=0, row=3, padx=5, pady=5)
        
        label_grocery_name = tk.Label(self.entry_frame, text="Grocery name", width=20)
        label_grocery_name.grid(column=0, row=4, padx=5, pady=5)
        
        self.entry_grocery_name = tk.Entry(self.entry_frame, width=25)
        self.entry_grocery_name.grid(column=1, row=4, padx=5, pady=5)
        
        label_grocery_qty = tk.Label(self.entry_frame, text="Grocery amount", width=20)
        label_grocery_qty.grid(column=0, row=5, padx=5, pady=5)
        
        self.entry_grocery_qty = tk.Entry(self.entry_frame, width=25)
        self.entry_grocery_qty.grid(column=1, row=5, padx=5, pady=5)     
                       
        submit_button = tk.Button(self.entry_frame, text='Submit', command=self.submit_add_remove_groceries)
        submit_button.grid(column=0, row=7, padx=5, pady=5)
        
        close_button = tk.Button(self.entry_frame, text='Close', command=self.close_add_remove_groceries)
        close_button.grid(column=1, row=7, padx=5, pady=5)
            
    def submit_add_remove_groceries(self):
        self.item_name = self.entry_grocery_name.get() 
        self.item_quantity = abs(int(self.entry_grocery_qty.get()))
        self.item_date = self.entry_grocery_date.get()
        
        self.entry_grocery_name.delete(0, tk.END)
        self.entry_grocery_qty.delete(0, tk.END)
        self.entry_grocery_date.delete(0, tk.END)
        
        self.update_groceries_list()
        
        return self.item_name, self.item_quantity, self.item_date
    
    def close_add_remove_groceries(self):
        self.entry_frame.destroy()

    def update_groceries_list(self, self.groceries):
        
        self.groceries_text.delete(0, tk.END)  # Clear the text widget           
        for item in self.groceries:
            self.groceries_text.insert(tk.END, f"{item.name}: {item.quantity} (Expires on: {item.expiration_date}\n)")

        
    #Kreiranje labela za Meteo tab SmartHome aplikacije
    def labels_meteo(self, tab):
        label1 = ttk.Label(tab, text="Label 1")
        label1.grid(column=0, row=0, padx=5, pady=5)

        label2 = ttk.Label(tab, text="Label 2")
        label2.grid(column=0, row=1, padx=5, pady=5)
        
        object1_text = "Object 1 Text"
        object2_text = "Object 2 Text"
        object3_text = "Object 3 Text"

        label_object1 = ttk.Label(tab, text=object1_text)
        label_object1.grid(column=1, row=0, padx=10, pady=10)

        label_object2 = ttk.Label(tab, text=object2_text)
        label_object2.grid(column=1, row=1, padx=10, pady=10)

        label_object3 = ttk.Label(tab, text=object3_text)
        label_object3.grid(column=1, row=2, padx=10, pady=10)


    