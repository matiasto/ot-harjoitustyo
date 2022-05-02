from io import BytesIO
import requests
from PIL import Image, ImageTk
from .config_service import ConfigService


class IconService:
    """Serves the icons that describe the weather."""

    def __init__(self) -> None:
        self.__base_url = ConfigService().icon_url

    def geticon(self, iconcode: str) -> object:
        """Retrieves icon by id

        Uses icon id retrieved from WeatherService API call 
        to request an image from OpenWeather API endpoint.

        Args:
            iconcode (str): id("10d")

        Returns:
            object: tk compatible image.
        """
        
        url = f"{self.__base_url}{iconcode}@2x.png"
        response_img = requests.get(url)
        raw_data = response_img.content
        img_data = Image.open(BytesIO(raw_data))
        img = ImageTk.PhotoImage(img_data)
        return img
