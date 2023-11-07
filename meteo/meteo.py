import requests
from bs4 import BeautifulSoup


class Meteo:
    def __init__(self) -> None:
        self.url = 'https://vrijeme.hr/hrvatska_n.xml'
        
    def fetch_weather_data(self):        
        response = requests.get(self.url)

        if response.status_code == 200:
            xml_data = response.text
            soup = BeautifulSoup(xml_data, 'xml')
            cities = soup.find_all('Grad')
            self.temp_zg_maksimir = self.humi_zg_maksimir = self.press_zg_maksimir = None

            for city in cities:
                if city.find('GradIme').text.strip() == 'Zagreb-Maksimir':
                    self.temp_zg_maksimir = city.find('Temp').text.strip()
                    self.humi_zg_maksimir = city.find('Vlaga').text.strip()
                    self.press_zg_maksimir = city.find('Tlak').text.strip()
             
            
            return self.temp_zg_maksimir, self.humi_zg_maksimir, self.press_zg_maksimir
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

if __name__ == "__main__":
    meteo = Meteo()
    meteo.fetch_weather_data()    
        
    print(f"Temperature: {meteo.temp_zg_maksimir} °C")
    print(f"Humidity: {meteo.humi_zg_maksimir} %")
    print(f"Pressure: {meteo.press_zg_maksimir} hPa")
