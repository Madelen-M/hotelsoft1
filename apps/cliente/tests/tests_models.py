
from django.test import TestCase
from apps.cliente.models import Cliente,Nacionalidad

class ClienteTestCase(TestCase):
    def setUp(self):
        Cliente.objects.create(nombre="Pedro", direccion="CLL42 AC CR 116D", documento="1007481383",telefono = "3003426188")
        Cliente.objects.create(nombre="Ledis", direccion="cll 43 ac cre 23", documento="43577562",telefono = "3218146407")

    def test_clientes_tienen_nombre(self):
        """Los clientes pueden tener difinido su nombre   corectamente"""
        Pedro = Cliente.objects.get(nombre = "Pedro" )
        Ledis = Cliente.objects.get(nombre = "Ledis" )
        self.assertEqual(Pedro.nombre,Ledis.nombre,"Pedro")
        self.assertEqual(Ledis.nombre,Pedro.nombre,"Ledis")