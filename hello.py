from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import requests
from bs4 import BeautifulSoup


class MainWidget(BoxLayout):
    label_1 = ObjectProperty()
    label_2 = ObjectProperty()
    def say_hello(self):
        with requests.Session() as se:
            se.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "*/*",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
            }


        url = 'https://www.onlinetrade.ru/catalogue/videokarty-c338/?price1=3099&price2=971100&graphic_processor[]=NVIDIA%20GeForce%20RTX%203060&advanced_search=1&rating_active=0&special_active=1&selling_active=1&producer_active=1&price_active=0&proizvoditel_vid_active=0&line_active=1&graphic_processor_active=1&naznachenie_active=1&memory_size_active=1&memory_type_active=1&bus_active=0&dop_pitanie_active=1&cooling_mode_active=1&ventilyatori_active=1&rekom_power_active=1&podsvetka_active=0&dlina_active=0&low_profile_active=0&kol_slots_active=0&sockets_active=0&srok_garantii_active=0&cat_id=338'
        response = se.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_='price regular js__actualPrice')
        c1 = 100000000000000
        for quote in quotes:
            c = quote.text.replace(' ', '')
            c = c.replace('\n', '')
            c = c.replace('₽','')
            if c1>int(c):
                c1 = int(c)
        self.label_1.text = "ОНЛАЙН ТРЕЙД - " + str(c1)+"₽"
        
        with requests.Session() as se:
            se.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "*/*",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
            }


        url = 'https://www.citilink.ru/catalog/videokarty/?f=rating.any%2C9368_29nvidiad1d1geforced1rtxd13060&pf=rating.any&sorting=price_asc'
        response = se.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')

        for quote in quotes:
            c = quote.text.replace(' ', '')
            self.label_2.text ="Ситилинк - " + c.replace('\n', '')+"₽"
            break


class MainApp(App):

    def build(self):
        return MainWidget()


if __name__ == '__main__':
    app = MainApp()
    app.run()