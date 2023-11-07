
import tkinter as tk

from gui.gui import GUI
from fridge.fridge import SmartFridge

def main():
    
    fridge = SmartFridge()   
    """for item in fridge.list_groceries():
        print(f"{item.name}: {item.quantity} (Expires on: {item.expiration_date})")"""
    root = tk.Tk()
    GUI(root)
    
  
     
    root.mainloop()
    fridge.close()
if __name__ == '__main__':
    main()