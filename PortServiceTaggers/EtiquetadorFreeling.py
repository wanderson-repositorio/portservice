from subprocess import Popen,PIPE
from PortServiceModelos.Token import Token


tagger = None

class EtiquetadorFreeling(object):


    def GetMarcacaoMorfossintaticaFreeeling(self,texto):

        listaTokensClassificados = list()
        processo = Popen(['analyze -f pt.cfg'],stdin=PIPE, stdout=PIPE,shell=True)
        saida = str(processo.communicate(bytes (texto, 'UTF-8'))[0])
        listaTokens = saida[2:len(saida)].split('\\n')
        for item in listaTokens[0:len(listaTokens)-2]:
            lista = item.split(' ')
            token = Token()
            token.Token = str(lista[0]).replace('n','')
            token.Lema = str(lista[1])
            token.ClasseGramatical = str(lista[2])
            listaTokensClassificados.append(token)

        return listaTokensClassificados

