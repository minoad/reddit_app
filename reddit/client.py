"""Return the reddit client provided by praw."""
from dataclasses import dataclass

from praw import Reddit

from reddit import config


@dataclass()
class Client:
    def __get_reddit_client(self) -> Reddit:
        client = Reddit(
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            password=self.config.password,
            user_agent=self.config.user_agent,
            username=self.config.username,
            read_only=self.config.read_only,
        )
        if not client.user.me():
            raise SystemError("Invalid credentials")
        return client

    def __post_init__(self):
        self.config = config.Config()
        self.client = self.__get_reddit_client()
