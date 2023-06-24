""" Main file"""
import sys

from reddit import subreddit, user


def app_run_default(
    subreddit_name: str = "askreddit", sort: str = "new", limit: int = 5
):
    """
    Default app run.
    Pick a subreddit and from n submissions based on `sort` type, get all of the users
    For each users get all comments and discussions
    Save to db.
    """
    #  [i.save_record(saver) for i in user.User(t_user).reddit_comments]
    users = [user.User(i, 2) for i in list(subreddit.Subreddit(subreddit_name, sort, limit).get_users())]
    print(users)
    print("a")
    
    
def default_analysis():
    # lets start by compiling a list of all users -> subreddit_names
    # # result -> bob -> [askreddit, funny, pics]
    # from users, get a list of all comments and submissions stacked
    # # fore each of these, get the subreddit name
    #subs = []
    #subs.extend([i.reddit_submissions for i in users])
    pass


def main() -> int:
    """Testing main"""
    app_run_default("askreddit", "new", 50)
    return 0


if __name__ == "__main__":
    sys.exit(main())
