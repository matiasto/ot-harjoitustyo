from tkinter.messagebox import NO
import unittest
from services import WeatherService
from services import ConfigService

class TestWeatherService(unittest.TestCase):
    def setUp(self) -> None:
        self.weather_service = WeatherService()
        self.config_service = ConfigService()

    def test_weather_service_exists(self):
        self.assertNotEqual(self.weather_service, None)

    def test_request(self):
        url = self.config_service.geocoding_url + "q=" + "Espoo" + "&appid=" + self.config_service.api_key
        data = self.weather_service._WeatherService__request(url)[0]
        self.assertEqual(isinstance(data, dict), True)
        self.assertEqual(len(data) > 0, True)

        