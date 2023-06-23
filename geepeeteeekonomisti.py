import os
import openai

class GeePeeTeeEkonomisti():
    openai.api_type = "azure"
    openai.api_base = os.getenv("OPENAI_API_ENDPOINT")
    openai.api_version = "2023-03-15-preview"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    api_engine = os.getenv("OPENAI_API_ENGINE")

    def kysyGeePeeTeeEkonomistilta(self, prompt):
        '''
            kysyGeePeeTeeEkonomistilta saa parametrina kehotteen, jonka se lähettää gpt3.5 -keinoälylle.
            Keinoäly antaa vastauksen asteikolla 1-5, jossa
                1 = Vahvasti samaa mieltä,
                2 = Samaa mieltä,
                3 = Epävarma,
                4 = Eri mieltä,
                5 = Vahvasti eri mieltä,
                0 = Ei mielipidettä.
            Lisäksi GeePeeTeeEkonomisti perustelee vastauksensa.
        '''
        response = openai.ChatCompletion.create(
            engine = self.api_engine,
            messages = [{"role":"system","content":"Olet suomalainen ekonomisti. Kerro mielipiteesi seuraaviin väittämiin asteikolla 1-5, jossa 1=Vahvasti samaa mieltä, 2=Samaa mieltä, 3=Epävarma, 4=Eri mieltä, 5=Vahvasti eri mieltä. Voit myös vastata 0=Ei mielipidettä. Anna perustelut väitteellesi ja arvioi vastausta parhaan taloustieteellisen mallin avulla. Kerro myös, kuka on mallin tunnetuin kehittäjä. Jos et tiedä vastausta, niin sano 0=Ei mielipidettä."},
                        {"role":"user","content": prompt},
                        {"role":"assistant","content":"{Mielipide]. Ekonomistit ovat usein erimielisiä valitusoikeuden rajoittamisen vaikutuksista maankäyttöasioissa, koska {perustelut}.\nPerustelut johonkin taloustieteelliseen malliin perustuen, mikäli mahdollista {taloustieteellinen malli}.\n{Mallin tunnetuimmat kehittäjät}."}
                        ],
            temperature=0.1,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)

        return response