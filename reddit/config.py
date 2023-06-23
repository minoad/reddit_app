"""
Configuration for reddit module
"""
from dataclasses import dataclass
from os import environ


@dataclass()
class Config:
    """
    By config order of precedence:
    1. Command Line
    2. Environment variables
    3. Config file

    """

    read_only: bool = True

    def __collect_cmd_line(self) -> bool:
        """Get config from command line"""
        return False

    def __collect_env_vars(self) -> bool:
        """
        All variables prepended with reddit_ will be assumed to be valid config items
        """
        envs = {
            "_".join(k.split("_")[1:]): v
            for k, v in environ.items()
            if k.startswith("reddit_")
        }
        try:
            self.client_id = envs["client_id"]
            self.client_secret = envs["client_secret"]
            self.password = envs["password"]
            self.username = envs["username"]
            self.user_agent = envs["username"]
        except KeyError:
            return False
        return True

    def __collect_config_file(self) -> bool:
        """Get config from predefined config file."""
        return False

    def __post_init__(self):
        for config_func in [
            self.__collect_cmd_line,
            self.__collect_env_vars,
            self.__collect_config_file,
        ]:
            if config_func():
                break
