import rdflib
from PortServiceModelos.Significado import Significado

ONTOLOGIA_ONTO_PT = None
DICIONARIO_OPERACOES = None


FORMA_LEXICAL = rdflib.term.URIRef(u'http://ontopt.dei.uc.pt/OntoPT.owl#formaLexical')
LABEL_ID_SYNSET = rdflib.term.URIRef(u'http://www.w3.org/2000/01/rdf-schema#label')
TYPE_SYNSET = rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
DEFINICAO = rdflib.term.URIRef(u'http://ontopt.dei.uc.pt/OntoPT.owl#definicao')


ANTONIMO_N_DE = rdflib.term.URIRef(u'http://ontopt.dei.uc.pt/OntoPT.owl#antonimoNDe')
ANTONIMO_ADV_DE = rdflib.term.URIRef(u'http://ontopt.dei.uc.pt/OntoPT.owl#antonimoAdvDe')
ANTONIMO_ADJ_DE = rdflib.term.URIRef(u'http://ontopt.dei.uc.pt/OntoPT.owl#antonimoAdjDe')
ANTONIMO_VE_DE = rdflib.term.URIRef(u'http://ontopt.dei.uc.pt/OntoPT.owl#antonimoVDe')

class OntoPt(object):

    def GetSynsets(self,palavra,operacao):
        o = rdflib.term.Literal(palavra)

        listaSignificados = list()
        query = ONTOLOGIA_ONTO_PT.query('select ?s ?p ?o where{?s ?p ?o .} limit 5',initBindings={'o':o})

        for s,p,o in query:
          significado = Significado()
          q = ONTOLOGIA_ONTO_PT.query('SELECT ?s ?p ?o WHERE { ?s ?p ?o .}',initBindings ={'s':s})

          for si,pi,oi in q:

            if pi == LABEL_ID_SYNSET:
                significado.SynsetId = str(oi)

            if pi == DEFINICAO:
                significado.Definicao = str(oi)

            if pi == FORMA_LEXICAL:
                if str(oi) not in significado.ListaFormasLexicais:
                    significado.ListaFormasLexicais.append(str(oi))

            if pi == TYPE_SYNSET:
                significado.ClasseGramatical = str(oi).split("#")[1]
               

            if pi in [ANTONIMO_ADJ_DE,ANTONIMO_ADV_DE,ANTONIMO_N_DE,ANTONIMO_VE_DE]:
                significado.ListaSynsetsAntonimos.append(self.GetPropiedades(oi))

            if operacao != None:
                if pi == rdflib.term.URIRef(u'http://ontopt.dei.uc.pt/OntoPT.owl#'+operacao):
                    significado.ListaSynsetsAnonimo.append(self.GetPropiedades(oi))

          listaSignificados.append(significado)
        
        return listaSignificados


    def GetPropiedades(self,URIRef):
        s = rdflib.URIRef(URIRef)
        query = ONTOLOGIA_ONTO_PT.query('SELECT ?s ?p ?o WHERE { ?s ?p ?o .}',initBindings ={'s':s})
        significado = Significado()
        for si,pi,oi in query:
            if pi == LABEL_ID_SYNSET:
                significado.SynsetId = str(oi)

            if pi == DEFINICAO:
                significado.Definicao = str(oi)

            if pi == FORMA_LEXICAL:
                if str(oi) not in significado.ListaFormasLexicais:
                    significado.ListaFormasLexicais.append(str(oi))

            if pi == TYPE_SYNSET:
                significado.ClasseGramatical = str(oi).split("#")[1]

        return significado

    def GetDicionarioOpercaoes(self,indice):
        return  DICIONARIO_OPERACOES[indice]









