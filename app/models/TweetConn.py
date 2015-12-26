# -*- coding: utf-8 -*-
import tweepy
from TratarTexto import *

class TweetConn(object):
    # Dados do App, link: https://apps.twitter.com/app/8699609/keys4
    API_KEY = "gqx2isXl6hdL9xsZgN7JoJStw"
    API_SECRET = "MHpERZf1SLYFokN3FirxO58BBX1JQ9wKMEpoxBSzDnB4ZXnWT0"
    ACCESS_TOKEN = "3433379141-Yq1ksW4MiNtQf1P2Y5EflCRWUO7ipba6nAQhED4"
    ACCESS_TOKEN_SECRET = "2nCqPfFaOQOaiz26vjg0s6KOLsTeeKjIOmWpRFwJj2EzH"
    Lista_palavras = {}
    # Construtor,quando a classe for instanciada gera uma sessão
    # para acesso ao twitter
    def __init__(self):
        OAUTH_KEYS = {'consumer_key': self.API_KEY,
                      'consumer_secret': self.API_SECRET,
                      'access_token_key': self.ACCESS_TOKEN,
                      'access_token_secret': self.ACCESS_TOKEN_SECRET}
        auth = tweepy.OAuthHandler(
            OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
        self.api = tweepy.API(auth)

    def PalavrasMaisFreq(self):
    	return self.Lista_palavras

    def get_Tweets(self,text, prof, polaridade):
        aux = text
        profundidade = prof
        # count = raw_input('Selecione a profundidade da busca:')
        listaTweets = tweepy.Cursor(self.api.search, q=aux).items(profundidade)
        wordF = ""
        tratarText = TratarTexto()
        lista = {}
        for tweet in listaTweets:   
            if polaridade == "Todos":
                print tweet.text + '    | Polaridade: ' + tratarText.SentimentalAnalysis(tweet.text) + '| '
                print '---------------------------------------------------------'
                wordF += tratarText.RetiraStopWords(tratarText.RetirarLinks(tweet.text))
       	        lista.update({tweet.text: tratarText.SentimentalAnalysis(tweet.text)})
            else:
                if polaridade == tratarText.SentimentalAnalysis(tweet.text):
                    print tweet.text + '    | Polaridade: ' + tratarText.SentimentalAnalysis(tweet.text) + '| '
                    print '---------------------------------------------------------'
                    wordF += tratarText.RetiraStopWords(tratarText.RetirarLinks(tweet.text))
                    lista.update({tweet.text: tratarText.SentimentalAnalysis(tweet.text)})

        wordF = tratarText.NormalizarTexto(wordF.encode('utf-8'))
        print "\nPalavras mais frequentes: \n"
        self.Lista_palavras = tratarText.PalavrasMaisFrequentes(wordF.encode('utf-8'))
        return lista