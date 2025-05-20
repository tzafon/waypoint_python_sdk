import websockets
import pytest
from tzafon._connection import _WsConnection
from tzafon.models import Command, Result, ActionType


@pytest.mark.asyncio
async def test_send_roundtrip():
    async def handler(ws):
        _ = await ws.recv()
        await ws.send(Result(success=True).dump())

    async with websockets.serve(handler, "localhost", 8765):
        conn = _WsConnection("ws://localhost:8765")
        await conn.connect()
        res = await conn.send(Command(ActionType.GOTO, url="about:blank"))
        assert res.success is True
        await conn.close()
