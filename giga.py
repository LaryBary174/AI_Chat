import asyncio
from typing import AsyncGenerator
from gigachat import GigaChat

from settings import settings


async def giga_prompt(prompt: str) -> str:
    async with GigaChat(
        credentials=settings.AI_CREDENTIALS,
        verify_ssl_certs=False,
    ) as giga:

        resp = giga.chat(prompt)

        return resp.choices[0].message.content


async def giga_stream(prompt: str) -> AsyncGenerator[str, None]:
    full_text = await giga_prompt(prompt)

    for text in full_text.split():
        await asyncio.sleep(0.1)
        yield text + ' '



