from features.base_feature import BaseFeature

class QuoteStatus(BaseFeature):
  __database__ = 'axsql'
  __column__ = 'quote_rate'
    
  def __init__(self) -> None:
    super().__init__(self.__database__, self.__column__)
  
  def query():
    print('quote_status feature')
