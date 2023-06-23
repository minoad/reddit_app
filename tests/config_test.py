import pytest

# from reddit import *
# from reddit.config import Config
from reddit import config


def config_test():
    c = config.Config()
    assert c.user_agent == "minoad_script"


def run_tests():
    config_test()


if __name__ == "__main__":
    run_tests()
