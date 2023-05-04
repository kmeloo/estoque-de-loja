
import { encontrarErro } from './utilitarios.js';

$(function () {

    $(document).on("click", "#btIncluir", function () {

        var rota = 'http://191.52.7.82:5000/incluir_venda';

        var vetor_dados = $("#formulario").serializeArray();
 
        var chave_valor = {};
        for (var i = 0; i < vetor_dados.length; i++) {
            chave_valor[vetor_dados[i]['name']] = vetor_dados[i]['value'];
        }

        // convertendo para JSON
        var dados_json = JSON.stringify(chave_valor);

        // ajax
        var acao = $.ajax({
            url: rota,
            method: 'POST',
            dataType: 'json', // os dados são recebidos no formato json,
            contentType: 'application/json', // os dados serão enviados em json
            data: dados_json
        });

        acao.done(function (retorno) {
            try {
                if (retorno.resultado == "ok") {
                    alert("tudo cert :-)");
                } else {
                    alert("Deu algum erro :-( " + retorno.detalhes);
                }
            } catch (error) { 
                alert("Erro ao tentar fazer o ajax: " + error +
                    "\nResposta da ação: " + retorno);
            }
        });

        acao.fail(function (jqXHR, textStatus) {
            mensagem = encontrarErro(jqXHR, textStatus, rota);
            alert("Erro na chamada ajax: " + mensagem);
        });

    }); 
});
