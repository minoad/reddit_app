import os
from pathlib import Path

from reddit import store


def test_store():
    s = store.SQLiteStore("data/test.db")
    s.establish_store()
    assert Path(s.path).exists()
    assert s.path == "data/test.db"
    os.remove("data/test.db")


if __name__ == "__main__":
    test_store()
