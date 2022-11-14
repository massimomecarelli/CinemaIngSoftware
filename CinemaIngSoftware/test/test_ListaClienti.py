from unittest import TestCase

from cliente.model.Cliente import Cliente
from lista_clienti.model.ListaClienti import ListaClienti


class TestListaClienti(TestCase):

    def crea_ambiente_test(self):
        self.lista_clienti = ListaClienti()
        cliente = Cliente("Mario", "Rossi", "Via Indirizzo", "123456789", "mariorossi", "password")
        self.lista_clienti.aggiungi_cliente(cliente)


    def test_rimuovi_cliente_by_user(self):
        self.crea_ambiente_test()
        self.assertFalse(self.lista_clienti.rimuovi_cliente_by_user("abcdef")) # deve dare False
        self.assertTrue(self.lista_clienti.rimuovi_cliente_by_user("mariorossi")) # deve sare True

    def test_get_cliente_by_user(self):
        self.crea_ambiente_test()
        self.assertIsNone(self.lista_clienti.get_cliente_by_user("abcdef"))
        self.assertIsNotNone(self.lista_clienti.get_cliente_by_user("mariorossi"))

    def test_get_lista_clienti(self):
        self.crea_ambiente_test()
        self.assertNotEqual(self.lista_clienti.get_lista_clienti(), []) # deve essere diverso da una lista vuota

