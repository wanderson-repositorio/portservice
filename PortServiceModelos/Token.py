#!/usr/bin/python
# coding: utf-8

from PortServiceModelos.Significado import Significado

class Token(object):

    def __init__(self):
       self.Token = str('--')
       self.Lema = str('--')
       self.ClasseGramatical = str('--')
       self.Genero = str('--')
       self.Numero = str('--')

       self.SubCategoria = str('--')  #referente a advérbios  
       self.Pessoa = str('--') #referente a verbo
       self.Modo = str('--') #referente a verbo
       self.Tempo = str('--') #referente a verbo
       self.Tipo = str('--') #referente e verbo
       self.ListaSignificados = list()
       self.OperacaoExtraOntoPT = None

       
    
           
   
        
