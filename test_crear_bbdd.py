import unittest
import sqlite3
from crear_bbdd import afegir_grup, mostrar_grups, eliminar_grup, actualitzar_grup, crear_base_dades

class TestGestorMusica(unittest.TestCase):

    def setUp(self):

        crear_base_dades()
        conn = sqlite3.connect("grups.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM grups")
        conn.commit()
        conn.close()

    def test_afegir_grup(self):
        afegir_grup("Txarango", 2010, "pop", 5)
        grups = mostrar_grups()
        self.assertIn(("Txarango", 2010, "pop", 5), grups)

    def test_eliminar_grup(self):
        afegir_grup("Sopa de Cabra", 1986, "rock", 4)
        eliminar_grup("Sopa de Cabra")
        grups = mostrar_grups()
        self.assertNotIn(("Sopa de Cabra", 1986, "rock", 4), grups)

    def test_actualitzar_grup(self):
        afegir_grup("Mishima", 2000, "pop", 4)
        actualitzar_grup("Mishima", 2001, "indie", 5)
        grups = mostrar_grups()
        self.assertIn(("Mishima", 2001, "indie", 5), grups)

    def test_mostrar_grups(self):
        afegir_grup("Buhos", 2012, "rock", 6)
        grups = mostrar_grups()
        self.assertTrue(len(grups) > 0)

if __name__ == '__main__':
    unittest.main()
