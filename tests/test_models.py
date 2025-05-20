from tzafon.models import ActionType, Command, Result


def test_command_roundtrip():
    cmd = Command(ActionType.GOTO, url="https://example.com", timeout=1234)
    assert Command.load(cmd.dump()) == cmd


def test_result_roundtrip():
    r1 = Result(success=True, image=b"\xff\xd8")
    assert Result.load(r1.dump()) == r1
