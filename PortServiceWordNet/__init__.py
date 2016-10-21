import os
import PortServiceWordNet.OntoPT as rdf
import PortServiceWordNet.OpenWordNetPT as openWN
import pickle
import codecs



PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))


arq = open(PROJECT_PATH+'/arquivos/onto_pt.pickle', 'rb+')
graph = pickle.load(arq)
arq.close()
rdf.ONTOLOGIA_ONTO_PT = graph


arq = open(PROJECT_PATH+'/arquivos/dicionario_operacoes.txt', 'r',encoding='iso-8859-1')
dicionarioOperacoes = dict()
for operacoes in arq:
        atributos = operacoes.split(',')
        dicionarioOperacoes[int(atributos[1])] = atributos[0]
rdf.DICIONARIO_OPERACOES = dicionarioOperacoes

arq = codecs.open('/home/portservice/wordnet/openWordNetPT.pickle', 'rb+')
openWN.openWordNetPT= pickle.load(arq)
arq.close()
