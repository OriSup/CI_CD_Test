from main import greet

def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()

    assert captureed.out == "Bonjour, Alice !\n"