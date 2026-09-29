from app import app

def test_health():
    assert app.test_client().get("/health").status_code == 200

def test_home():
    assert b"Hello" in app.test_client().get("/").data
