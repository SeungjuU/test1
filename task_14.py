with open('text_14.txt','w') as fw:
    with open('test.txt','r') as fr:
        for line in fr:
            fw.write(line)
    
    fw.write('12345\n')
    fw.write('ACGTACGT\n')

