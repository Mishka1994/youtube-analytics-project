import os
from googleapiclient.discovery import build


#Создаем глобальную переменную, содержащую ключ от API YouTube
api_key: str = os.getenv('YOU_TUBE_API')


class Video:
    """

    В экземплярах данного класса содержится информация о конкретном видео
    с сайта YouTube
    video_id: индивидуальный id видео
    title: заголовок видео
    link: ссылка на видео
    view_count: количество просмотров
    like_count: количество лайков

    """
    def __init__(self, video_id):
        self.video_id = video_id
        # Получаем информацию о конкретном видео в виде словаря
        response = Video.get_yt_object().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=video_id
                                                             ).execute()
        self.title = response['items'][0]['snippet']['title']
        self.link = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count: int = response['items'][0]['statistics']['viewCount']
        self.like_count: int = response['items'][0]['statistics']['likeCount']

    def __repr__(self):
        return f"{self.__class__.__name__}({self.video_id}, {self.title}, {self.link}, {self.view_count},{self.like_count})"

    def __str__(self):
        return f"{self.title}"

    @classmethod
    def get_yt_object(cls):
        """ Создает специальный объект для работы с YouTube API"""
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class PLVideo(Video):
    """
    Класс наследует поведение от класса Video.
    При инициализации экзмепляра на вход принимается один доп. параметр
    play_list_id: id плейлиста

    """
    def __init__(self, video_id, play_list_id):
        super().__init__(video_id)
        self.play_list_id = play_list_id


#video1 = Video('AWX4JnAnjBE')
#video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')

#print(video1)
#print(video2)

#assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
#assert str(video2) == 'MoscowPython Meetup 78 - вступление'