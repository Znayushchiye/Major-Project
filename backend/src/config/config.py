from src.config.dev_config import DevConfig
from src.config.prod_config import ProductionConfig

class Config:
   def __init__(self):
      self.dev_config = DevConfig()
      self.production_config = ProductionConfig()