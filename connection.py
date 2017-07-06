import dataset

db = dataset.connect('mysql://root:123456@127.0.0.1/jwcoding')

print(db.tables)




