import requests
from io import BytesIO
from PIL import Image, ImageTk
from .config_service import ConfigService

class IconService:
    def __init__(self) -> None:
        self.__base_url = ConfigService().icon_url

    def geticon(self, iconcode: str) -> object:
        url = f"{self.__base_url}{iconcode}@2x.png"
        response_img = requests.get(url)
        raw_data = response_img.content
        img_data = Image.open(BytesIO(raw_data))
        img = ImageTk.PhotoImage(img_data)
        return img