import os, geepeeteeekonomisti as gptEkonomisti, ekonomistikone

def main():
    tulostaOhje()

    # Haetaan väitteet/kysymykset ekonomistikone.fi -saitilta
    _ekonomistikone = ekonomistikone.Ekonomistikone()
    promptit = _ekonomistikone.haeKysymykset()

    # Annetaan kehotteet GeePeeTeeEkonimistille narskuteltavaksi
    _geePeeTeeEkonomisti = gptEkonomisti.GeePeeTeeEkonomisti()

    # Helpperi, johon kerätään vastaukset
    vastaukset = ''

    kysyGPTEkonomistilta(promptit, _geePeeTeeEkonomisti, vastaukset)


def kysyGPTEkonomistilta(promptit, _geePeeTeeEkonomisti, vastaukset):
    for väite, aihe in promptit.items():
        _title = 'Väite: ' + väite + ' (' + aihe + ')' + '\n'
        check = tarkistaOnkoJoKysytty(_title)
        if not check:
            _title += '\nChatGPT vastaa: '
            print(_title)
            vastaukset += _title
            response = _geePeeTeeEkonomisti.kysyGeePeeTeeEkonomistilta(väite)
            _vastaus = response["choices"][0]["message"]["content"] + '\n'
            _vastaus += '-' * 100 + '\n'
            print(_vastaus)
            vastaukset += _vastaus
    
            f = open('vastaukset.txt', "a", encoding = 'utf-8')
            f.write(vastaukset)
            f.close

def tarkistaOnkoJoKysytty(väite):
    with open('vastaukset.txt', 'r', encoding = 'utf-8') as f:
        rivit = f.readlines()
        for rivi in rivit:
            if väite in rivi:
                return True
    return False

def tulostaOhje():
    os.system('cls')
    print('=' * 100)
    print('ChatGPT vastailee ekonomistikone.fi:n väittämiin ekonomistin roolissa.')
    print('Sille esitetään www.ekonomistikone.fi:ssä olevia väittämiä, joihin suomalaiset ekonomistit ovat ottaneet sivustolla kantaa.')
    print()
    print('ChatGPT antaa väittämään vastauksensa alla olevalla asteikolla ja lisäksi siltä pyydetään vastaukselleen perusteluja.')
    print('ChatGPT:tä käsketään myös kertomaan, millä taloustieteellisellä mallilla se vastauksensa hahmottelee ja kuka on mallin tunnetuin kehittäjä.')
    print()
    print('Asteikko:')
    print('     1 = Vahvasti samaa mieltä,')
    print('     2 = Samaa mieltä,')
    print('     3 = Epävarma,')
    print('     4 = Eri mieltä,')
    print('     5 = Vahvasti eri mieltä,')
    print('     0 = Ei mielipidettä.')
    print('=' * 100)

if __name__ == "__main__":
    main()