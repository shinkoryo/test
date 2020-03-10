import pandas.tseries.offsets as offsets

d = {'nam_id': ['001', '002'], 
     'start_date': ['2019-11-11', '2019-11-10'],
     'len':[2,3],
     'drtnp':[1.34, 2.3]}
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(index=[])

for i in list(df.index):
    record = df.loc[i]
    for j in range(df.loc[i]['len']):
        record['len'] = j
        df2 = df2.append(record, ignore_index=True)        

df3 = pd.concat([df, df2])
def f1(df):
    return pd.to_datetime(df.start_date) + offsets.Day(df.len)

df3['start_date'] = df3[['start_date', 'len']].apply(f1, axis=1)  

df3

class Student():
    def get_score(self):
        return self._score

    def set_score(self, value):
        self._score = value

s = Student()

#print(s.get_score())

print(s.set_score(100))

print(s.get_score())


import bubbles

##########################################################################################################################################
#週末タスク: データの取得、　データの格納が実現できるようになること
#　GitLabの使い方
#input : RenewExshare PreproMktMoment
#output : FactorMoment
#PostGreSQL　DBとの連携について確認

import sqlalchemy


#データのインポートについて解決する必要がある

read_list = {'RenewExshare': {'date': '20190707', 'tblname': 'RenewExshare'},
             'PreproMktMoment': {'date': '20190707', 'tblname': 'PreproMktMoment'}
            }


class FFReader(Reader):
    @classmethod
    def read(cls, data_key : DataKey) -> DataProvider

        #DB接続

        #SQL文作成
        read_list = data_key

        #データ取得
        session = db_dev_coon.get_session()
        tmp_list = session.query(getattr(RenewExshare, 'nam_id'), getattr(RenewExshare, 'drtnp')).filiter(RenewExshare.date == date).all()
        session.close()

        return read_list



class DataProvider:
    def get_data(self)
        pass

    def set_data(self)
        pass

class EnrichedData:
    def get_data(self)
        pass

    def set_data(self)
        pass


class FFWriter(Writer):

    @classmethod
    def writer(cls, enriched_data: EnrichedData):
        #DB Connect

        #innsert
        session = db_dev_conn.get_session()
        session.execute(FactorMoment.__table__.innsert(), items)
        session.commit()
        session.close()
