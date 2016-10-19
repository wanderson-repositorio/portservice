from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from rest_framework.views import APIView
from PortServiceGerenteClasses.GerenteClasses import GerenteClasses
from PortServiceConstantes import Constantes


def inicio(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/inicio.html',context_instance=RequestContext(request,
           {
              'title': 'Portservice-Br',
              'inicio': True,
              'year': datetime.now().year,
           }))


def instrucoes(request):   
    assert isinstance(request, HttpRequest)
    return render(request,'app/instrucoes.html',context_instance=RequestContext(request,
           {
              'title': 'Instrucoes',
              'instrucoes': True,
              'year': datetime.now().year,                                                      
           }))


def publicacoes(request):   
    assert isinstance(request, HttpRequest)
    return render(request,'app/publicacoes.html',context_instance=RequestContext(request,
           {
             'title': 'Publicacoes',
             'publicacoes': True,
             'year': datetime.now().year,                                                      
           }))


def sobre(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/sobre.html',context_instance=RequestContext(request,
           {
             'title': 'Projeto',
             'sobre': True,
             'year': datetime.now().year,
           }))


def consultar(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/consultar.html',context_instance=RequestContext(request,
           {
             'title': 'Consultar',
             'conceituacao': True,
             'year': datetime.now().year,
          }))



'''Inicio etiquetadores morfossintaticos'''

class GetAnaliseMorfossintaticaFreelingXML(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('texto_portugues'), content_type ='application/xml')


            listaTokensClassificados = GerenteClasses.GetOpercaoes().GetAnaliseMorfossintaticaFreeling(texto)
            arquivoJson = GerenteClasses.GetGeradorArquivoXml().GerarArquivoFreelingTretaggerXml(listaTokensClassificados)
            return HttpResponse(arquivoJson,content_type ='application/xml')

        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml(str(ex)), content_type ='application/xml')


class GetAnaliseMorfossintaticaFreelingJson(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')

            listaTokensClassificados = GerenteClasses.GetOpercaoes().GetAnaliseMorfossintaticaFreeling(texto)
            arquivoJson = GerenteClasses.GetGeradorArquivoJson().GerarArquivoTreeTaggerFreelingJson(listaTokensClassificados)
            return HttpResponse(arquivoJson,content_type ='application/json')

        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')


class GetAnaliseMorfossintaticaTreTaggerXML(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml("texto_portugues"), content_type ='application/xml')

            listaTokensClassificados = GerenteClasses.GetOpercaoes().GetAnaliseMorfossintaticaTreeTagger(texto)
            arquivoxml = GerenteClasses.GetGeradorArquivoXml().GerarArquivoFreelingTretaggerXml(listaTokensClassificados)
            return HttpResponse(arquivoxml,content_type ='application/xml')

        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml(str(ex)), content_type ='application/xml')



class GetAnaliseMorfossintaticaTreTaggerJson(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')

            listaTokensClassificados = GerenteClasses.GetOpercaoes().GetAnaliseMorfossintaticaTreeTagger(texto)
            arquivoJson = GerenteClasses.GetGeradorArquivoJson().GerarArquivoTreeTaggerFreelingJson(listaTokensClassificados)
            return HttpResponse(arquivoJson,content_type ='application/json')

        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')



class GetAnaliseMorfossintaticaXML(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                return  HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('texto_portugues'), content_type ='application/xml')


            listaTokens = GerenteClasses.GetOpercaoes().GetAnaliseMorfossintaticaPadrao(texto.lower())
            arquivoXML = GerenteClasses.GetGeradorArquivoXml().GerararquivoTaggerPadraoXml(listaTokens)
            return HttpResponse(arquivoXML,content_type ='application/xml')
        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml(str(ex)), content_type ='application/xml')


class GetAnaliseMorfossintaticaJson(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')


            listaTokens = GerenteClasses.GetOpercaoes().GetAnaliseMorfossintaticaPadrao(texto.lower())
            arquivoJason = GerenteClasses.GetGeradorArquivoJson().GerarArquivoTaggerPadraoJson(listaTokens)
            return HttpResponse(arquivoJason,content_type ='application/json')
        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(str(ex))), content_type ='application/json')

#Fim etiquetadores morfossintaticos



#Inicio Analisadores lexico semanticos
class GetAnaliseLexicoSemanticaPuloJson(APIView):

    def get(self, request, *args, **kw):
         try:

            texto = request.GET.get('texto_portugues')

            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')


            listaTokens = GerenteClasses.GetOpercaoes().GetAnaliseLexicoSemanticaPulo(texto.lower())
            arquivoJason = GerenteClasses.GetGeradorArquivoJson().GerarArquivoPuloJson(listaTokens)
            return HttpResponse(arquivoJason,content_type ='application/json')
         except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')



class GetAnaliseLexicoSemanticaPuloXml(APIView):

    def get(self, request, *args, **kw):
         try:

            texto = request.GET.get('texto_portugues')

            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GeerarArquivoKeyErroXml('texto_portugues'), content_type ='application/xml')


            listaTokens = GerenteClasses.GetOpercaoes().GetAnaliseLexicoSemanticaPulo(texto.lower())
            arquivoxml = GerenteClasses.GetGeradorArquivoXml().GerarArquivoPuloXml(listaTokens)
            return HttpResponse(arquivoxml,content_type ='application/xml')
         except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroXml(str(ex)), content_type ='application/xml')


class GetAnaliseLexicoSemanticaOntoPtJson(APIView):

    def get(self, request, *args, **kw):
         try:

            texto = request.GET.get('texto_portugues')
            indice = request.GET.get('indice')

            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')
            if indice is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('indice'), content_type ='application/json')

            elif not indice.isnumeric() and indice == 'None':
                indice = None

            elif not indice.isnumeric():
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/json')

            elif not int(indice) in range(1,72):
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/json')

            else:
                indice = int(indice)


            listaTokens,operacao = GerenteClasses.GetOpercaoes().GetAnaliseLexicoSemanticaOntoPT(texto.lower(), indice)
            arquivoJason = GerenteClasses.GetGeradorArquivoJson().GerarArquivoOntoPtJson(listaTokens, operacao)
            return HttpResponse(arquivoJason,content_type ='application/json')
         except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')




class GetAnaliseLexicoSemanticaOntoPtXML(APIView):

    def get(self, request, *args, **kw):
         try:

            texto = request.GET.get('texto_portugues')
            indice = request.GET.get('indice')


            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('texto_portugues'), content_type ='application/xml')

            if indice is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('indice'), content_type ='application/xml')

            elif not indice.isnumeric() and indice == 'None':
                indice = None

            elif not indice.isnumeric():
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/xml')

            elif not int(indice) in range(1,72):
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/xml')

            else:
                indice  = int(indice)


            listaTokens,operacao = GerenteClasses.GetOpercaoes().GetAnaliseLexicoSemanticaOntoPT(texto.lower(), indice)
            arquivoXML = GerenteClasses.GetGeradorArquivoXml().GerarArquivoOntoPtXml(listaTokens, operacao)
            return HttpResponse(arquivoXML,content_type ='application/xml')
         except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml(str(ex)), content_type ='application/xml')

#Fim Analisadores lexico semanticos





#Inicio full analisadores
class GetFullAnaliseJson(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            indice = request.GET.get('indice')


            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')
            if indice is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('indice'), content_type ='application/json')

            elif not indice.isnumeric() and indice == 'None':
                indice = None

            elif not indice.isnumeric():
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/json')

            elif not int(indice) in range(1,72):
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/json')

            else:
                indice  = int(indice)


            listaTokens,operacao = GerenteClasses.GetOpercaoes().GetFullAnalise(texto.lower(),indice,Constantes.TAGGERPADRAO)
            arquivoJason = GerenteClasses.GetGeradorArquivoJson().GerarArquivoFullAnaliseOntoPtJson(listaTokens, operacao, Constantes.TAGGERPADRAO)
            return HttpResponse(arquivoJason,content_type ='application/json')
        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')



class GetFullAnaliseXml(APIView):

    def get(self, request, *args, **kw):
         try:

            texto = request.GET.get('texto_portugues')
            indice = request.GET.get('indice')

            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('texto_portugues'), content_type ='application/xml')
            if indice is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('indice'), content_type ='application/xml')

            elif not indice.isnumeric() and indice == 'None':
                indice = None

            elif not indice.isnumeric():
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/xml')

            elif not int(indice) in range(1,72):
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/xml')

            else:
                indice  = int(indice)


            listaTokens,operacao = GerenteClasses.GetOpercaoes().GetFullAnalise(texto.lower(),indice,Constantes.TAGGERPADRAO)
            arquivoXML = GerenteClasses.GetGeradorArquivoXml().GerarArquivoFullAnaliseOntoPtXml(listaTokens, operacao, Constantes.TAGGERPADRAO)
            return HttpResponse(arquivoXML,content_type ='application/xml')
         except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml(str(ex)), content_type ='application/xml')




class GetFullAnaliseTreeTaggerJson(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            indice = request.GET.get('indice')


            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')
            if indice is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('indice'), content_type ='application/json')

            elif not indice.isnumeric() and indice == 'None':
                indice = None

            elif not indice.isnumeric():
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/json')

            elif not int(indice) in range(1,72):
                return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/json')

            else:
                indice  = int(indice)


            listaTokens,operacao = GerenteClasses.GetOpercaoes().GetFullAnalise(texto,indice,Constantes.TAGGERTREETAGGER)
            arquivoJason = GerenteClasses.GetGeradorArquivoJson().GerarArquivoFullAnaliseOntoPtJson(listaTokens, operacao, Constantes.TAGGERTREETAGGER)
            return HttpResponse(arquivoJason,content_type ='application/json')
        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')





class GetFullAnaliseTreeTaggerXml(APIView):

    def get(self, request, *args, **kw):
         try:

            texto = request.GET.get('texto_portugues')
            indice = request.GET.get('indice')

            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('texto_portugues'), content_type ='application/xml')
            if indice is None:
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GeerarArquivoKeyErroXml('indice'), content_type ='application/xml')

            elif not indice.isnumeric() and indice == 'None':
                indice = None

            elif not indice.isnumeric():
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/xml')

            elif not int(indice) in range(1,72):
                return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml('Parâmetro indice deve ser um inteiro entre 1 e 72 ou ser None.'), content_type ='application/xml')

            else:
                indice  = int(indice)


            listaTokens,operacao = GerenteClasses.GetOpercaoes().GetFullAnalise(texto,indice,Constantes.TAGGERTREETAGGER)
            arquivoXML = GerenteClasses.GetGeradorArquivoXml().GerarArquivoFullAnaliseOntoPtXml(listaTokens, operacao, Constantes.TAGGERTREETAGGER)
            return HttpResponse(arquivoXML,content_type ='application/xml')
         except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoXml().GerarArquivoErroXml(str(ex)), content_type ='application/xml')
#Fim full analisadores



class GetFullAnaliseTreeTaggerOWNJson(APIView):

    def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')

            listaTokens = GerenteClasses.GetOpercaoes().GetFullAnaliseOWN(texto)
            arquivoJason = GerenteClasses.GetGeradorArquivoJson().GerarArquivoFullAnaliseOWN(listaTokens)
            return HttpResponse(arquivoJason,content_type ='application/json')
        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')


class GetSentenceTokenizer(APIView):
     def get(self, request, *args, **kw):
        try:

            texto = request.GET.get('texto_portugues')
            if texto is None:
                 return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivokeyErroJson('texto_portugues'), content_type ='application/json')

            listSentences = GerenteClasses.GetOpercaoes().SentenceTokenizer(texto=texto)
            arquivoJson = GerenteClasses.GetGeradorArquivoJson().GerarArquivoSentences(listSentences)
            return HttpResponse(arquivoJson,content_type ='application/json')

        except Exception as ex:
            return HttpResponse(GerenteClasses.GetGeradorArquivoJson().GerarArquivoErroJson(str(ex)), content_type ='application/json')