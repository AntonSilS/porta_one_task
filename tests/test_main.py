from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

text = '''
The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"
'''

text_2 = "123"

def test_get_front():
    response = client.get("/")
    assert response.status_code == 200
    assert response.template.name == "front.html"
    assert b"Enter your text" in response.content


def test_receive_text_positive():
    response = client.post(
        "/unique_symbol",
        data={"sentence": text}
    )
    assert response.status_code == 200
    assert '<p class="result">m</p>' in response.text

def test_receive_text_negative():
    response = client.post(
        "/unique_symbol",
        data={"sentence": text}
    )
    assert response.status_code == 200
    assert '<p class="result">r</p>' not in response.text


def test_receive_text_negative_is_not_text():
    response = client.post(
        "/unique_symbol",
        data={"sentence": text_2}
    )
    assert response.status_code == 200
    assert '<p class="result">it is not a text!!!</p>' in response.text