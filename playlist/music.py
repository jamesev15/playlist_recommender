import os

import requests
from pydantic import BaseModel

SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN")
BASE_URL = "https://api.spotify.com/"


class Artist(BaseModel):
    name: str


class Music(BaseModel):
    name: str
    artists: list[Artist]

    def printfy(self) -> str:
        return f'{self.name} | {",".join([artist.name for artist in self.artists])}'


def get_music_history(
    time_range: str = "short_term", limit: int = 8
) -> list[Music]:
    TRACKS_ENDPOINT = f"v1/me/top/tracks?time_range={time_range}&limit={limit}"

    headers = {"Authorization": f"Bearer {SPOTIFY_TOKEN}"}

    response = requests.get(
        url=f"{BASE_URL}{TRACKS_ENDPOINT}", headers=headers
    )

    return [Music.parse_obj(item) for item in response.json()["items"]]
