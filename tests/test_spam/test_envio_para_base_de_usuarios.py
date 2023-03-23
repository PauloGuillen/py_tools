import pytest
from unittest.mock import Mock
from py_tools.spam.main import EnviadorDeSpam
from py_tools.spam.model import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='usuario_teste', email='usuario_teste@gmail.com'),
            Usuario(nome='Outro_usuario', email='Outro_usuario@gmail.com')
        ],
        [
            Usuario(nome='usuario_teste', email='usuario_teste@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'remetente@gmail.com',
        'Assunto',
        'Corpo do email'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='usuario_parametros', email='usuario_parametrose@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'remetente_parametros@gmail.com',
        'Assunto',
        'Corpo do email'
    )
    enviador.enviar.assert_called_once_with(
        'remetente_parametros@gmail.com',
        'usuario_parametrose@gmail.com',
        'Assunto',
        'Corpo do email'
    )
