from py_tools.spam.model import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='usuario_teste', email='usuario_teste@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='usuario_teste', email='usuario_teste@gmail.com'),
                Usuario(nome='Outro_usuario', email='Outro_usuario@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
