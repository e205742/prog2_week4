def line_count():
    """target.txtファイルの中身を１行ずつ取り出し、段落数を数える"""        
    num=[]
    file='target.txt'
    with open(file,'r') as fh:
        for line in fh.readlines()[::2]: #2,4行目が空なので、2,4行目を飛ばして読み込む
            line=line.rstrip() 
            num.append(line)

    print('target.txtには{}つの段落が含まれています。'.format(len(num)))    

line_count()

def word_count01():
    """target.txtの１行目に含まれる、総単語数を調べる"""
    file='target.txt'
    with open(file,'r') as f:
        for line01 in f.readlines()[:1]:
            line01=line01.split(' ')
            word01=len(line01) 
            
    return word01
        
def word_count02():
    """target.txtの２行目に含まれる、総単語数を調べる"""
    file='target.txt'
    with open(file,'r') as f:
        for line02 in f.readlines()[1:3]:
            line02=line02.split(' ')
        word02=len(line02)  
    return word02

def word_count03():
    """target.txtの3行目に含まれる、総単語数を調べる"""
    file='target.txt'
    with open(file,'r') as f:
        for line03 in f.readlines()[3:]:
            line03=line03.split(' ')
        word03=len(line03)  
    return word03


word1=word_count01()
word2=word_count02()
word3=word_count03()

def unique_word_count01():
    """target.txtの１行目に含まれる、ユニークな単語数を調べる"""
    file='target.txt'
    with open(file,'r') as f:
        for line01 in f.readlines()[:1]:
            line01_lower=line01.lower().split()
    return line01_lower

def unique_word_count02():
    """target.txtの２行目に含まれる、ユニークな単語数を調べる"""
    file='target.txt'
    with open(file,'r') as f:
        for line02 in f.readlines()[1:3]:
            line02_lower=line02.lower().split(' ')  
    return line02_lower

def unique_word_count03():
    """target.txtの3行目に含まれる、ユニークな単語数を調べる"""
    file='target.txt'
    with open(file,'r') as f:
        for line03 in f.readlines()[3:]:
            line03_lower=line03.lower().split(' ') 
    return line03_lower

unique_word_count=[]

for word in unique_word_count01():
    if word in unique_word_count:
        pass
    else:
        unique_word_count.append(word)

for word in unique_word_count02():
    if word in unique_word_count:
        pass
    else:
        unique_word_count.append(word)

for word in unique_word_count03():
    if word in unique_word_count:
        pass
    else:
        unique_word_count.append(word)

print('単語総数は'+str(word1+word2+word3)+'個ありました。そのうちユニークな単語数は{}個です。'.format(len(unique_word_count)))

