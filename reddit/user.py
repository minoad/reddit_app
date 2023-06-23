from dataclasses import dataclass, field
from typing import List

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
class User:
    username: str = ""
    reddit_name: str = ""
    reddit_fullname: str = ""
    reddit_submissions: List = field(default_factory=list)
    reddit_comments: List = field(default_factory=list)

    # Helper function to create a dict comprehension that constructs a dict of fields we want.
    def __parse_submissions(self, data: List):
        """
        For all fields defined in the submission class, collect from results and set.
        To add a new field, simply add the field to the submission data class with a default value.
        """
        self.reddit_submissions = [
            types.Submission(**_create_dict_from_class(types.Submission, submission))
            for submission in data
        ]
        print("a")

    def __parse_comments(self, data: List):
        print("a")
        self.reddit_comments = [
            types.Comment(**_create_dict_from_class(types.Comment, comment))
            for comment in data
        ]
        print("a")

    def get_user(self, username: str = ""):
        if self.username == "" and not username:
            raise ValueError("Username must be provided")
        self.username = self.username or username
        self.user_data = client.Client().client.redditor(self.username)
        self.reddit_name = self.user_data.name
        self.reddit_fullname = self.user_data.fullname

        self.__parse_submissions(self.user_data.submissions.new())
        self.__parse_comments(self.user_data.comments.new())

        # TODO: get submissions into the correct class here
        print("a")
        # return self.client.client.user.me()

    def __post_init__(self):
        if self.username:
            self.get_user()
