import unittest
from services import ConfigService


class TestConfigService(unittest.TestCase):
    def setUp(self):
        self.config_service = ConfigService()

    def test_config_service_exists(self):
        self.assertNotEqual(self.config_service, None)

    def test_initialize(self):
        self.assertNotEqual(self.config_service.open_weather_url, None)
        self.assertNotEqual(self.config_service.geocoding_url, None)
        self.assertNotEqual(self.config_service.icon_url, None)

    def test_openweather_url(self):
        self.assertEqual(self.config_service.open_weather_url,
                         "https://api.openweathermap.org/data/2.5/onecall")

    def test_geocoding_url(self):
        self.assertEqual(self.config_service.geocoding_url,
                         "http://api.openweathermap.org/geo/1.0/direct?")

    def test_icon_url(self):
        self.assertEqual(self.config_service.icon_url,
                         "http://openweathermap.org/img/wn/")

    def test_api_key(self):
        self.assertEqual(len(self.config_service.api_key) > 6, True)

    def test_api_key_is_set(self):
        self.assertEqual(self.config_service.api_key_is_set(), True)

    def test_api_key_validate(self):
        key = self.config_service.api_key
        self.assertEqual(self.config_service.set_api_key(""), False)
        self.assertEqual(self.config_service.set_api_key(key), True)

    def test_api_key_set(self):
        key = self.config_service.api_key
        self.config_service._ConfigService__api_key = ""
        self.assertEqual(self.config_service.api_key_is_set(), False)
        self.config_service.set_api_key(key)
        self.assertEqual(self.config_service.api_key_is_set(), True)
