class ControlloreCliente:

    def __init__(self, cliente):
        self.model = cliente

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_telefono_cliente(self):
        return self.model.telefono

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    def get_username_cliente(self):
        return self.model.username

    def get_password_cliente(self):
        return self.model.password
