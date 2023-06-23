# python-gpt-meets-ekonomistikone

## ChatGPT tapaa ekonomistikoneen
Ohjelma noutaa suomalaisille ekonomisteille esitettyjä väittämiä sivustolta ekonomistikone.fi ja syöttää väittämät ChatGPT-mallille. ChatGPT antaa väittämään vastauksensa ja kertoo mielipiteensä.

### Vastaus
ChatGPT antaa väittämään vastauksen asteikolla 1-5, jossa 1 = Vahvasti samaa mieltä ja 5 = Vahvasti eri mieltä. GPT-mallia kehotetaan antamaan vastaukseensa myös perustelut sekä mahdollinen taloustieteellinen malli, jolla se voisi vastausta arvioida. Lisäksi siltä pyydetään viite taloustieteellisen mallin tunnetuimpiin kehittäjiin. GPT-mallia kehotetaan antamaan vastauksena myös "0=Ei mielipidettä", jos se ei tiedä.

### Vastauksen muoto
Vastauksen muoto määritellään api-kutsussa:
messages = [{"role":"system","content":"Olet suomalainen ekonomisti. Kerro mielipiteesi seuraaviin väittämiin asteikolla 1-5, jossa 1=Vahvasti samaa mieltä, 2=Samaa mieltä, 3=Epävarma, 4=Eri mieltä, 5=Vahvasti eri mieltä. Voit myös vastata 0=Ei mielipidettä. Anna perustelut väitteellesi ja arvioi vastausta parhaan taloustieteellisen mallin avulla. Kerro myös, kuka on mallin tunnetuin kehittäjä. Jos et tiedä vastausta, niin sano 0=Ei mielipidettä."},
                        {"role":"user","content": prompt},
                        {"role":"assistant","content":"{Mielipide]. Ekonomistit ovat usein erimielisiä valitusoikeuden rajoittamisen vaikutuksista maankäyttöasioissa, koska {perustelut}.\nPerustelut johonkin taloustieteelliseen malliin perustuen, mikäli mahdollista {taloustieteellinen malli}.\n{Mallin tunnetuimmat kehittäjät}."}

## Asennus
Asenna tarvittavat kirjastot komennolla
pip install -r requirements.txt

Korvaa GeePeeTeeEkonomisti-luokassa muuttujat omilla tiedoillasi:
- openai.api_type = "azure". Sovellus käyttää lähtökohtaisesti azuressa sijaitsevaa palvelua.
- os.getenv("OPENAI_API_ENDPOINT"). Korvaa tämä omalla endpointilla tai tee ympäristömuuttuja nimellä OPENAI_API_ENDPOINT ja lisää sinne endpointisi.
- os.getenv("OPENAI_API_KEY"). Korvaa tämä gpt-mallisi api-avaimella tai tee ympäristömuuttuja nimellä OPENAI_API_KEY ja lisää sinne avaimesi.
- os.getenv("OPENAI_API_ENGINE"). Korvaa tämä azureen tehdyn mallin nimellä tai tee ympäristömuuttuja nimellä OPENAI_API_ENGINE ja lisää sinne mallisi nimi.

## Ohjelman kulku
1) Ohjelma noutaa sivustolta ekonmistikone.fi väitteet
2) Tarkistaa, ovatko väitteet jo vastaukset.txt -tiedostossa
3) Syöttää väitteet, joita ei löydy jo vastaukset.txt:Stä, gpt-3.5-turbo -mallille
4) Tulostaa GPT-mallin vastauksen ja lisää tiedot vastaukset.txt-tiedostoon

## Tunnetut puutteet
- Sovellus ei hae väittämiä sivutetuilta sivuilta, paitsi ensimmäisellä sivulla näkyvät väittämät
- ChatGPT tunnetusti hallusinoi, joten vastaukset on syytä tarkistaa kriittisellä silmällä.
