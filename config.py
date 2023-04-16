class BaseConfig:
    DEBUG = False
    TESTING = False
    # 他の共通設定


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8008
    # 開発環境用の設定


class ProductionConfig(BaseConfig):

    # 本番環境用の設定