import unittest
from entities.forecast import Forecast


class TestForecast(unittest.TestCase):
    def setUp(self):
        self.mock_data = {
            "dt": 1618308000,
            "sunrise": 1618282134,
            "sunset": 1618333901,
            "moonrise": 1618284960,
            "moonset": 1618339740,
            "moon_phase": 0.04,
            "temp": {
                "day": 279.79,
                "min": 275.09,
                "max": 284.07,
                "night": 275.09,
                "eve": 279.21,
                "morn": 278.49
            },
            "feels_like": {
                "day": 277.59,
                "night": 276.27,
                "eve": 276.49,
                "morn": 276.27
            },
            "pressure": 1020,
            "humidity": 81,
            "dew_point": 276.77,
            "wind_speed": 3.06,
            "wind_deg": 294,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 56,
            "pop": 0.2,
            "rain": 0.62,
            "uvi": 1.93
        }
        self.forecast = Forecast(self.mock_data)

    def test_obj_exists(self):
        self.assertNotEqual(self.forecast, None)

    def test_time(self):
        self.assertEqual(self.forecast.time, "Tuesday")

    def test_temperature(self):
        self.assertEqual(self.forecast.temperature, 279.79)

    def test_report(self):
        self.assertEqual(self.forecast.report, "light rain")

    def test_icon(self):
        self.assertEqual(self.forecast.icon, "10d")
