__author__ = 'Wanderson Rocha'

from xml.etree.ElementTree import Element, SubElement
from PortServiceXML.ElementTree_pretty import prettify
from PortServiceConstantes import Constantes

class XML(object):


    def GeerarArquivoKeyErroXml(self, err):
        error = Element('error')
        error.text = 'Parâmetro '+str(err)+' não encontrado.'
        return prettify(error)



    def GerarArquivoErroXml(self, err):
        error = Element('error')
        error.text = err
        return prettify(error)


    def GerarArquivoFreelingTretaggerXml(self, listaTokens):

        tokens = Element("texto")

        for item in listaTokens:

            pa = item
            token = SubElement(tokens, "token")

            tokenPalavra = SubElement(token, "palavra")
            tokenPalavra.text = pa.Token

            lema = SubElement(token, "lema")
            lema.text = pa.Lema

            classe = SubElement(token, 'pos')
            classe.text = pa.ClasseGramatical

        return prettify(tokens)



    def GerararquivoTaggerPadraoXml(self, listaTokens):

        tokens = Element("texto")

        for item in listaTokens:

            pa = item
            token = SubElement(tokens, "token")

            tokenPalavra = SubElement(token, "palavra")
            tokenPalavra.text = pa.Token

            lema = SubElement(token, "lema")
            lema.text = pa.Lema

            classe = SubElement(token, 'pos')
            classe.text = pa.ClasseGramatical

            genero = SubElement(token, 'genero')
            genero.text = pa.Genero

            numero = SubElement(token, 'numero')
            numero.text = pa.Numero

            sub = SubElement(token, 'sub_class')
            sub.text = pa.SubCategoria

            pessoa = SubElement(token, 'pessoa')
            pessoa.text = pa.Pessoa

            modo = SubElement(token, 'modo')
            modo.text = pa.Modo

            tempo = SubElement(token, 'tempo')
            tempo.text = pa.Tempo

            tipo = SubElement(token, 'finitude')
            tipo.text = pa.Tipo

        return prettify(tokens)


    def GerarArquivoOntoPtXml(self, listaTokens, operacao):
         tokens = Element("texto")

         for item in listaTokens:

            pa = item
            token = SubElement(tokens, "token")

            tokenPalavra = SubElement(token, "palavra")
            tokenPalavra.text = pa.Token
            if pa.ListaSignificados != None:
                significados = SubElement(token, 'significados')
                for sig in pa.ListaSignificados:
                    significado = SubElement(significados,'significado')
                    id = SubElement(significado, 'id')
                    id.text = sig.SynsetId

                    if sig.Definicao == None:
                        defi = '--'
                    else:
                        defi = sig.Definicao

                    definicao = SubElement(significado, 'definicao')
                    definicao.text = defi

                    classeSynset = SubElement(significado, 'classe')
                    classeSynset.text = sig.ClasseGramatical

                    sinonimos = SubElement(significado, 'lista_sinonimo')
                    listaAntonimos = SubElement(significado, 'lista_antonimo')

                    if operacao != None:
                        listaAnonimo = SubElement(significado, 'lista_'+operacao)                       
                    
                        for m in sig.ListaSynsetsAnonimo:

                            anonimo = SubElement(listaAnonimo, operacao)

                            id = SubElement(anonimo, 'id')
                            id.text = m.SynsetId

                            definicao = SubElement(anonimo, 'definicao')
                            definicao.text = m.Definicao

                            classe = SubElement(anonimo, 'classe')
                            classe.text = m.ClasseGramatical
                            palavras = SubElement(anonimo, 'palavras')

                            for l in m.ListaFormasLexicais:                               
                                palavra = SubElement(palavras, 'palavra')
                                palavra.text = l

                    if sig.ListaFormasLexicais == None:
                        sinonimos.text = '--'
                    else:
                        for s in sig.ListaFormasLexicais:
                            sinonimo = SubElement(sinonimos, 'palavra')
                            sinonimo.text = s

                    if sig.ListaSynsetsAntonimos == None:
                        listaAntonimos.text = '--'
                    else:
                        for a in sig.ListaSynsetsAntonimos:
                            antonimo = SubElement(listaAntonimos, 'antonimo')

                            id = SubElement(antonimo, 'id')
                            id.text = a.SynsetId

                            definicao = SubElement(antonimo, 'definicao')
                            definicao.text = a.Definicao

                            classe = SubElement(antonimo, 'classe')
                            classe.text = a.ClasseGramatical

                            for l in a.ListaFormasLexicais:
                                antonimos = SubElement(antonimo, 'palavras')
                                palavra = SubElement(antonimos, 'palavra')
                                palavra.text = l

                    

         return prettify(tokens)





    def GerarArquivoPuloXml(self, listaTokens):
         tokens = Element("texto")

         for item in listaTokens:

            pa = item
            token = SubElement(tokens, "token")

            tokenPalavra = SubElement(token, "palavra")
            tokenPalavra.text = pa.Token
            if pa.ListaSignificados != None:
                significados = SubElement(token, 'significados')
                for sig in pa.ListaSignificados:
                    significado = SubElement(significados,'significado')
                    id = SubElement(significado, 'id')
                    id.text = sig.SynsetId

                    if sig.Definicao == None:
                        defi = '--'
                    else:
                        defi = sig.Definicao

                    definicao = SubElement(significado, 'definicao')
                    definicao.text = defi

                    classeSynset = SubElement(significado, 'classe')
                    classeSynset.text = sig.ClasseGramatical

                    sinonimos = SubElement(significado, 'lista_sinonimo')


                    if sig.ListaFormasLexicais == None:
                        sinonimos.text = '--'
                    else:
                        for s in sig.ListaFormasLexicais:
                            sinonimo = SubElement(sinonimos, 'palavra')
                            sinonimo.text = s


         return prettify(tokens)



    def GerarArquivoFullAnaliseOntoPtXml(self, listaTokens, operacao, tagger):

        tokens = Element("texto")

        for item in listaTokens:

            pa = item
            token = SubElement(tokens, "palavra")

            tokenPalavra = SubElement(token, "palavra")
            tokenPalavra.text = pa.Token

            lema = SubElement(token, "lema")
            lema.text = pa.Lema

            classe = SubElement(token, 'pos')
            classe.text = pa.ClasseGramatical

            if tagger == Constantes.TAGGERPADRAO:
                genero = SubElement(token, 'genero')
                genero.text = pa.Genero

                numero = SubElement(token, 'numero')
                numero.text = pa.Numero

                sub = SubElement(token, 'sub_class')
                sub.text = pa.SubCategoria

                pessoa = SubElement(token, 'pessoa')
                pessoa.text = pa.Pessoa

                modo = SubElement(token, 'modo')
                modo.text = pa.Modo

                tempo = SubElement(token, 'tempo')
                tempo.text = pa.Tempo

                tipo = SubElement(token, 'finitude')
                tipo.text = pa.Tipo

            if pa.ListaSignificados != None:
                significados = SubElement(token, 'significados')
                for sig in pa.ListaSignificados:
                    significado = SubElement(significados,'significado')
                    id = SubElement(significado, 'id')
                    id.text = sig.SynsetId

                    if sig.Definicao == None:
                        defi = '--'
                    else:
                        defi = sig.Definicao

                    definicao = SubElement(significado, 'definicao')
                    definicao.text = defi

                    classeSynset = SubElement(significado, 'classe')
                    classeSynset.text = sig.ClasseGramatical

                    sinonimos = SubElement(significado, 'lista_sinonimo')
                    listaAntonimos = SubElement(significado, 'lista_antonimo')

                    if operacao != None:
                        listaAnonimo = SubElement(significado, 'lista_'+operacao)                       
                    
                        for m in sig.ListaSynsetsAnonimo:

                            anonimo = SubElement(listaAnonimo, operacao)

                            id = SubElement(anonimo, 'id')
                            id.text = m.SynsetId

                            definicao = SubElement(anonimo, 'definicao')
                            definicao.text = m.Definicao

                            classe = SubElement(anonimo, 'classe')
                            classe.text = m.ClasseGramatical
                            palavras = SubElement(anonimo, 'palavras')

                            for l in m.ListaFormasLexicais:                               
                                palavra = SubElement(palavras, 'palavra')
                                palavra.text = l


                    if sig.ListaFormasLexicais == None:
                        sinonimos.text = '--'
                    else:
                        for s in sig.ListaFormasLexicais:
                            sinonimo = SubElement(sinonimos, 'palavra')
                            sinonimo.text = s



                    if sig.ListaSynsetsAntonimos == None:
                        listaAntonimos.text = '--'
                    else:
                        for a in sig.ListaSynsetsAntonimos:
                            antonimo = SubElement(listaAntonimos, 'antonimo')

                            id = SubElement(antonimo, 'id')
                            id.text = a.SynsetId

                            definicao = SubElement(antonimo, 'definicao')
                            definicao.text = a.Definicao

                            classe = SubElement(antonimo, 'classe')
                            classe.text = a.ClasseGramatical

                            antonimos = SubElement(antonimo, 'palavras')
                            for l in a.ListaFormasLexicais:
                                
                                palavra = SubElement(antonimos, 'palavra')
                                palavra.text = l

                    

        return prettify(tokens)
