from dataclasses import dataclass, asdict, astuple

@dataclass
class QuoteRate:
  database: str = 'axsql'
  table: str = 'quote'
  column: str = 'quote_rate'
  
  
@dataclass(frozen=True)
class QuoteStatus:
  database: str = 'axsql'
  table: str = 'quote'
  column: str = 'quote_status'
