f=open('/home/sajan/sajan/python/american-english.txt')
k=open('demo.txt','w+')
l=[x for x in f.read().split('\n')]
print(len(l))
for i in l:
	k.write(str(i).upper()+'\n')
k.close()
f.close()
