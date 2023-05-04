import { encontrarErro } from './utilitarios.js';

$(function () {

    var rota = 'http://191.52.7.82:5000/listar_vendas';

    var acao = $.ajax({
        url: rota,
        dataType: 'json',
    });

    acao.done(function (retorno) {
        try {
            if (retorno.resultado == "ok") {
                for (var p of retorno.detalhes) {
                    var paragrafo = $("<p>");
                    paragrafo.html(`==> ${p.id}, ${p.cpf}, ${p.produto}, ${p.data}, ${p.quantidade}, ${p.preco_total}`);
                    $('#listagem').append(paragrafo);
                }
            } else {
                alert("Erro informado pelo backend: " + retorno.detalhes);
            }
        } catch (error) {
            alert("Erro ao tentar fazer o ajax: " + error +
                "\nResposta da ação: " + retorno.detalhes);
        }
    });

    acao.fail(function (jqXHR, textStatus) {
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });

});
