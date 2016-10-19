#!/usr/bin/python
# coding: utf-8

from subprocess import *
import re as regex

MAPEAMENTO_CLASSE_GRAMATICAL = {'punct':'pu','punct2d':'pu_asp','punctg':'pu_exc','puncth':'pu_int','punct1a':'pu_vir',
                                'punctj':'pu_ret','punct1c':'pu_dp','punct2e':'pu_abe','punct1b':'pu_pv','puncti':'pu_fim',
                                'ppos':'det','pind':'det','pdem':'det','pint':'det','ppes':'pers','prel':'det','prep':'prep','in':'in',
                                'con':'con','nc':'n','np':'prop','adj':'adj','a_nc':'n_adj','art':'art','pass':'pass','v':'v','cp':'cp',
                                'punct2f':'punct_fec','card':'num_card','nord':'num_ord','adv':'adv'}

MAPEAMENTO_TIPO_PRONOME = {'ppos':'poss','pind':'ind','pdem':'dem','pint':'int','ppes':'pess','prel':'rel'}

MAPEAMENTO_TEMPO = {'p':'PR','pi':'IMPF ','pp':'PS','pmp':'MQP','f':'FUT','ip':'IP','inf':'INF','ppa':'PPA','pc':'PC','pic':'PIC','c':'COND',
                    'fc':'FC','g':'GER','i':'IMP'}


class JspellAcessInterface(object):
    PATERN_LEMA = u'(\w+)'
    PATERN_GATEGORIA = u'cat=(\w+)'
    PATERN_FSEM = u'fsem=(\w+)'
    PATER_DEF_ARTIGO = u'cla=(\w+)'
    PATERN_SUBCAT = u'subcat=(\w+)'
    PATERN_GENERO = u'g=(\w+)'
    PATERN_NUMERO = u'n=(\w+)'
    PATERN_PESSOA = u'p=(\w+)'
    PATERN_TEMPO = u',t=(\w+)'

    @staticmethod
    def ConsultarJspell(word):
        try:
            p = Popen('jspell -d port -a',stdin=PIPE, stdout=PIPE, stderr=PIPE)
            saida = str(p.communicate(word.encode('utf-8'))[0])
            p.terminate()
            p.kill()
            return saida
        except Exception as ex:           
            return None

    @staticmethod
    def ObeterMorphologiaJsepll(word):
        try:
            saida = JspellAcessInterface.ConsultarJspell(word)
            if saida != '*' and saida != None:
                return JspellAcessInterface.GetAtributos(saida.lower(), word)
            else:
                return None
        except:
            return None

    @staticmethod
    def GetAtributos(saida, palavra):

        try:
           
            genero = str('--')
            numero = str('--')
            lema = str('--')
            pessoa = str('--')
            tempo = str('--')
            subCategoria = str('--')
            tipo = str('--')
            listaSaida = saida.split('lex')[1].replace('(', '').replace(')', '').split(', ')

            pesquisa = JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_FSEM)

            if pesquisa != '--':
                categoria = MAPEAMENTO_CLASSE_GRAMATICAL[JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_GATEGORIA)]

                if categoria =='det':
                    tipo = MAPEAMENTO_TIPO_PRONOME[JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_GATEGORIA)]

                if categoria == 'adv':
                    subCategoria = JspellAcessInterface.GetPropriedades(listaSaida[3],JspellAcessInterface.PATERN_SUBCAT)

                elif categoria in ['nc','n']:
                    genero = JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_GENERO)
                    if genero == '_':
                        genero = '-'
                    numero = JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_NUMERO)

                lema = palavra


            else:
                lema = listaSaida[0]
                categoria = MAPEAMENTO_CLASSE_GRAMATICAL[JspellAcessInterface.GetPropriedades(listaSaida[1], JspellAcessInterface.PATERN_GATEGORIA)]



                if categoria in ['n', 'adj', 'pron', 'art', 'cp']:
                    genero = JspellAcessInterface.GetPropriedades(listaSaida[1], JspellAcessInterface.PATERN_GENERO)
                    if genero == '_':
                        genero = '-'
                    numero = JspellAcessInterface.GetPropriedades(listaSaida[1], JspellAcessInterface.PATERN_NUMERO)

                if categoria == 'art':
                    categoria += '-' + JspellAcessInterface.GetPropriedades(listaSaida[1],
                                                                            JspellAcessInterface.PATER_DEF_ARTIGO)

                if categoria == 'adv':
                    subCategoria = JspellAcessInterface.GetPropriedades(listaSaida[1],
                                                                        JspellAcessInterface.PATERN_SUBCAT)

                if tipo in ['poss', 'pess']:
                    genero = JspellAcessInterface.GetPropriedades(listaSaida[1], JspellAcessInterface.PATERN_GENERO)
                    numero = JspellAcessInterface.GetPropriedades(listaSaida[1], JspellAcessInterface.PATERN_NUMERO)
                    pessoa = JspellAcessInterface.GetPropriedades(listaSaida[1], JspellAcessInterface.PATERN_PESSOA)

                if categoria == 'v':
                    if listaSaida[3] != '[]':
                        pessoa = JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_PESSOA)
                        numero = JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_NUMERO)
                        tempo = MAPEAMENTO_TEMPO[JspellAcessInterface.GetPropriedades(listaSaida[3], JspellAcessInterface.PATERN_TEMPO)]
                    else:
                        tipo = 'v-inf'

            return [genero, numero.upper(), lema, pessoa.upper(), tempo.upper(), subCategoria.upper(), categoria.upper(),tipo.upper()]
        except Exception as erro:           
            return  None


    @staticmethod
    def GetPropriedades(item, patern):
        regexCompilado = regex.compile(patern, regex.U)
        pesquisa = regexCompilado.search(item)
        if pesquisa != None:
            atributo = pesquisa.group(1)
            return atributo
        return '--'


    @staticmethod
    def GetSubCategoriaAdverbio(palavra):
        saida = JspellAcessInterface.ConsultarJspell(palavra).lower()
        subCategoria = str('--')
        if saida[0] != '&':
            subCategoria = str(JspellAcessInterface.GetPropriedades(saida, JspellAcessInterface.PATERN_SUBCAT))

        return subCategoria
