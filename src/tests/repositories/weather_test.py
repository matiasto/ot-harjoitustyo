import unittest
from pandas import DataFrame
from entities import Weather


class TestWeather(unittest.TestCase):
    def setUp(self):
        self.mock_data_weather = {
            "lat": 33.44,
            "lon": -94.04,
            "timezone": "America/Chicago",
            "timezone_offset": -21600,
            "current": {
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
            },
            "minutely": [
                {
                    "dt": 1618317060,
                    "precipitation": 0.205
                }
            ],
            "hourly": [
                {
                    "dt": 1618315200,
                    "temp": 282.58,
                    "feels_like": 280.4,
                    "pressure": 1019,
                    "humidity": 68,
                    "dew_point": 276.98,
                    "uvi": 1.4,
                    "clouds": 19,
                    "visibility": 306,
                    "wind_speed": 4.12,
                    "wind_deg": 296,
                    "wind_gust": 7.33,
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ],
                    "pop": 0
                }
            ],
            "daily": [
                {
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
            ]
        }

        self.mock_data_historical = [
            {
                "dt": 1586390400,
                "temp": 278.41,
                "feels_like": 269.43,
                "pressure": 1006,
                "humidity": 65,
                "dew_point": 272.46,
                "clouds": 0,
                "wind_speed": 9.83,
                "wind_deg": 60,
                "wind_gust": 15.65,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01n"
                    }
                ]
            }
        ]
        self.weather = Weather(
            "testi", self.mock_data_weather, self.mock_data_historical)

    def test_obj_exists(self):
        self.assertNotEqual(self.weather, None)

    def test_has_current_weather_object(self):
        self.assertNotEqual(self.weather.current, None)
        self.assertEqual(isinstance(self.weather.current, object), True)

    def test_has_weather_forecast(self):
        self.assertEqual(len(self.weather.forecast), 1)
        self.assertEqual(isinstance(self.weather.forecast[0], object), True)

    def test_has_graph_data(self):
        self.assertEqual(isinstance(self.weather.graph, object), True)
        self.assertEqual(isinstance(self.weather.graph.data, DataFrame), True)
        self.assertEqual(len(self.weather.graph.data), 2)

    def test_city_name_correct(self):
        self.assertEqual(self.weather.city, "testi")
