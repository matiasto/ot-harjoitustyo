import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    # Alussa

    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaate_alussa_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    # Edullisesti kateisella

    def test_riittavalla_maksulla_edullisesti_kateisella_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_vajaalla_maksulla_edullisesti_kateisella_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_tasa_maksulla_edullisesti_kateisella_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    # Maukkaasti kateisella

    def test_riittavalla_maksulla_maukkaasti_kateisella_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_vajaalla_maksulla_maukkaasti_kateisella_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_tasa_maksulla_maukkaasti_kateisella_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # Edullisesti kortilla

    def test_riittavalla_saldolla_edullisesti_kortilla_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kortti.saldo, 760)

    def test_vajaalla_saldolla_edullisesti_kortilla_toimii_oikein(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kortti.saldo, 100)

    def test_tasa_saldolla_edullisesti_kortilla_toimii_oikein(self):
        self.kortti.ota_rahaa(760)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kortti.saldo, 0)

    # Maukkaasti kortilla

    def test_riittavalla_saldolla_maukkaasti_kortilla_toimii_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kortti.saldo, 600)

    def test_vajaalla_saldolla_maukkaasti_kortilla_toimii_oikein(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kortti.saldo, 100)

    def test_tasa_saldolla_maukkaasti_kortilla_toimii_oikein(self):
        self.kortti.ota_rahaa(600)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kortti.saldo, 0)

    def test_kassapaatteen_saldo_ei_muutu_kortilla_ostaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Rahan lataaminen

    def test_lataa_rahaa_toimii_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.kortti.saldo, 1100)

    def test_lataa_rahaa_ei_hyvaksy_negatiivista_summaa(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.kortti, -10), None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
