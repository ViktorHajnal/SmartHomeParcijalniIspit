import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from datetime import datetime

from fridge.fridge import SmartFridge
from meteo.meteo import Meteo

fridge = SmartFridge()
meteo = Meteo()

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Home")
        self.root.geometry("900x600")
        self.create_tabs()        
        
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
        self.groceries_text = tk.Text(tab, height=15, width=50)
        self.groceries_text.grid(column=0, row=1, padx=5, pady=5, columnspan=2)
        # Popunjavamo text field sa trenutnim podacima u bazi prilikom pokretanja programa
        self.update_groceries_list()
        
        # Create a button to add groceries
        add_button = ttk.Button(tab, text="Add Groceries", command=self.add_groceries)
        add_button.grid(column=0, row=2, padx=5, pady=5)

        # Create a button to remove groceries
        remove_button = ttk.Button(tab, text="Remove Groceries", command=self.remove_groceries)
        remove_button.grid(column=1, row=2, padx=5, pady=5)        

               
        
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
                       
        submit_button = tk.Button(self.entry_frame, text='Submit', command=self.submit_add_groceries)
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
                       
        submit_button = tk.Button(self.entry_frame, text='Submit', command=self.submit_remove_groceries)
        submit_button.grid(column=0, row=7, padx=5, pady=5)
        
        close_button = tk.Button(self.entry_frame, text='Close', command=self.close_add_remove_groceries)
        close_button.grid(column=1, row=7, padx=5, pady=5)
            
    def submit_add_groceries(self):
        self.item_name = self.entry_grocery_name.get() 
        self.item_quantity = abs(int(self.entry_grocery_qty.get())) #
        self.item_date = datetime.strptime(self.entry_grocery_date.get(), '%Y-%m-%d') #Moramo unositi u formatu YYYY-MM-DD
        
        self.entry_grocery_name.delete(0, tk.END)
        self.entry_grocery_qty.delete(0, tk.END)
        self.entry_grocery_date.delete(0, tk.END)
        
        fridge.add_grocery(name= self.item_name, quantity= self.item_quantity, expiration_date= self.item_date)
        self.update_groceries_list()
        
    
    def submit_remove_groceries(self):
        self.item_name = self.entry_grocery_name.get() 
        self.item_quantity = abs(int(self.entry_grocery_qty.get()))
        
        self.entry_grocery_name.delete(0, tk.END)
        self.entry_grocery_qty.delete(0, tk.END)
        
        fridge.remove_grocery(name= self.item_name, quantity=self.item_quantity)
        self.update_groceries_list()        
    
    def close_add_remove_groceries(self):
        self.entry_frame.destroy()

    def update_groceries_list(self):
        groceries = fridge.list_groceries()
        self.groceries_text.delete(1.0, tk.END)  # Clear the text widget           
        for item in groceries:
            self.groceries_text.insert(tk.END, f"{item.name}: {item.quantity} (Expires on: {item.expiration_date}\n)")
                    
    #Kreiranje labela za Meteo tab SmartHome aplikacije
    def labels_meteo(self, tab):
        # Frame za weather gdje pokazujemo tekstualno podatke o vanjskoj temp
        weather_frame = tk.Frame(self.tab2, highlightbackground='black', highlightthickness=1)
        weather_frame.grid(column=0, row=0, padx=5, pady=5, columnspan=1) 
        
        frame_name = ttk.Label(weather_frame, text="Trenutna vremenska situacija u Zagrebu", font=("Arial", 14, 'bold'))
        frame_name.grid(column=0, row=0, padx=5, pady=5)
        
        label_temp = ttk.Label(weather_frame, text=f"Trenutna temperatura zraka: {meteo.temp_zg_maksimir} °C", font=("Arial", 12))
        label_temp.grid(column=0, row=1, padx=5, pady=5)
        
        label_humi = ttk.Label(weather_frame, text=f"Trenutna vlažnost zraka: {meteo.humi_zg_maksimir} %", font=("Arial", 12))
        label_humi.grid(column=0, row=2, padx=5, pady=5)
        
        label_press = ttk.Label(weather_frame, text=f"Trenutni tlak zraka: {meteo.press_zg_maksimir} hPa", font=("Arial", 12))
        label_press.grid(column=0, row=3, padx=5, pady=5)
        
        label_text = ttk.Label(weather_frame, text=f"Trenutno vrijeme: {meteo.weather_text}", font=("Arial", 12))
        label_text.grid(column=0, row=4, padx=5, pady=5)
        
        # Frame za ikone gdje pokazujemo kako se treba obući vani
        weather_icon_frame = tk.Frame(self.tab2, highlightbackground='black', highlightthickness=1)
        weather_icon_frame.grid(column=1, row=0, padx=5, pady=5, columnspan=1) 
        
        label_temp = ttk.Label(weather_icon_frame, text="Prijedlog za oblačenje ukoliko se ide u van.", font=("Arial", 12))
        label_temp.grid(column=0, row=0, padx=5, pady=5)
        # Mora se napisati ovim redosljedom da bi se pokazivala sličica
        icon_photo_city = ImageTk.PhotoImage(meteo.icon_city_image)        
        icon_label_city = ttk.Label(weather_icon_frame, image=icon_photo_city) 
        icon_label_city.image = icon_photo_city
        icon_label_city.grid(column=0, row=1, padx=5, pady=5)
        
        # Frame za situaciju u kući
        house_frame = tk.Frame(self.tab2, highlightbackground='black', highlightthickness=1)
        house_frame.grid(column=0, row=1, padx=5, pady=5, columnspan=1) 
        
        frame_house_name = ttk.Label(house_frame, text="Trenutna vremenska situacija u kući", font=("Arial", 14, 'bold'))
        frame_house_name.grid(column=0, row=0, padx=5, pady=5)
        
        label_house_temp = ttk.Label(house_frame, text=f"Trenutna temperatura zraka: {meteo.temp_inside} °C", font=("Arial", 12))
        label_house_temp.grid(column=0, row=1, padx=5, pady=5)
        
        label_house_humi = ttk.Label(house_frame, text=f"Trenutna vlažnost zraka: {meteo.humi_inside} %", font=("Arial", 12))
        label_house_humi.grid(column=0, row=2, padx=5, pady=5)
        
        label_house_press = ttk.Label(house_frame, text=f"Trenutni tlak zraka: {meteo.press_inside} hPa", font=("Arial", 12))
        label_house_press.grid(column=0, row=3, padx=5, pady=5)
        
        # Frame za ikone gdje pokazujemo kako se treba obući u kući
        city_icon_frame = tk.Frame(self.tab2, highlightbackground='black', highlightthickness=1)
        city_icon_frame.grid(column=1, row=1, padx=5, pady=5, columnspan=1) 
        
        label_house_temp = ttk.Label(city_icon_frame, text="Prijedlog za oblačenje u kući.", font=("Arial", 12))
        label_house_temp.grid(column=0, row=0, padx=5, pady=5)
        # Mora se napisati ovim redosljedom da bi se pokazivala sličica
        icon_house_photo = ImageTk.PhotoImage(meteo.icon_house_image)        
        icon_label_house = ttk.Label(city_icon_frame, image=icon_house_photo) 
        icon_label_house.image = icon_house_photo
        icon_label_house.grid(column=0, row=1, padx=5, pady=5)
        

        

    