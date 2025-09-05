import json
import threading
from pathlib import Path

# store path
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
USERS_FILE = DATA_DIR / "info.txt"
_LOCK = threading.Lock()

def _ensure_store():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not USERS_FILE.exists():
        USERS_FILE.write_text("[]", encoding="utf-8")  

def add_userdata(user_dict: dict):
    """Append a user to data/info.txt"""
    _ensure_store()
    with _LOCK:
        try:
            raw = USERS_FILE.read_text(encoding="utf-8")
            users = json.loads(raw)
            if not isinstance(users, list):
                users = []
        except (json.JSONDecodeError, FileNotFoundError):
            users = []

        users.append(user_dict)
        USERS_FILE.write_text(
            json.dumps(users, indent=2, ensure_ascii=False), encoding="utf-8"
        )

def read_usersdata() -> dict:
    """Return all users as {"data": [...]}"""
    _ensure_store()
    with _LOCK:
        try:
            raw = USERS_FILE.read_text(encoding="utf-8")
            users = json.loads(raw)
            if not isinstance(users, list):
                users = []
        except (json.JSONDecodeError, FileNotFoundError):
            users = []

    return {"data": users}
