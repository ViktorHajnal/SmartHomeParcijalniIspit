import tkinter as tk
from gui.gui import GUI
from fridge.fridge import SmartFridge

def main():
    
    fridge = SmartFridge()  
    root = tk.Tk()
    GUI(root)  
    root.mainloop()
    
    
    
if __name__ == '__main__':
    main()