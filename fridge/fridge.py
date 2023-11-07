from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()
DATABASE_URL= "sqlite:///smart_home.db"

class GroceryInventory(Base):
    __tablename__ = 'groceryinventory'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    date_in_out = Column(DateTime, default=datetime.now())
    expiration_date = Column(DateTime)

class SmartFridge:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_grocery(self, name, quantity, expiration_date=None):
        session = self.Session()
        grocery_item = GroceryInventory(name=name, quantity=quantity, expiration_date=expiration_date)
        session.add(grocery_item)
        session.commit()
        session.close()

    def remove_grocery(self, name, quantity):
        session = self.Session()
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
        session = self.Session()
        #Pokazujemo samo one iteme koji imaju količinu veću od 0 
        groceries = session.query(GroceryInventory).filter(GroceryInventory.quantity > 0).order_by(GroceryInventory.expiration_date).all()
        session.close()
        return groceries

    def close(self):
        self.engine.dispose()
        
"""
if __name__ == "__main__":
    database_url = "sqlite:///smart_home.db"
    fridge = SmartFridge(database_url)

    # Add groceries to the fridge
    fridge.add_grocery("Milk", 6, datetime.now() + timedelta(days=5))
    fridge.add_grocery("Eggs", 12, datetime.now() + timedelta(days=7))
    fridge.add_grocery("Apples", 6, datetime.now() + timedelta(days=3))

    # Remove a specific quantity of a grocery from the fridge
    fridge.remove_grocery("Milk", 4)

    # List the available groceries in the fridge by closest expiration date
    groceries_in_fridge = fridge.list_groceries()
    for item in groceries_in_fridge:
        print(f"{item.name}: {item.quantity} (Expires on: {item.expiration_date})")

    # Close the fridge
    fridge.close()
"""