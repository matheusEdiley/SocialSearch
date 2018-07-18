# -*- coding: utf-8 -*-
from instagram.client import InstagramAPI
from TratarTexto import *

class InstagramConn(object):

    """description of class"""
    MAX_TWEETS = 10  # A API só retorna 100 tweets em uma consulta.
    BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"
    client_id = 'e11a4d95154c487ea457eea9288068b0'
    client_secret = '737a73555b784345b2e12665be0cd3d3'
    access_token = '2149654552.5b9e1e6.76d7c9a9e0c541e0bf30abe1ffa5d7a6'
    client_ip = '200.15.1.1'

    def __init__(self):
        self.api = InstagramAPI()
        self.api = InstagramAPI(client_id=self.client_id,
                                client_secret=self.client_secret, access_token=self.access_token)
    
    def BuscarResultados(self, query, qtd,polaridade):
        ''' BuscarResultados(text) -> string
         A api irá buscar pela tag referenciada abaixo,limitando a pesquisa
         de acordo com o contador tag_recent_media retorna duas variáveis,
         o id do post e o texto 
         
         return string
         '''
        aux = query

        recent_media, next = self.api.tag_recent_media(
            tag_name=aux, count=qtd)
        wordF = ""
        tratarText = TratarTexto()
        lista = {}
        for media in recent_media:
            if polaridade == "Todos":
                print media.caption.text + '    | Polaridade: ' + tratarText.SentimentalAnalysis(media.caption.text) + '| '
                print '---------------------------------------------------------'
                wordF += tratarText.RetiraStopWords(tratarText.RetirarLinks(media.caption.text))
                lista.update({media.caption.text: tratarText.SentimentalAnalysis(media.caption.text)})
            else: 
                if polaridade == tratarText.SentimentalAnalysis(media.caption.text):
                    print media.caption.text + '    | Polaridade: ' + tratarText.SentimentalAnalysis(media.caption.text) + '| '
                    print '---------------------------------------------------------'
                    wordF += tratarText.RetiraStopWords(tratarText.RetirarLinks(media.caption.text))
                    lista.update({media.caption.text: tratarText.SentimentalAnalysis(media.caption.text)})
        wordF = tratarText.NormalizarTexto(wordF.encode('utf-8'))
        print "\nPalavras mais frequentes: \n"
        print tratarText.PalavrasMaisFrequentes(wordF.encode('utf-8'))
        return lista