import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from main import app, get_db
from services.database import Base

# Setup in-memory sqlite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def cleanup():
    # Before test
    yield
    # After test (no op here but good for future)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "running" in response.json().get("status", "").lower()

def test_get_games():
    # Test games endpoint
    response = client.get("/api/games?limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_repertoire_folders():
    response = client.get("/api/repertoire/folders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_repertoire_folder():
    folder_data = {"name": "Test Opening Folder", "color": "neon-blue"}
    response = client.post("/api/repertoire/folders", json=folder_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Opening Folder"
    assert data["color"] == "neon-blue"
    assert "id" in data

def test_parse_pgn_api():
    pgn_data = {
        "pgn": "[Event \"World Cup\"]\n[White \"Carlsen,M\"]\n[Black \"Bu Xiangzhi\"]\n[Result \"0-1\"]\n\n1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 0-1"
    }
    response = client.post("/api/parse-pgn", json=pgn_data)
    assert response.status_code == 200
    data = response.json()
    # PGN parser doesn't return headers by design
    assert "moves" in data
    assert "e4" in data["moves"]
    assert "fens" in data
    assert len(data["fens"]) > 0
