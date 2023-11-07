
import tkinter as tk

from gui.gui import GUI
from fridge.fridge import SmartFridge

def main():
    database_url = "sqlite:///smart_home.db"
    fridge = SmartFridge(database_url)    
    groceries_list = fridge.list_groceries()
    root = tk.Tk()
    GUI(root, groceries= groceries_list)
      
    
    root.mainloop()
    fridge.close()
if __name__ == '__main__':
    main()