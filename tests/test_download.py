import pytest
import pathlib
import src.adash as _


def test_download():
    url = "https://cdn.jsdelivr.net/npm/js-hello-world@1.0.0/helloWorld.js"
    path = "tmp/hello.js"
    p = pathlib.Path(path)
    assert not p.exists()
    assert _.download(url, p) == 1
    assert _.download(url, path) == 0
    text = p.read_text()
    assert 'console.log("Hello World");' in text
    p.unlink()


def test_download_unknown():
    url = "https://www.google.com/example"
    with pytest.warns(UserWarning) as record:
        assert _.download(url, "down_test.html") == 0
        assert record[0].message.args[0] == "404: Not Found"
        assert record[1].message.args[0] == "url: https://www.google.com/example"
