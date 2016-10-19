import json
from PortServiceConstantes import Constantes
class Json(object):



    def GerarArquivokeyErroJson(self, err):
        error = {'error':'Parâmetro '+err+' não encontrado.'}
        return json.dumps(error,indent=4)


    def GerarArquivoErroJson(self, err):
        error = {'error':err}
        return json.dumps(error,indent=4)


    def GerarArquivoTreeTaggerFreelingJson(self, listaTokensClassificados):
        tokens = {}
        lista = list()

        for item in listaTokensClassificados:

            token = {}
            responseData = {}
            tk = item
            responseData['palavra'] = tk.Token
            responseData['lema'] = tk.Lema
            responseData['pos'] = tk.ClasseGramatical
            token['token'] = responseData
            lista.append(token)

        tokens['texto'] = lista
        return json.dumps(tokens, indent=4)



    def GerarArquivoTaggerPadraoJson(self, listaTokens):

        tokens = {}
        lista = list()      

        for item in listaTokens:      
            
            token = {}
            responseData = {}
            tk = item

            responseData['palavra'] = tk.Token
            responseData['lema'] = tk.Lema
            responseData['pos'] = tk.ClasseGramatical
            responseData['genero'] = tk.Genero
            responseData['numero'] = tk.Numero
            responseData['sub_class'] = tk.SubCategoria
            responseData['pessoa'] = tk.Pessoa
            responseData['modo'] = tk.Modo
            responseData['tempo'] = tk.Tempo
            responseData['finitude'] = tk.Tipo

            token['token'] = responseData
            lista.append(token)

        tokens['texto'] = lista
        return json.dumps(tokens, indent=4)



    def GerarArquivoPuloJson(self, listaTokens):
        tokens = {}
        lista = list()

        for item in listaTokens:

            token = {}
            responseData = {}
            tk = item

            if tk.ListaSignificados != None and tk.ListaSignificados != []:
                listaSignificados = list()
                for item in tk.ListaSignificados:
                    sinonimos = item.ListaFormasLexicais

                    if item.Definicao == None:
                        definicao = '--'

                    else:
                        definicao = item.Definicao


                    listaSignificados.append({'id':item.SynsetId,'definicao': definicao,'classe':item.ClasseGramatical,'lista_sinonimo':sinonimos})
                responseData['significados'] = listaSignificados
            else:
                responseData['significados'] = '--'

            responseData['palavra'] = tk.Token
            token['token'] = responseData
            lista.append(token)

        tokens['texto'] = lista
        return json.dumps(tokens,indent=4)



    def GerarArquivoOntoPtJson(self, listaTokens, operacao):

        tokens = {}
        lista = list()      

        for item in listaTokens:      
            
            token = {}
            responseData = {}
            tk = item
          
            if tk.ListaSignificados != None and tk.ListaSignificados != []:
                listaSignificados = list()
                for item in tk.ListaSignificados:
                    sinonimos = item.ListaFormasLexicais
                    antonimos = self._GetAntonimos(item.ListaSynsetsAntonimos)
                   
                    if item.Definicao == None:
                        definicao = '--'

                    else:
                        definicao = item.Definicao

                    if operacao != None:
                        anonimo = self._GetListaSynsetsAnonimo(item.ListaSynsetsAnonimo)
                        listaSignificados.append({'id':item.SynsetId,'definicao': definicao,'classe':item.ClasseGramatical,'lista_sinonimo':sinonimos,'lista_antonimo':antonimos,'lista_'+operacao:anonimo})
                    else:
                         listaSignificados.append({'id':item.SynsetId,'definicao': definicao,'classe':item.ClasseGramatical,'lista_sinonimo':sinonimos,'lista_antonimo':antonimos})
                responseData['significados'] = listaSignificados
            else:
                responseData['significados'] = '--'

            responseData['palavra'] = tk.Token
            token['token'] = responseData
            lista.append(token)

        tokens['texto'] = lista
        return json.dumps(tokens,indent=4)




    def GerarArquivoFullAnaliseOntoPtJson(self, listaTokens, operacao, tagger):

        tokens = {}
        lista = list()      

        for item in listaTokens:      
            
            token = {}
            responseData = {}
            tk = item


            responseData['palavra'] = tk.Token
            responseData['lema'] = tk.Lema
            responseData['pos'] = tk.ClasseGramatical

            if tagger == Constantes.TAGGERPADRAO:
                responseData['genero'] = tk.Genero
                responseData['numero'] = tk.Numero
                responseData['sub_class'] = tk.SubCategoria
                responseData['pessoa'] = tk.Pessoa
                responseData['modo'] = tk.Modo
                responseData['tempo'] = tk.Tempo
                responseData['finitude'] = tk.Tipo


            if tk.ListaSignificados != None:
                listaSignificados = list()
                for item in tk.ListaSignificados:
                    sinonimos = item.ListaFormasLexicais
                    antonimos = self._GetAntonimos(item.ListaSynsetsAntonimos)
                    if item.Definicao == None:
                        definicao = '--'
                    else:
                        definicao = item.Definicao

                    if operacao != None:
                        anonimo = self._GetListaSynsetsAnonimo(item.ListaSynsetsAnonimo)
                        listaSignificados.append({'id':item.SynsetId,'definicao': definicao,'classe':item.ClasseGramatical,'lista_sinonimo':sinonimos,'lista_antonimo':antonimos,'lista_'+operacao:anonimo})

                    else:
                         listaSignificados.append({'id':item.SynsetId,'definicao': definicao,'classe':item.ClasseGramatical,'lista_sinonimo':sinonimos,'lista_antonimo':antonimos})

                responseData['significados'] = listaSignificados
            else:
                responseData['significados'] = '--'


            token['token'] = responseData
            lista.append(token)

        tokens['texto'] = lista
        return json.dumps(tokens,indent=4)




    def _GetSinonimos(self, listaSinonimos):
         lista = list()
         if listaSinonimos != []:
            for s in listaSinonimos:
                lista.append({'palavra':s})
            return lista
         else:
             return '--'



    def _GetListaSynsetsAnonimo(self, anonimo):
         listAnonimo = list()
         if anonimo != []:
            for s in anonimo:
                lista = list()
                for si in s.ListaFormasLexicais:
                    lista.append(si)
                listAnonimo.append({'id':s.SynsetId,'definicao':s.Definicao,'classe':s.ClasseGramatical,'palavras':lista})
            return listAnonimo
         else:
             return '--'



    def _GetAntonimos(self, antonimos):
         listaAntonimos = list()
         if antonimos != []:
            for s in antonimos:
                lista = list()
                for si in s.ListaFormasLexicais:
                    lista.append(si)
                listaAntonimos.append({'id':s.SynsetId,'definicao':s.Definicao,'classe':s.ClasseGramatical,'palavras':lista})

            return listaAntonimos
         else:
             return '--'

    def GerarArquivoFullAnaliseOWN(self,listaTokens):

        tokens = {}
        lista = list()

        for item in listaTokens:

            token = {}
            responseData = {}
            dicionarioMorfossintax = {'word':item.Token,'lemma':item.Lema,'poss':item.ClasseGramatical}
            responseData['morfossintax'] = dicionarioMorfossintax

            listaSignificados = list()

            for own in item.ListaSignificados:
                listaSignificados.append({'synsetId':own.SynsetId,'synset': own.Synset,'type':own.Type,'gloss':own.Gloss})
            responseData['synsets'] = listaSignificados

            token['token'] = responseData
            lista.append(token)

        tokens['tokens'] = lista
        return json.dumps(tokens,indent=4)


    def GerarArquivoSentences(self,listSentence):
        sentences = {}
        listaSenteces = list()

        for item in listSentence:
            sentence = {"sentence":item}
            listaSenteces.append(sentence)

        sentences["sentences"] = listaSenteces
        return json.dumps(sentences,indent=4)
