"""
Definition of views.
"""
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from models.TweetConn import *
from models.InstagramConn import *
from models.TratarTexto import *
from forms import *
                                                                                            

def twitter(request):
    """Renders the home page."""
    session = request.session
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if "form1" in request.POST:  
                #print "print" + session['lista']
                username = request.POST.get('your_name')
                profundidade = request.POST.get('profundidade')
                polaridade = request.POST.get('polaridade')
                buscaBinaria = ''
        else: 
            lista = {}
            buscaBinaria = request.POST.get('buscaBinaria')
            listaBin = session['listaAntiga']
            for key,value in listaBin.items():
                if buscaBinaria in key:
                    lista.update({key: value})
            session['lista'] = lista
            session.save()
            username = 'twitter'
            profundidade = 10
            polaridade = 'Todos'

    else: 
        username = 'twitter'
        profundidade = 10
        polaridade = 'Todos'
        buscaBinaria = ''

    tweet = TweetConn()
    tratarText = TratarTexto()  
    #print polaridade
    if buscaBinaria == '':
        tweets = tweet.get_Tweets(username,int(profundidade), polaridade)
        session['lista'] = tweets
        session['listaAntiga'] = tweets
        session['hashtag'] = username
        session.save()
    else: 
        tweets = session['lista']
    tweetLista = ''
    for x in tweets:
        tweetLista += tratarText.RetiraStopWords(tratarText.RetirarLinks(x)) + ' ' 
    listaPalavras = tratarText.PalavrasMaisFrequentes(tratarText.NormalizarTexto(tweetLista.encode('utf-8')))
    
    qtdPos = sum(x == "Positivo" for x in tweets.values())    
    qtdNeg = sum(x == "Negativo" for x in tweets.values())  
    qtdNeutro = sum(x == "Neutro" for x in tweets.values())
    
    qtdTotal = qtdPos + qtdNeg + qtdNeutro
    percentPos = 0; percentNeg = 0; percentNeutro = 0
    #print qtdPos
    if qtdPos != 0:
        percentPos = (100.0 * qtdPos) / qtdTotal 
    if qtdNeg != 0:
        percentNeg = (100.0 * qtdNeg) / qtdTotal
    if qtdNeutro != 0:
        percentNeutro = (100.0 * qtdNeutro) / qtdTotal
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/twitter.html',
        context_instance = RequestContext(request,
        {
            'listDict' : tweets,
            'title':'Twitter',
            'year':datetime.now().year,
            'qtdPos':qtdPos,
            'qtdNeg': qtdNeg,
            'qtdNeutro':qtdNeutro,
            'hashtag': session['hashtag'],
            'listBin': session['lista'],
            'percentPos':"{0:.2f}".format(round(percentPos,2)),
            'percentNeg':"{0:.2f}".format(round(percentNeg,2)),
            'percentNeutro':"{0:.2f}".format(round(percentNeutro,2)),
            'listPalavras': listaPalavras,
        })
    )



def instagram(request):
    session = request.session
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if "form1" in request.POST:  
                username = request.POST.get('your_name')
                profundidade = request.POST.get('profundidade')
                polaridade = request.POST.get('polaridade')
                buscaBinaria = ''
        else: 
            lista = {}
            buscaBinaria = request.POST.get('buscaBinaria')
            listaBin = session['listaAntiga']
            for key,value in listaBin.items():
                if buscaBinaria in key:
                    lista.update({key: value})
            session['lista'] = lista
            username = 'insta'
            profundidade = 10
            polaridade = 'Todos'
    else: 
        username = 'insta'
        profundidade = 10
        polaridade = 'Todos'
        buscaBinaria = ''

    insta = InstagramConn()
    tratarText = TratarTexto()
    if buscaBinaria == '':
        instaPosts = insta.BuscarResultados(username,int(profundidade), polaridade)
        session['lista'] = instaPosts
        session['listaAntiga'] = instaPosts
        session['hashtag'] = username
        session.save()
    else: 
        instaPosts = session['lista']
    instaLista = ''
    for x in instaPosts:
        instaLista += tratarText.RetiraStopWords(tratarText.RetirarLinks(x)) + ' ' 
    listaPalavras = tratarText.PalavrasMaisFrequentes(tratarText.NormalizarTexto(instaLista.encode('utf-8')))
    
    qtdPos = sum(x == "Positivo" for x in instaPosts.values())    
    qtdNeg = sum(x == "Negativo" for x in instaPosts.values())  
    qtdNeutro = sum(x == "Neutro" for x in instaPosts.values())
    qtdTotal = qtdPos + qtdNeg + qtdNeutro
    percentPos = 0; percentNeg = 0; percentNeutro = 0
    

    #print qtdPos
    if qtdPos != 0:
        percentPos = (100.0 * qtdPos) / qtdTotal 
    if qtdNeg != 0:
        percentNeg = (100.0 * qtdNeg) / qtdTotal
    if qtdNeutro != 0:
        percentNeutro = (100.0 * qtdNeutro) / qtdTotal

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/instagram.html',
        context_instance = RequestContext(request,
        {
            'listDict' : instaPosts,
            'title':'Instagram',
            'year':datetime.now().year,
            'qtdPos':qtdPos,
            'qtdNeg': qtdNeg,
            'hashtag': session['hashtag'],
            'qtdNeutro':qtdNeutro,
            'listBin': session['lista'],
            'percentPos':"{0:.2f}".format(round(percentPos,2)),
            'percentNeg':"{0:.2f}".format(round(percentNeg,2)),
            'percentNeutro':"{0:.2f}".format(round(percentNeutro,2)),
            'listPalavras': listaPalavras,
        })
    )
