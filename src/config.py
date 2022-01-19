import os  # new


class BaseConfig:
    TESTING = False
    SECRET_KEY = "my_precious"


class DevelopmentConfig(BaseConfig):
    TESTING = True


class TestingConfig(BaseConfig):
    TESTING = True


# class ProductionConfig(BaseConfig):
