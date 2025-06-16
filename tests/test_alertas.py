import unittest
from unittest.mock import patch
from app import app

class test_alertas(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    @patch('app.getAlerts') #SIMULA LA FUNCIÓN GET ALERTS
    def test_listar_alertas(self, simulador_getAlerts):
        simulador_getAlerts.return_value = [
            {'id': 1, 'mensaje': 'Alerta 1'},
            {'id': 2, 'mensaje': 'Alerta 2'}
        ]

        response = self.app.get('/alertas')#SIMULAMOS UN CLIENTE PARA QUE HAGA LA SOLICITUD
        self.assertEqual(response.status_code, 200) #VERIFICAMOS SI EL CODIGO QUE DEVOLVIÓ ES 200

        expected = [
            {'id': 1, 'mensaje': 'Alerta 1'},
            {'id': 2, 'mensaje': 'Alerta 2'}
        ]
        self.assertEqual(response.get_json(), expected) #VERIFICAMOS SI LO QUE DEVOLVIÓ ES LO MISMO

if __name__ == '__main__':
    unittest.main()