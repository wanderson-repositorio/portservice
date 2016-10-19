
openWordNetPT = None

class ModelOpenWordNetPT(object):

    def __init__(self):
        self.SynsetId = str()
        self.Synset = str()
        self.Type = str()
        self.Word = str()
        self.Gloss = str()

class OpenWordNetPT(object):


    def GetSynsets(self,palavra):

        listModelOpenWordNetPT = list()

        query = openWordNetPT.query\
        (
            ''' select ?synsetId ?synset ?type ?gloss
            {
                ?w <https://w3id.org/own-pt/wn30/schema/lexicalForm> "'''+palavra+'''"@pt .
                ?ws <https://w3id.org/own-pt/wn30/schema/word> ?w .
                ?synset <https://w3id.org/own-pt/wn30/schema/containsWordSense> ?ws .
                ?synset <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                ?synset <https://w3id.org/own-pt/wn30/schema/synsetId> ?synsetId
                optional { ?synset <https://w3id.org/own-pt/wn30/schema/gloss> ?gloss . }
            }'''
        )

        for synsetId,synset,type,gloss in query:
            modelOpenWordNetPT = ModelOpenWordNetPT()
            modelOpenWordNetPT.Synset = synset
            modelOpenWordNetPT.SynsetId = synsetId
            modelOpenWordNetPT.Type = str(type).split('/')[6]
            if gloss != None:
                modelOpenWordNetPT.Gloss = gloss
            listModelOpenWordNetPT.append(modelOpenWordNetPT)

        return listModelOpenWordNetPT








