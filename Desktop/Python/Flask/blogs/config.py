import os

class Config:

    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://user:najma254@localhost/blogs'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevConfig(Config):

    DEBUG= True
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://user:najma254@localhost/blogs'
    SECRET_KEY='najma'
    ENV='development'


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")


config_options={
    'development':DevConfig,
    'production':ProdConfig
}