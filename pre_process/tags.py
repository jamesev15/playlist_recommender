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

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")


class MusicTag(BaseModel):
    emotions: list[str]
    feelings: list[str]
    moods: list[str]

    def printify(self) -> str:
        return ",".join(self.emotions + self.feelings + self.moods)


def get_music_tags(music: Music) -> MusicTag:
    system_prompt = f"""
    The user will enter a music name with the artists related to the music.

    Your task is the following

    1. Find the emotions, feelings and moods related to the music. Be detailed
    2. Compose a JSON which contains the information of the point 1.
    3. As output, return only the JSON, without any explanation. Please be sure that your 
       output is only a JSON.
       The JSON will contain the keys: music_name, artists, emotions, feelings, moods


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

    return MusicTag.parse_obj(json.loads(response))
