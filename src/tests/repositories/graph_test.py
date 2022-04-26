from datetime import datetime
import unittest
from pandas import DataFrame
from entities.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.mock_data = [{
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
        },
            {
            "dt": 1618315999,
            "temp": 300.0,
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
                    "main": "clear",
                    "description": "clear sky",
                    "icon": "02d"
                }
            ],
            "pop": 0
        }]
        self.graph = Graph(self.mock_data)

    def test_obj_exists(self):
        self.assertNotEqual(self.graph, None)

    def test_data_type(self):
        self.assertEqual(isinstance(self.graph.data, DataFrame), True)

    def test_parse(self):
        test_df = DataFrame.from_dict({"time": [datetime.fromtimestamp(1618315200), datetime.fromtimestamp(
            1618315999)], "temp": [282.58, 300.0], "rain": [0, 0]})
        test_df = test_df.set_index("time")
        test_df = test_df.sort_index()

        self.assertEqual(self.graph.data.equals(test_df), True)

    def test_sort(self):
        self.assertEqual(
            self.graph.data.index[0], datetime.fromtimestamp(1618315200))
        self.assertEqual(
            self.graph.data.index[1], datetime.fromtimestamp(1618315999))
