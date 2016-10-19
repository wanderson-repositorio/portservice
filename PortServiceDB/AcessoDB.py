import pymysql

class AcessoDB(object):

    def GetConexao(self,database):
        conexao = pymysql.connect(user = 'portservice',password = '648273',host ='portservice.mysql.pythonanywhere-services.com',database = database, charset ="utf8",cursorclass=pymysql.cursors.DictCursor)
        cursor = conexao.cursor()
        return cursor



    def GetPropriedadesMorfossintaticaDB(self,token,id):

         cursor = self.GetConexao("portservice$portservice")
         try:
             query = cursor.execute(('''select m.classe_gramatical,m.tempo,m.pessoa,m.numero,m.genero,m.modo,m.tipo,m.sub_classe
                                        from morfologia m where m.identificador =%s limit 1'''),(id))
             if query > 0:
                 select = cursor.fetchone()                
                 classe_gramatical = select['classe_gramatical']
                 tempo = select['tempo']
                 pessoa = select['pessoa']
                 numero = select['numero']
                 genero = select['genero']
                 modo = select['modo']
                 tipo = select['tipo']
                 subClasse = select['sub_classe']
                 

                 query = cursor.execute(('''select l.lema from lemas l join flexao f on l.identificador = f.id_lema where f.flexao=%s'''),(token))
                 if query > 0 :
                     lema = cursor.fetchone()['lema']
                 else:
                     lema = self.GetLemaLexico(token)

                 return[lema,classe_gramatical,tempo,pessoa,numero,genero,modo,tipo,subClasse]

             else:
                 return None

         except Exception as ex:
             return None




    def GetLemaLexico(self,token):
        cursor = self.GetConexao("portservice$portservice")
        try:
             query = cursor.execute(('''select p.lema  from lexico p where p.flexao =%s limit 1'''),(token))
             if query > 0:
                 select = cursor.fetchone()   
                 lema = select['lema'] 
                 return lema
             else:
                 return '--'

        except Exception as ex:
            return None




    def GetPropriedadesDBLexico(self,token):
         cursor = self.GetConexao("portservice$portservice")
         try:
             query = cursor.execute(('''select p.lema,p.classe_gramatical,p.tempo,p.pessoa,p.numero,p.genero,p.modo,p.tipo,p.sub_classe
                                        from lexico p where p.flexao =%s limit 1'''),(token))
             if query > 0:
                 select = cursor.fetchone()   
                 lema = select['lema']           
                 classe_gramatical = select['classe_gramatical']
                 tempo = select['tempo']
                 pessoa = select['pessoa']
                 numero = select['numero']
                 genero = select['genero']
                 modo = select['modo']
                 tipo = select['tipo']
                 subClasse = select['sub_classe']                 
                 return[lema,classe_gramatical,tempo,pessoa,numero,genero,modo,tipo,subClasse]

             else:
                 return None

         except Exception as ex:
             return None





    def GetSynsetsPulo(self,lema):
        cursor = self.GetConexao("portservice$portservice")
        try:
            listaSignificados = list()
            query = cursor.execute(('''select  s.pos, s.gloss,s.offset from  wei_por_30_variant v , wei_por_30_synset s where v.word= %s and v.offset = s.offset'''),(lema))

            if query != 0:
                return cursor
            else:

                return None

        except Exception as ex:
             return None

        finally:
             cursor.close()


    def GetSinonimosPulo(self,id):
            cursor = self.GetConexao("portservice$portservice")

            try:
                listaPalavras = list()
                query = cursor.execute( ('select  v.word from  wei_por_30_variant v , wei_por_30_synset s where s.offset= %s and v.offset = s.offset'),(id))
                if query != 0:
                    return cursor
                else:
                    return None

            except Exception as ex:
                 return None

            finally:
                 cursor.close()
