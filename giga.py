import asyncio
from typing import AsyncGenerator
from gigachat import GigaChat

from settings import settings


async def get_response_from_ai(prompt: str) -> str:
    async with GigaChat(
        credentials=settings.AI_API_KEY,
        verify_ssl_certs=False,
    ) as giga:

        resp = giga.chat(prompt)

        return resp.choices[0].message.content


async def get_giga_streaming(prompt: str) -> AsyncGenerator[str, None]:
    """Потоковая передача ответа от GigaChat (Streaming)"""
    full_text = await get_response_from_ai(prompt)

    for text in full_text.split():
        await asyncio.sleep(0.1)
        yield text + ' '
