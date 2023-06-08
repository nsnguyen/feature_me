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

# from features.data_classes import QuoteRate, QuoteStatus

features = [QuoteRate, QuoteStatus]

def group_features(features):
  _group = {}
  for feature in features:
    if feature.table not in _group:
      _group[feature.table] = [feature]
    else:
      _group[feature.table].append(feature)
  return _group


def build_query(feature_group):
  if len(feature_group) == 1:
    # only a single table.
    _table_name = [i for i in feature_group][0]
    _columns = [i.column for i in feature_group[_table_name]]
    _template = f"SELECT {','.join(_columns)} FROM {_table_name}"   
  return _template

# build a list of features
feature_group = group_features([QuoteRate,
                                QuoteStatus])

query = build_query(feature_group)

breakpoint()