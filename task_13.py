f= open("test.tst",'r')
line=f.xreadlines()
for s in line:
    print(s)
f.close()


'''
with open('test.txt','r') as frL
    for line in fr:
        print (line)  # line에도 엔터가 있어서 line.strip()으로 공백 없애줌
'''
#아래 방법 추천! with open
