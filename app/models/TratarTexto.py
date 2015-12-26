# -*- coding: utf-8 -*-
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re
import unicodedata
from textblob import TextBlob


class TratarTexto(object):

    """description of class"""

    def RetirarCaracterEspecial(self, word):
        '''RetirarCaracterEspecial(text) -> string
        Retira todos os caracteres especiais de uma string.

            return string
        '''
        # Cria uma lista dos caracteres normais(não especiais)
        safe_chars = string.ascii_letters + string.digits + '_'
        # Retira todos os caracteres especiais do texto.
        word = ''.join([char if char in safe_chars else ' ' for char in word])
        return word
        
    def RetirarLinks(self, text):
        ''' Retirarsinks(text) -> string    

        Retira todos os links da string passada por parametro,
        usando uma Expressão regex.

            return string
        '''
        text = re.sub(r"(?:\@|https?\://)\S+", "", text)
        text = re.sub(r"(?:\@|http?\://)\S+", "", text)
        text = re.sub("http", "", text)
        text = re.sub("https", "", text)
        return text

    def RetirarMencoes(self, text):
        ''' RetirarMencoes(text) -> string

        Remove todas as menções(redes sociais) que começam com '@'.
        Exemplo: @username, @RT...

            return string
        '''
        text = re.sub(
            r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "", text)
        return text

    def RemoverAcentos(self, text):
        ''' RemoverAcentos(text) -> string
        Remove todos os acentos da string.
            return string
        '''
        text = ''.join((c for c in unicodedata.normalize('NFD', text.decode(
            'utf-8', 'ignore')) if unicodedata.category(c) != 'Mn'))
        return text

    def PalavrasMaisFrequentes(self, text):
        '''PalavrasMaisFrequentes(text) -> string

        Lista as palavras mais frequentes da string passada como parametro.
        return list[]
        '''
        fill = Counter(text.split()).most_common()
        return fill

    def RemoverPalavrasPeq(self, text):
        shortword = re.compile(r'\W*\b\w{1,3}\b')
        return shortword.sub('', text)

    def RetiraStopWords(self, text):
        '''RetirarCaracterEspecial(text) -> string
        Retira todas as 'palavras proibidas' de uma string(stopWords).
        return string
        '''
        wordF = ""
        filtrado = [w for w in word_tokenize(
            text) if not w in stopwords.words()]
        for palavra in filtrado:
            wordF += " " + palavra
        else:
            return wordF

    def NormalizarTexto(self, text):
        '''NormalizarTexto(text) -> string
        Normaliza o texto retirando acentos,as palavras muito pequenas,caracteres especiais e as menções

        return string
        '''
        text = self.RemoverPalavrasPeq(text)
        # Remover acentuação.
        text = self.RemoverAcentos(text)
        # Retira todos os caracteres especiais do texto.
        text = self.RetirarCaracterEspecial(text)
        # retirar mençõesss
        text = self.RetirarMencoes(text)
        return text

    def SentimentalAnalysis(self, text):
        '''SentimentalAnalysis(text) -> string
        Analisa o texto passado como parametro para saber se é positivo ou negativo.

        return string
        '''
        tweet = TextBlob(text)
        if tweet.sentiment.polarity < 0:
            sentiment = "Negativo"
        elif tweet.sentiment.polarity == 0:
            sentiment = "Neutro"
        else:
            sentiment = "Positivo"
        return sentiment

