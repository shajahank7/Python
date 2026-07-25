import yaml

class ConfigReader:
    with open("EnvironmentConfig", "r") as f:
        config = yaml.safe_load(f)

    @staticmethod
    def get_url():
        return ConfigReader.config["url"]

    @staticmethod
    def get_browser():
        return ConfigReader.config["browser"]

    @staticmethod
    def get_username():
        return ConfigReader.config["username"]

    @staticmethod
    def get_password():
        return ConfigReader.config["password"]