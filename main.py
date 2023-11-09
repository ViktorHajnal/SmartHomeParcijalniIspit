import tkinter as tk
from gui.gui import GUI
from fridge.fridge import SmartFridge
from sql.sql_conn import Sql

def main():
    root = tk.Tk()
    sql = Sql()
    GUI(root)  
    root.mainloop()
    sql.close_session()

if __name__ == '__main__':
    main()