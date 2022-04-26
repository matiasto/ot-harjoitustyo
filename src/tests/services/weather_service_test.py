import unittest
from pandas import DataFrame
from services import WeatherService
from services import ConfigService


class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.weather_service = WeatherService()
        self.config_service = ConfigService()

    def test_weather_service_exists(self):
        self.assertNotEqual(self.weather_service, None)

    def test_request(self):
        url = self.config_service.geocoding_url + "q=" + \
            "Espoo" + "&appid=" + self.config_service.api_key
        data = self.weather_service._WeatherService__request(url)[0]
        self.assertEqual(isinstance(data, dict), True)
        self.assertEqual(len(data) > 0, True)

    def test_failed_request(self):
        with self.assertRaises(Exception):
            url = self.config_service.geocoding_url + "q=" + \
                "..." + "&appid=" + self.config_service.api_key
            self.weather_service._WeatherService__request(url)

    def test_location(self):
        data = self.weather_service._WeatherService__location("Espoo")
        self.assertEqual(data, ("60.2047672", "24.6568435"))

    def test_weather_data(self):
        data = self.weather_service._WeatherService__weather_data(
            "60.2047672", "24.6568435")
        self.assertEqual(isinstance(data, dict), True)
        self.assertEqual(isinstance(data["current"]["temp"], float), True)

    def test_historical_data(self):
        data = self.weather_service._WeatherService__historical_weather_data(
            "60.2047672", "24.6568435")
        self.assertEqual(isinstance(data, list), True)
        self.assertEqual(isinstance(data[0]["temp"], float), True)
        self.assertEqual(len(data) == 120, True)

    def test_weather(self):
        data = self.weather_service.weather("Espoo")
        self.assertEqual(isinstance(data.current.temperature, float), True)
        self.assertEqual(isinstance(data.current.report, str), True)
        self.assertEqual(len(data.forecast), 8)

    def test_graph(self):
        data = self.weather_service.weather("Espoo")
        self.assertEqual(isinstance(data.graph.data, DataFrame), True)
        self.assertEqual(len(data.graph.data) > 120, True)
