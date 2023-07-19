import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала
    #api_key: Содержит API-ключ для работы с API YouTube
    #youtube: Объект, необходимый для работы с API
    """

    def __init__(self, channel_id='') -> None:
        """
        По информацию о канале по его id. Создает экземпляр класса Channel,
        где свойствами экземпляра являются различные данные о канале.
        """
        self.__channel_id = channel_id
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = channel['items'][0]['snippet']['customUrl']
        self.num_subscribers = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.total_views = channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @staticmethod
    def print_json(dict_to_print: dict) -> str:
        """Выводит словарь в json-подобном удобном формате с отступами"""

        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы YouTube API"""
        return build('youtube', 'v3', developerKey=os.getenv("YOU_TUBE_API"))

    def to_json(self, name_file):
        """
        Метод, который сохраняет словарь со значением атрибутов экземпляра Channel
        """
        with open(str(name_file), 'w+') as file:
            info_about_channel = self.print_json(self.__dict__)
            file.write(info_about_channel)
