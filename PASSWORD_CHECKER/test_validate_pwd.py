import unittest 
from validazione_pwd import validazione_password, validazione_password_con_messaggio_di_errore, validazione_password_con_regex


class TestValidatePwd(unittest.TestCase):
    def test_lunghezza_pwd(self):
        # Testa la lunghezza della password
        self.assertRaises(ValueError, validazione_password_con_regex, "1234567")
        self.assertRaises(ValueError, validazione_password_con_regex, "123456789012345678901")
        # Testare la presenza di almeno una lettera maiuscola
        self.assertRaises(ValueError, validazione_password_con_regex, "password")
        # Testare la presenza di almeno una lettera minuscola
        self.assertRaises(ValueError, validazione_password_con_regex, "PASSWORD")
        # Testare la presenza di almeno un numero
        self.assertRaises(ValueError, validazione_password_con_regex, "Password")
        # Testare la presenza di almeno un carattere speciale
        self.assertRaises(ValueError, validazione_password_con_regex, "Password1")
        
        

if __name__ == '__main__':

    # Esegui tutti i test
    unittest.main()