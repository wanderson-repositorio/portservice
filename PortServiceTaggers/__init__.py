import os
import pickle
import PortServiceTaggers.EtiquetadorPadrao as pln
import PortServiceTaggers.EtiquetadorTreeTagger as treetagger
import codecs
from PortServiceTaggers import EtiquetadorTreeTagger

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

if pln.etiquetador == None:
    arq = codecs.open('/home/portservice/taggers/etiquetador_perceptron_tagger.pickle','rb+',encoding='iso-8859-1')
    #arq = codecs.open(PROJECT_PATH+'/arquivos/taggers/hibrido/etiquetador.pickle','rb+',encoding='iso-8859-1')
    etiquetador = pickle.load(arq)
    arq.close()

    '''arq = codecs.open(PROJECT_PATH+'/arquivos/dicionarioMultiWord.pickle','rb+',encoding='iso-8859-1')
    dicionarioMultiWord = pickle.load(arq)
    arq.close()'''

    '''arq = codecs.open(PROJECT_PATH+'/arquivos/processadorMultWord.pickle','rb+',encoding='iso-8859-1')
    processadorMultWord = pickle.load(arq)
    arq.close()'''

    contracoes = open(PROJECT_PATH+'/arquivos/dicionario_contracoes.txt','r',encoding='iso-8859-1')
    dicionarioContracoes = dict()
    for con in contracoes:
        atributos = con.split(':')
        dicionarioContracoes[atributos[0]] = atributos[1]

    tagger = EtiquetadorTreeTagger.EtiquetadorTreeTagger(language='portuguese')

    #pln.dicionarioMultiWord = dicionarioMultiWord
    #pln.processadorMultWord = processadorMultWord
    treetagger.tagger = tagger
    pln.dicionarioContracoes = dicionarioContracoes
    pln.etiquetador = etiquetador


   

