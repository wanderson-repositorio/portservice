from PortServiceModelos.Token import Token
from PortServiceConstantes import Constantes
import PortServiceGerenteClasses.GerenteClasses
from nltk import sent_tokenize

class Operacoes(object):


    def GetAnaliseMorfossintaticaFreeling(self,texto):
        listaTokensClassificados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetEtiquetadorFreeling().GetMarcacaoMorfossintaticaFreeeling(texto)
        return listaTokensClassificados


   
    def GetAnaliseMorfossintaticaPadrao(self, texto):
        listaTokensClassificados = self.__GetMarcacaoMorfossintaticaPadrao(texto)
        return listaTokensClassificados



    def GetAnaliseMorfossintaticaTreeTagger(self,texto):
        listaTokensCassificados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetEtiquetadorTreeTagger().GetMarcacaoMorfossintaticaTreeTagger(texto)
        return  listaTokensCassificados




    def GetAnaliseLexicoSemanticaOntoPT(self, texto, indice):
        listaTokensClassificados =  self.GetAnaliseMorfossintaticaTreeTagger(texto)
        try:
            operacao = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetOntoPt().GetDicionarioOpercaoes(indice)
        except:
            operacao = None


        for token in listaTokensClassificados:

            if token.ClasseGramatical[0] in ['A','R','N','V']:
                token.ListaSignificados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetOntoPt().GetSynsets(token.Lema,operacao)


        return listaTokensClassificados,operacao




    def GetAnaliseLexicoSemanticaPulo(self,texto):
        listaTokensClassificados =  self.GetAnaliseMorfossintaticaTreeTagger(texto)

        for token in listaTokensClassificados:

            if token.ClasseGramatical[0] in ['A','R','N','V']:
                token.ListaSignificados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetPulo().GetSynsets(token.Lema)


        return listaTokensClassificados



    def GetFullAnalise(self,texto,indice,tagger):

        listaTokensClassificados = None

        if tagger == Constantes.TAGGERPADRAO:
            listaTokensClassificados = self.__GetMarcacaoMorfossintaticaPadrao(texto)
        elif tagger == Constantes.TAGGERTREETAGGER:
            listaTokensClassificados = self.GetAnaliseMorfossintaticaTreeTagger(texto)

        try:
            operacao = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetOntoPt().GetDicionarioOpercaoes(indice)
        except:
            operacao = None


        for token in listaTokensClassificados:
            if tagger == Constantes.TAGGERPADRAO:
                if token.ClasseGramatical in ['ADV','ADJ','N','V']:
                    token.ListaSignificados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetOntoPt().GetSynsets(token.Lema,operacao)
            elif tagger == Constantes.TAGGERTREETAGGER:
                token.ListaSignificados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetOntoPt().GetSynsets(token.Lema,operacao)
       
        return listaTokensClassificados,operacao







    def __GetMarcacaoMorfossintaticaPadrao(self, texto):
        listaTokensClassificados = list()
        tokensEtiquetados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetEtiquetadorPadrao().EtiquetarTexto(texto)

        if tokensEtiquetados != None:
            for item in tokensEtiquetados:
                              
                  if item[1]!= None:
                    token = self.__GetMarcacaoMorfossintaticaDB(item[0],item[1])   
                  else:
                      token = self.__GetPropriedadesMorfossintaticaDBLexico(item[0])
                 
                  if token == None:
                      token = Token()
                      token.Token = item[0]     
                                 
                  listaTokensClassificados.append(token)

                
        return listaTokensClassificados


    def __GetMarcacaoMorfossintaticaDB(self,palavra,id):
        propriedades = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetAcessoDB().GetPropriedadesMorfossintaticaDB(palavra, id)
        if propriedades != None:
            token = Token()
            token.Token = palavra
            token.Lema = propriedades[0]
            if token.Lema == None:
                token.Lema = palavra
            token.ClasseGramatical = propriedades[1]
            token.Tempo = propriedades[2]
            token.Pessoa= propriedades[3]
            token.Numero = propriedades[4]
            token.Genero = propriedades[5]
            token.Modo = propriedades[6]
            token.Tipo = propriedades[7]
            token.SubCategoria = propriedades[8]
            return token
        else:
            return None


    def __GetPropriedadesMorfossintaticaDBLexico(self,palavra):
        propriedades = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetAcessoDB().GetPropriedadesDBLexico(palavra)
        if propriedades != None:
            token = Token()
            token.Token = palavra
            token.Lema = propriedades[0]
            if token.Lema == None:
                token.Lema = palavra
            token.ClasseGramatical = propriedades[1]
            token.Tempo = propriedades[2]
            token.Pessoa= propriedades[3]
            token.Numero = propriedades[4]
            token.Genero = propriedades[5]
            token.Modo = propriedades[6]
            token.Tipo = propriedades[7]
            token.SubCategoria = propriedades[8]          
            return token
        else:
            return None


    def GetFullAnaliseOWN(self,texto):
        listaTokensClassificados = self.GetAnaliseMorfossintaticaTreeTagger(texto)

        for token in listaTokensClassificados:
                if token.ClasseGramatical[0] in ['A','R','N','V']:
                    token.ListaSignificados = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetOpenWordNetPT().GetSynsets(token.Lema)


        return listaTokensClassificados


    def SentenceTokenizer(self,texto):
        return sent_tokenize(texto,language = 'portuguese')



