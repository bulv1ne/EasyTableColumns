#!/usr/bin/python

class Table:
    def __init__(self, f, column_name = '', table=None):
        self.f = f
        self.column_name = column_name
        self.table = table

    def columns(self):
        return self.table.columns() + (self.column_name,) if self.table \
                else (self.column_name,)

    def data(self, data):
        return self.table.data(data) + (self.f(data),) if self.table \
                else (self.f(data),)

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
