""" Main file"""
import sys

from reddit import config


def main() -> int:
    """Testing main"""
    reddit_config = config.Config()
    print(reddit_config)
    return 0


if __name__ == "__main__":
    sys.exit(main())
