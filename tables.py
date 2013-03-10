#!/usr/bin/python

class Table:
    def __init__(self, f, column_name = '', table=None):
        self.f = f
        self.column_name = column_name
        self.table = table

    def columns(self):
        cols = ()
        # Check parent if exists
        if self.table:
            cols += self.table.columns()
        cols += (self.column_name,)
        return cols

    def data(self, data):
        d = ()
        # Check parent if exists
        if self.table:
            d += self.table.data(data)
        d += (self.f(data),)
        return d

if __name__ == "__main__":

    test_data = [
        {
            'name':'Anna',
            'age':20,
            'country':'Sweden'
        },
        {
            'name':'Bob',
            'age':24,
            'country':'US'
        },
        {
            'name':'Cindy',
            'age':30,
            'country':'Great Britain'
        }
    ]

    t = Table(lambda x:x['country'], 'Country')
    t = Table(lambda x:x['name'], 'Name', t)
    t = Table(lambda x:x['age'], 'Age', t)
    print t.columns()
    for x in test_data:
        print t.data(x)
