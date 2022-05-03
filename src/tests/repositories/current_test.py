import unittest
from entities.current import Current


class TestForecast(unittest.TestCase):
    def setUp(self):
        self.mock_data = {
            "dt": 1618317040,
            "sunrise": 1618282134,
            "sunset": 1618333901,
            "temp": 284.07,
            "feels_like": 282.84,
            "pressure": 1019,
            "humidity": 62,
            "dew_point": 277.08,
            "uvi": 0.89,
            "clouds": 0,
            "visibility": 10000,
            "wind_speed": 6,
            "wind_deg": 300,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "rain": {
                "1h": 0.21
            }
        }
        self.current = Current(self.mock_data)

    def test_obj_exists(self):
        self.assertNotEqual(self.current, None)

    def test_deg_to_cardinal(self):
        self.current._Current__deg_to_str(90)
        self.assertEqual(self.current.wind_deg, "East")

    def test_time(self):
        self.assertEqual(self.current.time, "15:30")

    def test_temperature(self):
        self.assertEqual(self.current.temperature, 284.07)

    def test_wind_speed(self):
        self.assertEqual(self.current.wind_speed, 6)

    def test_feels_like(self):
        self.assertEqual(self.current.feels_like, 282.84)

    def test_sunrise(self):
        self.assertEqual(self.current.sunrise, "05:48")

    def test_sunset(self):
        self.assertEqual(self.current.sunset, "20:11")

    def test_uvi(self):
        self.assertEqual(self.current.uvi, 0.89)

    def test_report(self):
        self.assertEqual(self.current.report, "light rain")

    def test_icon(self):
        self.assertEqual(self.current.icon, "10d")
