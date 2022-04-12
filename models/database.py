from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
#database.pyと同じパスにMemoCon.dbというファイルを絶対パスで定義
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'MemoCon.db')
#SQLiteを利用して上で定義した絶対パスにDBを構築
engine = create_engine(os.environ.get('DATABASE_URI') or 'sqlite:///' + databese_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base() #メタクラスというやつ
Base.query = db_session.query_property()

def init_db(): #DB初期化
    import models.models
    Base.metadata.create_all(bind=engine) #テーブルクラスのテーブルを生成