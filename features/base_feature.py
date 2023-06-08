import abc

class BaseFeatureError(Exception):
  pass

class BaseFeature(metaclass=abc.ABCMeta):
  def __init__(self, database, column) -> None:
    self.database = database
    self.column = column
    
  @abc.abstractmethod
  def query(self):
    pass