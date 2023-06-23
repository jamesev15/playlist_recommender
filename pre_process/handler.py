from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from langchain.docstore.document import Document

from playlist.music import get_music_history, Music
from pre_process.tags import get_music_tags, MusicTag


def get_music_documents(
    music_history: list[Music], music_tags: list[MusicTag]
) -> list[Document]:
    documents: list[Document] = []
    for music, music_tag in zip(music_history, music_tags):
        documents.append(
            Document(page_content=music_tag.printify(), metadata=music.dict())
        )

    return documents


if __name__ == "__main__":
    music_history: list[Music] = get_music_history()
    music_tags: list[MusicTag] = list(map(get_music_tags, music_history))

    music_documents = get_music_documents(
        music_history=music_history, music_tags=music_tags
    )

    vector_store = FAISS.from_documents(
        documents=music_documents, embedding=OpenAIEmbeddings()
    )

    vector_store.save_local("vector_store")
