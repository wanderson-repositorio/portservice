from PortServiceModelos.Significado import Significado
import PortServiceGerenteClasses.GerenteClasses


class Pulo(object):


    def GetSynsets(self,lemma):
        cursorSynsets = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetAcessoDB().GetSynsetsPulo(lemma)

        if cursorSynsets != None:
            listaSignificados = list()
            synsets = cursorSynsets.fetchall()
            for syn in synsets:
                     significado = Significado()
                     significado.ClasseGramatical = syn['pos']
                     significado.Definicao = syn['gloss']
                     significado.SynsetId = syn['offset']
                     cursorSinonimosSynsets = PortServiceGerenteClasses.GerenteClasses.GerenteClasses.GetAcessoDB().GetSinonimosPulo(significado.SynsetId)
                     if cursorSinonimosSynsets != None:
                         for word in cursorSinonimosSynsets.fetchall():
                                significado.ListaFormasLexicais.append(word['word'])

                     listaSignificados.append(significado)
            return listaSignificados
        else:
            return None




