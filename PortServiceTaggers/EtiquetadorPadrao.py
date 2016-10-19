from nltk import word_tokenize as tokenizar
import re as regex

etiquetador = None
processadorMultWord = None
dicionarioMultiWord = None
dicionarioContracoes =  None
dicionarioPropriedades = None
dicionarioFlexaoLema = None
dicionarioPropriedadesLexico = None

class EtiquetadorPadrao(object):


    def EtiquetarTexto(self,texto):
        novoTexto = self.ReplaceContracoes(texto,dicionarioContracoes)             
        tokens = self.Tokenizar(novoTexto)
        tokensEtiquetados = self.Etiquetador(tokens)
        return tokensEtiquetados

    '''def EtiquetarTexto(self,texto,multWordidentificado):
        novoTexto = self.ReplaceContracoes(texto,dicionarioContracoes)
        tokens =self.Tokenizar(novoTexto)
        if multWordidentificado:
            tokens = self.__LimparTokensMultWord(tokens)
        tokensEtiquetados = self.Etiquetador(tokens)
        return tokensEtiquetados'''


      
    def Tokenizar(self,texto):        
        tokes = tokenizar(texto,language = 'portuguese')
        return tokes



    def Etiquetador(self,tokens):         
        tokensEtiquetados = etiquetador.tag(tokens)
        return tokensEtiquetados       
    

    def IdentificarExpressoesMultWord(self,texto):      
       textoMultWord = processadorMultWord.sub(lambda mo: dicionarioMultiWord[mo.string[mo.start():mo.end()]], texto)
       if texto == textoMultWord:
        return  False,textoMultWord
       else:
           return  True,textoMultWord


    def __LimparTokensMultWord(self,listaTokens):
       novaListaTokens = list()
       for token in listaTokens:
           novaListaTokens.append(token.replace('_',' '))
       return novaListaTokens



    def ReplaceContracoes(self,text, replace_dict):        
        rc = regex.compile(r"[A-Za-z_]\w*")
        def translate(match):
            word = match.group(0)
            return replace_dict.get(word, word)
        return rc.sub(translate, text)    

    

    