from reddit import client


def test_client():
    c = client.Client()
    assert c.config.user_agent == "minoad_script"


if __name__ == "__main__":
    test_client()
