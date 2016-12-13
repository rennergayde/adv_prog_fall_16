samp_dict = {
    0:10,
    1:20
}
samp_dict['2']=30

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)
#print dic1


key_guess = 'key_guess'
guess = dic1.get(key_guess)

#if not guess:
    #print "Sorry, no %s." % (key_guess)

#for i in dic1:
    #print dic1[i]

#for i in sorted(dic1.keys()):
    #print i, dic1[i]
for i in dic1:
    print i, dic1[i]
