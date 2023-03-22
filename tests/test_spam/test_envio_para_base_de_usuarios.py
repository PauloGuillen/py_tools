import pytest
from py_tools.spam.enviador_de_email import Enviador
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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'remetente@gmail.com',
        'Assunto',
        'Corpo do email'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='usuario_parametros', email='usuario_parametrose@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'remetente_parametros@gmail.com',
        'Assunto',
        'Corpo do email'
    )
    assert enviador.parametros_de_envio == (
        'remetente_parametros@gmail.com',
        'usuario_parametrose@gmail.com',
        'Assunto',
        'Corpo do email'
    )
