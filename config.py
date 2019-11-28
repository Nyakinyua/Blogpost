import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
   
   
   
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 