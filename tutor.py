import csv


attn=['oshoke','louis','tayo']
path='registSymbolo2er.csv'

newlist=['tope','tayo','ojo','oshoke']

def search(val):
    if val in attn:
        return {1:val}
    else:
        return {0:val}

def reader():
    with open(path,'r') as reg:
        doc = reg.readline()
    yield doc
    #m= map(print,doc)
avail=map(search,newlist)


avail=map(search,newlist)
'''for i in avail:avail=map(search,newlist)
    print(i) '''
print(list(avail))
#print(reader())



print (list(reader()))


