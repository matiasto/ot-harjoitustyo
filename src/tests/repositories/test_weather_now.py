from tkinter.messagebox import NO
import unittest
from entities import WeatherNow


class TestWeatherNow(unittest.TestCase):
    def setUp(self):
        self.mock_data = {
            "coord": {
                "lon": -122.08,
                "lat": 37.39
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 282.55,
                "feels_like": 281.86,
                "temp_min": 280.37,
                "temp_max": 284.26,
                "pressure": 1023,
                "humidity": 100
            },
            "visibility": 10000,
            "wind": {
                "speed": 1.5,
                "deg": 350
            },
            "clouds": {
                "all": 1
            },
            "dt": 1560350645,
            "sys": {
                "type": 1,
                "id": 5122,
                "message": 0.0139,
                "country": "US",
                "sunrise": 1560343627,
                "sunset": 1560396563
            },
            "timezone": -25200,
            "id": 420006353,
            "name": "Mountain View",
            "cod": 200
        }
        self.weather_now = WeatherNow("testi", self.mock_data)

    def test_obj_exists(self):
        self.assertNotEqual(self.weather_now, None)

    def test_temperature_correct(self):
        self.assertEqual(self.weather_now.temperature, 282.55)

    def test_humidity_correct(self):
        self.assertEqual(self.weather_now.humidity, 100)

    def test_pressure_correct(self):
        self.assertEqual(self.weather_now.pressure, 1023)

    def test_report_correct(self):
        self.assertEqual(self.weather_now.report, "Clear")


    
