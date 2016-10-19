from PortServiceJSON.Json import Json
from PortServiceOperacoes.Operacoes import Operacoes
from PortServiceXML.XML import XML
from PortServiceTaggers.EtiquetadorPadrao import EtiquetadorPadrao
from PortServiceTaggers.EtiquetadorFreeling import EtiquetadorFreeling
from PortServiceTaggers.EtiquetadorTreeTagger import EtiquetadorTreeTagger
from PortServiceWordNet.OntoPT import OntoPt
from PortServiceWordNet.Pulo import Pulo
from PortServiceDB.AcessoDB import AcessoDB
from PortServiceWordNet.OpenWordNetPT import OpenWordNetPT


class GerenteClasses(object):

    __geradorArquivoJson = None
    __geradorArquivoXml = None
    __operacoes = None
    __etiquetadorPadrao = None
    __etiquetadorFreeling = None
    __etiquetadorTreeTagger = None
    __ontoPt = None
    __acessoDB = None
    __pulo = None
    __openWordNetPT = None



    @staticmethod
    def GetGeradorArquivoJson():
        if GerenteClasses.__geradorArquivoJson == None:
            GerenteClasses.__geradorArquivoJson = Json()
        return GerenteClasses.__geradorArquivoJson


    @staticmethod
    def GetGeradorArquivoXml():
        if GerenteClasses.__geradorArquivoXml == None:
            GerenteClasses.__geradorArquivoXml = XML()
        return  GerenteClasses.__geradorArquivoXml


    @staticmethod
    def GetOpercaoes():
        if GerenteClasses.__operacoes == None:
            GerenteClasses.__operacoes = Operacoes()
        return  GerenteClasses.__operacoes


    @staticmethod
    def GetEtiquetadorPadrao():
        if GerenteClasses.__etiquetadorPadrao == None:
            GerenteClasses.__etiquetadorPadrao = EtiquetadorPadrao()
        return GerenteClasses.__etiquetadorPadrao


    @staticmethod
    def GetEtiquetadorFreeling():
        if GerenteClasses.__etiquetadorFreeling == None:
            GerenteClasses.__etiquetadorFreeling = EtiquetadorFreeling()
        return GerenteClasses.__etiquetadorFreeling

    @staticmethod
    def GetEtiquetadorTreeTagger():
        if GerenteClasses.__etiquetadorTreeTagger == None:
            GerenteClasses.__etiquetadorTreeTagger = EtiquetadorTreeTagger()
        return GerenteClasses.__etiquetadorTreeTagger


    @staticmethod
    def GetOntoPt():
        if GerenteClasses.__ontoPt == None:
            GerenteClasses.__ontoPt = OntoPt()
        return GerenteClasses.__ontoPt


    @staticmethod
    def GetPulo():
        if GerenteClasses.__pulo == None:
            GerenteClasses.__pulo = Pulo()
        return GerenteClasses.__pulo


    @staticmethod
    def GetAcessoDB():
        if GerenteClasses.__acessoDB == None:
            GerenteClasses.__acessoDB = AcessoDB()
        return GerenteClasses.__acessoDB

    @staticmethod
    def GetOpenWordNetPT():
        if GerenteClasses.__openWordNetPT == None:
            GerenteClasses.__openWordNetPT = OpenWordNetPT()
        return GerenteClasses.__openWordNetPT



