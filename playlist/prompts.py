import json
import os
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from pydantic import BaseModel
from playlist.music import Music


class MusicTag(BaseModel):
    emotions: list[str]
    feelings: list[str]
    moods: list[str]

    def display_info(self) -> str:
        return ",".join(self.emotions + self.feelings + self.moods)


def get_music_tags(music: Music) -> MusicTag:
    system_prompt = f"""
    The user will enter a music name with the artists related to the music.

    Your task, behind scene, is the following

    1. Find the emotions, feelings and moods related to the music. Be detailed
    2. Compose a JSON which contains the information of the point 1. 
       The JSON will contain the keys: music_name, artists, emotions, feelings, moods
    3. As output, return only the JSON, without any explanation. Please be sure that your 
       output is only a JSON.

    """
    user_prompt = """
    music name: {music_name}
    artists: {artists}
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        template=system_prompt,
    )
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        template=user_prompt,
        input_variables=["music_name", "artists"],
    )
    prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt],
    )

    response = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt).run(
        music_name=music.name,
        artists=[artist.name for artist in music.artists],
    )

    print("Processing: ", music.display_info())
    print("Tags: ", response, "\n")

    return MusicTag.parse_obj(json.loads(response))
