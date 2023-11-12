from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sql.sql_conn import Sql

Base = declarative_base()

class GroceryInventory(Base):
    __tablename__ = 'groceryinventory'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    date_in_out = Column(DateTime, default=datetime.now())
    expiration_date = Column(DateTime)

class SmartFridge:
    def __init__(self):
        self.sql = Sql()
        self.session = self.sql.session()

    def add_grocery(self, name, quantity, expiration_date=None):
        session = self.session
        grocery_item = GroceryInventory(name=name, quantity=quantity, expiration_date=expiration_date)
        session.add(grocery_item)
        session.commit()
        session.close()

    def remove_grocery(self, name, quantity):
        session = self.session
        grocery_items = session.query(GroceryInventory).filter_by(name=name).order_by(GroceryInventory.date_in_out).all()
        total_item_quantity = session.query(func.sum(GroceryInventory.quantity)).filter_by(name=name).scalar()
        
        #FIFO metoda micanja van itema iz inventorya. Za svaki item provjeravamo stanje i mičemo do 0 dokle god ima količine koju mičemo.
        removed_quantity = 0
        if total_item_quantity < quantity:
            print(f'Currently in inventory {total_item_quantity}. Cannot remove more than in inventory.')
        else:
            for item in grocery_items:
                if item.quantity <= (quantity - removed_quantity):
                    removed_quantity += item.quantity
                    item.quantity = 0
                else:
                    item.quantity -= (quantity - removed_quantity) 
                    break               
            
        session.commit()
        session.close()
        
    def list_groceries(self):
        session = self.session
        #Pokazujemo samo one iteme koji imaju količinu veću od 0 
        groceries = session.query(GroceryInventory).filter(GroceryInventory.quantity > 0).order_by(GroceryInventory.expiration_date).all()
        session.close()
        return groceries

    
   