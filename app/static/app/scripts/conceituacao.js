function mensagem(titulo,mensagem) {

    bootbox.dialog({
        message: mensagem,
        title: titulo,
        animate: true,
        buttons: {
            danger: {
                label: "Entendi!",
                className: "btn-danger"
            }

        }
    });
}


//Parte do script referente ao modal de espera para concluir a tradução
var waitingDialog = (function ($) {

    var $dialog = $(
        '<div class="modal fade" data-backdrop="static" data-keyboard="false" tabindex="-1" role="dialog" aria-hidden="true" style="padding-top:15%; overflow-y:visible;">' +
        '<div class="modal-dialog modal-m">' +
        '<div class="modal-content">' +
        '<div class="modal-header text-center"><h3 style="margin:0;"></h3></div>' +
        '<div class="modal-body">' +
        '<div class="progress progress-striped active" style="margin-bottom:0;"><div class="progress-bar" style="width: 100%"></div></div>' +
        '</div>' +
        '</div></div></div>');

    return {

        show: function (message, options) {
            var settings = $.extend({
                dialogSize: 'm',
                progressType: 'success'
            }, options);
            if (typeof message === 'undefined') {
                message = 'Realizando análise...';
            }
            if (typeof options === 'undefined') {
                options = {};
            }

            $dialog.find('.modal-dialog').attr('class', 'modal-dialog').addClass('modal-' + settings.dialogSize);
            $dialog.find('.progress-bar').attr('class', 'progress-bar');
            if (settings.progressType) {
                $dialog.find('.progress-bar').addClass('progress-bar-' + settings.progressType);
            }
            $dialog.find('h3').text(message);
            $dialog.modal();
        },

        hide: function () {
            $dialog.modal('hide');
        }
    }

})(jQuery);
//fina da parte do modal de espera

function opercao() {
    var operacao = parseInt($("select#operacao option").filter(":selected").val())
    if (operacao == 1) {
        $("#tagger").prop("disabled", false);
    }
    else
        $("#tagger").prop("disabled", true);

    if (operacao == 2) {
        $("#wordnet").prop("disabled", false);
    }
    else
        $("#wordnet").prop("disabled", true);
}


$(document).ready(function () {
    opercao();

    $("#operacao").change(function () {
        opercao();
    });

    var objetoJson;
    $("#button_conceituar").click(function (e) {
        e.preventDefault();
        synsets.innerHTML = '';
        morphologia.innerHTML = '';


        var texto_portugues = $.trim($("#texto_portugues").val());

        if (texto_portugues == "") {
            mensagem("Atenção","Insira um texto para realizar a análise.");
            return;
        }

        var tipo_tarefa = parseInt($("select#operacao option").filter(":selected").val());
        var tipo_etiquetador = parseInt($("select#tagger option").filter(":selected").val());
        var tipo_wordnet = parseInt($("select#wordnet option").filter(":selected").val());

        var tarefa = "";
        var parametros;

        switch (tipo_tarefa) {
            case 1:

                if (tipo_etiquetador == 1)
                    tarefa = "get_analise_morfossintatica_padrao_json";
                else if (tipo_etiquetador == 2)
                    tarefa = "get_analise_morfossintatica_treetagger_json";

                parametros = {"texto_portugues": texto_portugues};
                break;

            case 2:

                if (tipo_wordnet == 1) {
                    tarefa = "get_analise_lexico_semantica_ontopt_json";
                    parametros = {"texto_portugues": texto_portugues, 'indice': 'None'};
                }
                else if (tipo_wordnet == 2) {
                    tarefa = "get_analise_lexico_semantica_pulo_json";
                    parametros = {"texto_portugues": texto_portugues};
                }
                break;

        }


        waitingDialog.show();
        $.ajax({
            type: "GET",
            url:"http://portservice.pythonanywhere.com/"+tarefa + "/",
            dataType: "json",
            contentType: "application/json",
            data: parametros,
            success: function (retorno) {
                waitingDialog.hide();
                objetoJson = retorno;
                preencher_texto_span(objetoJson, tipo_tarefa, tipo_etiquetador, tipo_wordnet);

            },

            error: function () {
                mensagem("Erro!!","Não foi possível executar a conceituação!!");
                waitingDialog.hide();
            }

        });

    });

});

function verificaPontuacao(token){
     vetorPontuacao = new Array("Faa","Fat","Fc","Fca","Fct","Fd","Fe","Fg","Fh","Fia","Fit","Fla",
                               "Flt","Fp","Fpa","Fpt","Fra","Frc","Fs","Ft","Fx","Fz","Fz","Fz","PU");

    for(var i = 0; i<vetorPontuacao.length;i++){
        if (vetorPontuacao[i] == token)
            return true
    }
    return false

}

function preencher_texto_span(objetoJson, tipo_tarefa, tipo_etiquetador, tipo_wordnet) {

    var html = '';
    for (var i = 0; i < objetoJson.texto.length; i++) {

        if (!verificaPontuacao(objetoJson.texto[i].token.pos))
            html += "<span>"+"  "+"</span><span id='" + i + "' class='word' style='cursor:pointer; border-radius:4px;'>"+ objetoJson.texto[i].token.palavra + "</span>";
        else
            html += "<span id='" + i + "' class='word' style='cursor:pointer; border-radius:4px;'>" + objetoJson.texto[i].token.palavra + "</span>";
    }

    tokens_retornados.innerHTML = html;

    $("#tokens_retornados > span").click(
        function () {
            indice = parseInt($(this).attr('id'));
            texto = objetoJson.texto[indice]
            if (tipo_tarefa == 1)
                preencher_morphologia(texto, tipo_etiquetador);

            else if (tipo_tarefa == 2) {
                prencher_synsets(texto, tipo_wordnet);
            }

        }
    );


    $("#tokens_retornados > .word").hover(
        function () {
            $(this).css('background-color', '#5bc0de').text();
        },

        function () {
            $(this).css('background-color', '');
        });
}


function prencher_synsets(texto, tipo_wordnet) {
    synsets.innerHTML = "";
    var html = '';

    for (var i = 0; i < texto.token.significados.length; i++) {
        var inicio = "<div class='row well'> <p>" +
            "<div class='info'> <p> <span>Definição:</span> " + texto.token.significados[i].definicao + "</p>" +
            "<p> <span>Identificador:</span> " + texto.token.significados[i].id + "<p><span>Classe Gramatical: </span>" + texto.token.significados[i].classe + "</p></div>";


        if (tipo_wordnet == 1) {
            var sinonimos = get_sinonimos(texto.token.significados[i], texto.token.palavra);
            var antonimos = get_antonimos(texto.token.significados[i], texto.token.palavra);
            html += inicio + sinonimos + antonimos + "</div>";
        }
        else if (tipo_wordnet == 2) {
            var sinonimos = get_sinonimos(texto.token.significados[i], texto.token.palavra);
            html += inicio + sinonimos + "</div>";
        }
    }

    synsets.innerHTML = html;
}


function get_sinonimos(significado, palavra) {
    var html = '';
    if (significado.lista_sinonimo != '--') {
        var propriedades = '';
        var inicio = "<div class='col-md-12'> <div class='panel panel-primary resposta'> <div class='panel-heading'><p><span>Formas lexicais sinônimas</span></p></div>"
        var final = "</div> </div>";
        var palavras = "";

        for (var i = 0; i < significado.lista_sinonimo.length; i++) {

            if (i < significado.lista_sinonimo.length - 1)
                palavras += significado.lista_sinonimo[i] + " - ";
            else
                palavras += significado.lista_sinonimo[i];
        }


        propriedades += "<p class='propriedades'> <span>Palavras: </span>" + palavras + "</p>";
        html += inicio + propriedades + final;
    }

    return html;

}


function get_antonimos(significado, palavra) {
    var html = '';
    if (significado.lista_antonimo != '--') {

        for (var i = 0; i < significado.lista_antonimo.length; i++) {

            var propriedades = '';
            var inicio = "<div class='col-md-12'> <div class='panel  panel-success resposta'> <div class='panel-heading'><p><span>Synsets antônimos</span></p></div>"
            var final = "</div> </div>";
            var palavras = "";
            for (var ii = 0; ii < significado.lista_antonimo[i].palavras.length; ii++) {

                if (ii < significado.lista_antonimo[i].palavras.length - 1)
                    palavras += significado.lista_antonimo[i].palavras[ii] +" - ";
                else
                    palavras += significado.lista_antonimo[i].palavras[ii];
            }

            propriedades += "<p class='propriedades'><span>Definição: </span>" + significado.lista_antonimo[i].definicao + "</p>" +
                "<p class='propriedades'><span>Identificador: </span>" + significado.lista_antonimo[i].id + "</p>" +
                "<p class='propriedades'><span>Classe Gramatical: </span>" + significado.lista_antonimo[i].classe + "</p>" +
                "<p class='propriedades'> <span>Palavras: </span>" + palavras + "</p>";


            html += inicio + propriedades + final;
        }
    }
    return html;

}

function preencher_morphologia(texto, tipo_etiquetador) {

    var propriedades = '';
    var html = '';
    var inicio = "<div class='row'><div class='col-md-6 well'> <div class='panel panel-danger resposta'> <div class='panel-heading'><p><span>Propriedades morfossintáticas</span></p></div>";
    var final = "</div> </div> </div>";

    propriedades += "<p class='propriedades'><span class='titulo'>Palavra: </span>" + texto.token.palavra + "</p>";
    if (texto.token.lema != '--')
        propriedades += "<p class='propriedades'><span class='titulo'>Lema: </span>" + texto.token.lema + "</p>";
    if (texto.token.pos != '--')
        propriedades += "<p class='propriedades'><span class='titulo'>Classe: </span>" + texto.token.pos + "</p>";
    if (texto.token.genero != '--')

        if (tipo_etiquetador == 1) {
            propriedades += "<p class='propriedades'><span class='titulo'>Genero: </span>" + texto.token.genero + "</p>";
            if (texto.token.numero != '--')
                propriedades += "<p class='propriedades'><span class='titulo'>Numero: </span>" + texto.token.numero + "</p>";
            if (texto.token.sub_class != '--')
                propriedades += "<p class='propriedades'><span class='titulo'>Sub-Categoria: </span>" + texto.token.sub_class + "</p>";
            if (texto.token.pessoa != '--')
                propriedades += "<p class='propriedades'><span class='titulo'>Pessoa: </span>" + texto.token.pessoa + "</p>";
            if (texto.token.modo != '--')
                propriedades += "<p class='propriedades'><span class='titulo'>Modo: </span>" + texto.token.modo + "</p>";
            if (texto.token.tempo != '--')
                propriedades += "<p class='propriedades'><span class='titulo'>Tempo: </span>" + texto.token.tempo + "</p>";
            if (texto.token.finitude != '--')
                propriedades += "<p class='propriedades'><span class='titulo'>Tipo: </span>" + texto.token.finitude + "</p>";
        }


    if (propriedades != '')
        html += inicio + propriedades + final;

    morphologia.innerHTML = html;
}

$('[data-toggle="collapse"]').on('click', function () {
    var $this = $(this),
        $parent = typeof $this.data('parent') !== 'undefined' ? $($this.data('parent')) : undefined;
    if ($parent === undefined) { /* Just toggle my  */
        $this.find('.glyphicon').toggleClass('glyphicon-plus glyphicon-minus');
        return true;
    }

    /* Open element will be close if parent !== undefined */
    var currentIcon = $this.find('.glyphicon');
    currentIcon.toggleClass('glyphicon-plus glyphicon-minus');
    $parent.find('.glyphicon').not(currentIcon).removeClass('glyphicon-minus').addClass('glyphicon-plus');

});