class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email do rementente inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass
