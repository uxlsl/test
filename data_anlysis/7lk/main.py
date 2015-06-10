#-*- coding:utf-8 -*-
import pandas.io.sql as sql
import  sqlite3


def main():
    con = sqlite3.connect('db.sqlite3')
    frame = sql.read_sql('select * from goods_goodsdealer', con=con)
    goods_id = frame['goods_id'].value_counts()
    print(goods_id[:10])
    goods_id[:10].plot(kind='barh',rot=0)


if __name__ =='__main__':
    main()
