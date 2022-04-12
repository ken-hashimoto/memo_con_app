from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime,timedelta
import pytz
class MemoContents(Base):
  __tablename__ = 'memocontents' # テーブル名を設定
  # 作成するテーブルのカラムを定義
  Number = Column(Integer,primary_key = True)
  UserID = Column(String(20))
  Title = Column(String(128),default = "無題")
  Memo = Column(Text)
  Date = Column(DateTime,default=datetime.utcnow() + timedelta(hours=9))
  def __init__(self, UserID=None,Title=None, Memo=None, Date=None):
    self.UserID = UserID
    self.Title = Title
    self.Memo = Memo
    self.Date = Date
  def __repr__(self):
    return '<Title %r>' % (self.Title)

class User(Base):
    __tablename__ = 'users' # テーブル名を設定
    # 作成するテーブルのカラムを定義
    UserID = Column(String(20), primary_key=True)
    hashed_password = Column(String(128))

    def __init__(self, UserID=None, hashed_password=None):
        self.UserID = UserID
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<UserID %r>' % (self.UserID)