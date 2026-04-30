import aiofiles

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from giga import get_giga_streaming

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    async with aiofiles.open("index.html", 'r') as f:
        return await f.read()


@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        while True:
            data = await websocket.receive_json()
            async for chunk in get_giga_streaming(data["content"]):

                await websocket.send_json({
                    "type": "ai_response_chunk",
                    "content": chunk
                })

    except WebSocketDisconnect:
        pass
