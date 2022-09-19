infile = open('sometext.txt','r')

words = infile.readline()

words = words.split()
count = dict()

for i in words:
    if i in count:
        count[i] +=1
    else:
        count[i]=1

    #WordFreq[i] = i.count(i)
    #count += WordFreq[i].count(i)
    #WordFreq[i] = count
             
print(count)
             




#print(WordFreq)

#print(words)

