import pickle


shopListFile = 'shoplist.data'
shopList = ['apples', 'mango', 'carrot']

with open(shopListFile, 'wb') as f:
    pickle.dump(shopList, f)

del shopList

with open(shopListFile, 'rb') as f:
    storedList = pickle.load(f)
    print(storedList)
