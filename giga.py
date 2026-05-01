from typing import AsyncGenerator
from gigachat import GigaChat

from settings import settings


async def get_giga_streaming(prompt: str) -> AsyncGenerator[str, None]:
    """Потоковая передача ответа от GigaChat (Streaming)"""
    async with GigaChat(
        credentials=settings.AI_API_KEY,
        verify_ssl_certs=False,
    ) as giga:
        async for text in giga.astream(prompt):
            yield text.choices[0].delta.content
