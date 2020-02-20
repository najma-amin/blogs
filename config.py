import os




class Config:
    debug = True
    SECRET_KEY = 'najma'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:najma254@localhost/blogs'
    
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:najma254@localhost/blogs'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
    
    



