from datetime import datetime
from django.conf.urls import patterns, url,include
from app import views



urlpatterns = patterns('',
                       url(r'^$', views.inicio, name='inicio'),
                       url(r'^consultar', views.consultar, name='consultar'),
                       url(r'^publicacoes', views.publicacoes, name='publicacoes'),
                       url(r'^instrucoes',views.instrucoes, name='instrucoes'),
                       url(r'^sobre$',views.sobre, name='sobre'),

                       url(r'^get_analise_morfossintatica_freeling_xml/$',views.GetAnaliseMorfossintaticaFreelingXML.as_view(),name='get_analise_morfossintatica_freeling_xml'),
                       url(r'^get_analise_morfossintatica_freeling_json/$',views.GetAnaliseMorfossintaticaFreelingJson.as_view(),name='get_analise_morfossintatica_freeling_json'),
                       url(r'^get_analise_morfossintatica_treetagger_json/$',views.GetAnaliseMorfossintaticaTreTaggerJson.as_view(),name='get_analise_morfossintatica_treetagger_json'),
                       url(r'^get_analise_morfossintatica_treetagger_xml/$',views.GetAnaliseMorfossintaticaTreTaggerXML.as_view(),name='get_analise_morfossintatica_treetagger_xml'),
                       url(r'^get_analise_morfossintatica_padrao_json/$', views.GetAnaliseMorfossintaticaJson.as_view(), name='get_analise_morfossintatica_padrao_json'),
                       url(r'^get_analise_morfossintatica_padrao_xml/$',views.GetAnaliseMorfossintaticaXML.as_view(),name ='get_analise_morfossintatica_padrao_xml'),

                       url(r'^get_full_analise_json/$',views.GetFullAnaliseJson.as_view(),name ='get_full_analise_json'),
                       url(r'^get_full_analise_xml/$',views.GetFullAnaliseXml.as_view(),name ='get_full_analise_xml'),
                       url(r'^get_full_analise_treetagger_json/$',views.GetFullAnaliseTreeTaggerJson.as_view(),name ='get_full_analise_treetagger_json'),
                       url(r'^get_full_analise_treetagger_xml/$',views.GetFullAnaliseTreeTaggerXml.as_view(),name ='get_full_analise_treetagger_xml'),

                       url(r'^get_analise_lexico_semantica_ontopt_json/$', views.GetAnaliseLexicoSemanticaOntoPtJson.as_view(), name ='get_analise_lexico_semantica_json'),
                       url(r'^get_analise_lexico_semantica_ontopt_xml/$', views.GetAnaliseLexicoSemanticaOntoPtXML.as_view(), name ='get_analise_lexico_semantica_xml'),
                       url(r'^get_analise_lexico_semantica_pulo_json/$',views.GetAnaliseLexicoSemanticaPuloJson.as_view(),name ='get_analise_lexico_semantica_pulo_json'),
                       url(r'^get_analise_lexico_semantica_pulo_xml/$',views.GetAnaliseLexicoSemanticaPuloXml.as_view(),name ='get_analise_lexico_semantica_pulo_xml'),
                       url(r'^get_analise_lexico_semantica_OWN_json/$',views.GetFullAnaliseTreeTaggerOWNJson.as_view(),name ='get_analise_lexico_semantica_OWN_json'),
                       url(r'^get_sentence_tokenizer/$',views.GetSentenceTokenizer.as_view(),name ='get_sentence_tokenizer'),
                       )

