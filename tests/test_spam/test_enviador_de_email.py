import pytest
from py_tools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['email1@gmail.com', 'destino_2@gmail.com'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'email2.gmail.com',
        'Assunto do email',
        'Cortpo do email'
    )
    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['', 'destino_2gmail.com'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'email2.gmail.com',
            'Assunto do email',
            'Cortpo do email'
        )
        assert remetente in resultado
