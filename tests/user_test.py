from reddit import store, user

TEST_USERS = [
    "ricardoroddy1",
    "minoad_script",
    "Arkjump",
    "TheTorontoExplorer",
    "xomaleo",
    "esi_disi",
]


def comment_file_store_test():
    saver = store.FileStore("data/test.txt")
    user.User(TEST_USERS[3]).reddit_comments[0].save_record(saver)
    print("a")


def comment_sql_store_test():
    saver = store.SQLiteStore("data/test.db")
    user.User(TEST_USERS[3]).reddit_comments[0].save_record(saver)
    print("a")


def multiple_comment_sql_store_test():
    saver = store.SQLiteStore("data/test.db")
    [i.save_record(saver) for i in user.User(TEST_USERS[3]).reddit_comments]

    # [0].save_record(saver)
    print("a")


def multiple_comment_multiple_users_sql_store_test():
    saver = store.SQLiteStore("data/test.db")

    for t_user in TEST_USERS:
        [i.save_record(saver) for i in user.User(t_user).reddit_comments]

    # [0].save_record(saver)
    print("a")


def missing_username_test():
    u = user.User()


def valid_user_constructor_test():
    u = user.User(TEST_USERS[2])
    print("a")
    assert u.username == TEST_USERS[2]


# def valid_user_method_test():
#     u = user.User()
#     assert u.username == TEST_USERS[2]


def user_test():
    valid_user_constructor_test()


if __name__ == "__main__":
    multiple_comment_multiple_users_sql_store_test()
    # comment_file_store_test()
    # multiple_comment_sql_store_test()
    comment_sql_store_test()
    # user_test()
    # n = []
