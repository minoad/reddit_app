from dataclasses import dataclass
from typing import List

from praw import Reddit

from reddit import client, types


def _create_dict_from_class(cls, data: dict) -> dict:
    """
    Recieves a class and a dict.  Constructs a dict containing only members of the class.
    """
    return {
        k: v
        for k, v in data.__dict__.items()
        if k in [k for k in cls.__dict__ if not k.startswith("_") and k != "type"]
    }


@dataclass()
class Subreddit:
    """
    A subreddit has comments made by users.
    A subreddit has submissions made by users.
    """

    name: str
    sort: str = "new"
    limit: int = 10
    over18: bool = False
    subscribers: int = 0
    title: str = ""
    url: str = ""
    accounts_active: str = ""
    display_name: str = ""

    def __parse_comments(self, data: list):
        self.comments: List[Reddit.Redditor] = [
            types.Comment(**_create_dict_from_class(types.Comment, comment))
            for comment in data
        ]

    def get_subreddit(self):
        self.subreddit_data = client.Client().client.subreddit(self.name)
        self.over18 = self.subreddit_data.over18
        self.subscribers = self.subreddit_data.subscribers
        self.title = self.subreddit_data.title
        self.url = self.subreddit_data.url
        self.accounts_active = self.subreddit_data.accounts_active
        self.display_name = self.subreddit_data.display_name

        self.__parse_comments(list(self.subreddit_data.comments(limit=self.limit)))
        # self.__raw_submissions = self.subreddit_data.submissions(limit=self.limit)
        print("a")

    def get_users(self) -> list:
        """
        Get a list of users who have made comments in the subreddit.
        """
        n = [comment.author.name for comment in self.comments]
        print("a")
        return n

    def __post_init__(self):
        self.get_subreddit()
