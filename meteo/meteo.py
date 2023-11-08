import requests
from bs4 import BeautifulSoup
from random import randint
from PIL import Image
from sqlalchemy import create_engine, Column, Integer, DateTime, func, Float, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
DATABASE_URL= "sqlite:///smart_home.db"

class MeteoInfo(Base):
    __tablename__ = 'meteoinfo'

    id = Column(Integer, primary_key=True)    
    date_reading = Column(DateTime, default=datetime.now())
    temp_zg_maksimir = Column(Float, nullable=False)
    temp_inside = Column(Float, nullable=False)
    temp_outside = Column(Float, nullable=False)
    humi_zg_maksimir = Column(Float, nullable=False)
    humi_inside = Column(Float, nullable=False)
    humi_outside = Column(Float, nullable=False)
    press_zg_maksimir = Column(Float, nullable=False)
    press_inside = Column(Float, nullable=False)
    press_outside = Column(Float, nullable=False)
    weather_text = Column(String)


class Meteo:
    def __init__(self) -> None:
        self.url = 'https://vrijeme.hr/hrvatska_n.xml'
        self.fetch_weather_data()
        self.simul_inside_outside()
        self.icons_city_temp_humi_press()
        self.icons_house_temp_humi_press()
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.add_sql_meteoinfo()
        
    def fetch_weather_data(self):        
        response = requests.get(self.url)

        if response.status_code == 200:
            xml_data = response.text.encode(encoding='UTF-8')
            soup = BeautifulSoup(xml_data, 'xml', from_encoding='UTF-8')
            cities = soup.find_all('Grad')
            self.temp_zg_maksimir = self.humi_zg_maksimir = self.press_zg_maksimir = None

            for city in cities:
                if city.find('GradIme').text.strip() == 'Zagreb-Maksimir':
                    self.temp_zg_maksimir = city.find('Temp').text.strip()
                    self.humi_zg_maksimir = city.find('Vlaga').text.strip()
                    self.press_zg_maksimir = city.find('Tlak').text.strip()
                    self.weather_text = city.find('Vrijeme').text.strip() #ovo iz nekog razloga ne čita č,ž,š makar je prebačeno na UTF-8
                    print(soup.original_encoding)
             
            
            #return self.temp_zg_maksimir, self.humi_zg_maksimir, self.press_zg_maksimir, self.weather_text
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    
    def simul_inside_outside(self):
        
        self.temp_inside = float(self.temp_zg_maksimir) + randint(5, 8) #Dižemo temperaturu u odnosu na gradsku
        self.humi_inside = float(self.humi_zg_maksimir) + (randint(-20, 20) / 10) #Mijenjamo vlažnost u odnosu na gradsku
        self.press_inside = float(self.press_zg_maksimir) + randint(20, 100) #Mijenjamo tlak u odnosu na gradsku
        self.temp_outside = float(self.temp_zg_maksimir) + randint(0, 3) #Dižemo temperaturu vani u odnosu na gradsku
        self.humi_outside = float(self.humi_zg_maksimir) + (randint(-10, 10) / 10) #Mijenjamo vlažnost vani u odnosu na gradsku
        self.press_outside = float(self.press_zg_maksimir) + randint(20, 40) #Mijenjamo tlak vani u odnosu na gradsku
        
    def icons_city_temp_humi_press(self):
        if float(self.temp_zg_maksimir) >= 28:
            self.icon_city_image =  Image.open('icons\icons8-shorts-100.png')  
        elif float(self.temp_zg_maksimir) >= 18:
            self.icon_city_image =  Image.open('icons\icons8-polo-shirt-100.png') 
        elif float(self.temp_zg_maksimir) >= 5:
            self.icon_city_image =  Image.open('icons\icons8-mens-hoodie-100.png')
        else:
            self.icon_city_image =  Image.open('icons\icons8-mitten-100.png')
        self.icon_city_image = self.icon_city_image.resize((60, 60))
    
    def icons_house_temp_humi_press(self):
        if float(self.temp_inside) >= 28:
            self.icon_house_image =  Image.open('icons\icons8-shorts-100.png')  
        elif float(self.temp_inside) >= 18:
            self.icon_house_image =  Image.open('icons\icons8-polo-shirt-100.png') 
        elif float(self.temp_inside) >= 5:
            self.icon_house_image =  Image.open('icons\icons8-mens-hoodie-100.png')
        else:
            self.icon_house_image =  Image.open('icons\icons8-mitten-100.png')
        self.icon_house_image = self.icon_house_image.resize((60, 60))
    
    def update_all(self):
        self.fetch_weather_data()
        self.simul_inside_outside()
        self.icons_city_temp_humi_press()
        self.icons_house_temp_humi_press()
        self.add_sql_meteoinfo()
        
    def add_sql_meteoinfo(self):
        session = self.Session()
        meteo_info = MeteoInfo(temp_zg_maksimir= float(self.temp_zg_maksimir),
                                temp_inside = float(self.temp_inside),
                                temp_outside = float(self.temp_outside),
                                humi_zg_maksimir = float(self.humi_zg_maksimir),
                                humi_inside = float(self.humi_inside),
                                humi_outside = float(self.humi_outside),
                                press_zg_maksimir = float(self.press_zg_maksimir),
                                press_inside = float(self.press_inside),
                                press_outside = float(self.press_outside),
                                weather_text = self.weather_text
                                )
        session.add(meteo_info)
        session.commit()
        session.close()



"""

if __name__ == "__main__":
    meteo = Meteo()
        
    print(f"Temperature: {meteo.temp_zg_maksimir} °C")    
    print(f"Temperature inside: {meteo.temp_inside} °C")
    print(f"Temperature outside: {meteo.temp_outside} °C")
    print(f"Humidity: {meteo.humi_zg_maksimir} %")
    print(f"Humidity inside: {meteo.humi_inside} %")
    print(f"Humidity outside: {meteo.humi_outside} %")
    print(f"Pressure: {meteo.press_zg_maksimir} hPa")
    print(f"Pressure inside: {meteo.press_inside} hPa")
    print(f"Pressure outside: {meteo.press_outside} hPa")
    print(f"Weather outside: {meteo.weather_text} hPa")"""
    
