import requests
from bs4 import BeautifulSoup

base_url = 'https://www.ekonomistikone.fi'
aiheet_url = base_url + '/aiheet/'


class Ekonomistikone():

    def haeKysymykset(url = aiheet_url):
        väiteDic = {}

        # Lähetä HTTP GET -pyyntö aiheet-sivulle
        response = requests.get(aiheet_url)

        # Tarkista, että pyyntö onnistui
        if response.status_code == 200:
            # Käytä BeautifulSoupia sivun analysointiin
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Etsi kaikki aihe-linkit sivulta
            aihe_linkit = soup.find_all('a', class_='tag-cloud-link')
            
            # Käy läpi jokainen aihe-linkki
            for linkki in aihe_linkit:
                aihe = linkki.string

                # Korjataan epäloogisuus
                if(aihe == "Omistajapolitiikka"):
                    aihe = "omistaja-politiikka"
                
                # Lähetä HTTP GET -pyyntö aiheen alasivulle
                aihe_response = requests.get(base_url + '/tag/' + aihe
                                            .replace(' ', '-') # lisätään väliviiva urliin
                                            .replace('ä', 'a') # poistetaan ääkköset urleista
                                            .replace('ö', 'o')
                                            )
                
                # Tarkista, että pyyntö onnistui
                if aihe_response.status_code == 200:
                    # Käytä BeautifulSoupia aiheen sivun analysointiin
                    aihe_soup = BeautifulSoup(aihe_response.text, 'html.parser')
                    
                    # Etsi kaikki artikkelit aihesivulta
                    artikkelit = aihe_soup.find_all('article')
                    
                    # Tulosta löydetyt kysymykset
                    for artikkeli in artikkelit:
                        title = artikkeli.find("h2")
                        väiteDic[title.string] = aihe
                        #print('Aihe: ' + aihe + '. Väite: ' + title.string)
                else:
                    print('Virhe: Pyyntö aiheen alasivulle epäonnistui, statuskoodi', aihe_response.status_code)
        else:
            print('Virhe: Pyyntö aiheet-sivulle epäonnistui, statuskoodi', response.status_code)
        return väiteDic
