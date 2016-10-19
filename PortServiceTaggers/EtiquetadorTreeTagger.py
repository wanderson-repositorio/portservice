import os
from subprocess import Popen, PIPE
from nltk.internals import find_binary, find_file
from nltk.tag.api import TaggerI
from PortServiceModelos.Token import Token

tagger = None

_treetagger_url = 'http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/'

_treetagger_languages = ['bulgarian', 'dutch', 'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'italian', 'polish', 'russian', 'slovak', 'slovak2', 'spanish','portuguese']

class EtiquetadorTreeTagger(TaggerI):

    def __init__(self, path_to_home=None, language='german',verbose=False, abbreviation_list=None):

        treetagger_paths = ['.', '/usr/bin', '/usr/local/bin', '/opt/local/bin',
                            '/Applications/bin', '~/bin', '~/Applications/bin',
                            '~/work/tmp/treetagger/cmd', '~/tree-tagger/cmd',
                            '/home/wanderson/Documentos/Tagger/cmd','/home/wanderson/Documentos/TreeTagger/cmd',
                            '/home/portservice/TreeTagger/cmd']


        treetagger_paths = list(map(os.path.expanduser, treetagger_paths))
        self._abbr_list = abbreviation_list

        if language in _treetagger_languages:
            treetagger_bin_name = 'tree-tagger-' + language
        else:
            raise LookupError('Language not in language list!')

        try:
            self._treetagger_bin = find_binary(
                treetagger_bin_name, path_to_home,
                env_vars=('TREETAGGER', 'TREETAGGER_HOME'),
                searchpath=treetagger_paths,
                url=None,
                verbose=verbose)
        except LookupError:
            print('NLTK was unable to find the TreeTagger bin!')

    def tag(self, sentences):

        # Write the actual sentences to the temporary input file
        if isinstance(sentences, list):
            _input = '\n'.join((x for x in sentences))
        else:
            _input = sentences

        # Run the tagger and get the output
        if(self._abbr_list is None):
            p = Popen([self._treetagger_bin], 
                        shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        elif(self._abbr_list is not None):
            p = Popen([self._treetagger_bin,"-a",self._abbr_list], 
                        shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        
        (stdout, stderr) = p.communicate(bytes(_input, 'UTF-8'))

        # Check the return code.
        if p.returncode != 0:
            print(stderr)
            raise OSError('TreeTagger command failed!')

        treetagger_output = stdout.decode('UTF-8')

        # Output the tagged sentences
        tagged_sentences = []
        for tagged_word in treetagger_output.strip().split('\n'):
            tagged_word_split = tagged_word.split('\t')
            tagged_sentences.append(tagged_word_split)

        return tagged_sentences



    def GetMarcacaoMorfossintaticaTreeTagger(self,texto):
        listaTokensEtiquetados = list()
        try:
            sentencasMarcadas = tagger.tag(texto)
            for sent in sentencasMarcadas:
                token = Token()
                token.Token = sent[0]
                token.ClasseGramatical = sent[1]
                token.Lema = sent[2]
                listaTokensEtiquetados.append(token)
            return listaTokensEtiquetados

        except Exception as ex:
            print(ex)
            return None




if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
