import pytest
from tzafon.client import Waypoint
from tzafon.models import Command, Result, ActionType


class DummyConn:
    def __init__(self):
        self.sent = []

    async def connect(self):
        ...

    async def close(self):
        ...

    @property
    def is_open(self):
        return True

    async def send(self, cmd: Command):
        self.sent.append(cmd)
        return Result(
            success=True,
            image=b"\xff\xd8" if cmd.action_type == ActionType.SCREENSHOT else None,
        )


@pytest.mark.asyncio
async def test_screenshot_happy_path(monkeypatch, tmp_path):
    dummy = DummyConn()
    monkeypatch.setattr("tzafon.client._WsConnection", lambda *a, **k: dummy)
    async with Waypoint(token="wpk_dummy") as wp:
        img = await wp.screenshot(tmp_path / "shot.jpg")
        assert img.startswith(b"\xff\xd8")
        assert (tmp_path / "shot.jpg").exists()
