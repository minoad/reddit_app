from reddit import user

TEST_USERS = [
    "ricardoroddy1",
    "minoad_script",
    "Arkjump",
    "TheTorontoExplorer",
    "xomaleo",
    "esi_disi",
]


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
    user_test()
    n = []
