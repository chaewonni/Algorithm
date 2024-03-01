# import numpy as np

# a = np.arange(15).reshape(3,5)
# print(a)

# print(a.shpae)
# print(a.ndim)
# print(a.dtype.name)
# print(a.itemsize)
# print(a.size)
# print(type(a))

# b =np.array([6,7,8])
# print(b)
# print(type(b))

# import numpy as np

# a=np.array([2,3,4])
# print(a)
# print(a.type)

# b=np.array([1.2, 3.5, 5.1])
# print(b)
# print(b.type)

# a=np.array(1,2,3,4) #wrong
# a=np.array([1,2,3,4])

# print(np.zeros(3,4))
# print(np.ones(2,3,4), dtype=np.int16)
# print(np.empty(2,3))

# print(np.arange(0,2,0.3))
# print(np.arange(10,30,5))

# print(np.linspace(0,2,9))

# x=np.linspace(0,2*pi,100)
# print(x)

# f=np.sin(x)
# print(f)

# import numpy as np

# b=np.arrange(12).reshpae(1,12,1)

# B=np.arange(3)
# print(B)

# print(np.exp(B))
# print(np.sqrt(B))

# C=np.array([2.,-1.,4.])





# s=pd.Series(np.random.randn(5), index=["a","b","c","d","e"])

# print(s[0])
# print(s[:3])
# print(s[s>s.median()])
# print(s[[4,3,1]])
# print(np.exp(s))

# s=pd.Series(np.random.radn(5), name="something")
# print(s)
# print(s.name)

# s2 = s.name("different")
# print(s2.name)

# d={"one":pd.Series([1.0,2.0,3.0], index=["a","b","c"]), "two":pd.Series([1.0,2.0,3.0,4.0], index=["a","b","c","d"])}
# df=pd.DataFrame(d)
# print(df)

# df=pd.DataFrame(d, index=["d","b","a"])
# print(df)

# df = pd.DataFrame(d, index=["d","b","a"], columns=["two","three"])
# print(df)

# print(df.index)
# print(df.columns)

# d={"one":pd.Series([1.0,2.0,3.0], index=["a","b","c"]), "two": pd.Series([1.0,2.0,3.0,4.0],index=["a","b","c","d"])}
# df=pd.DataFrame(d)
# print(df)

# df=pd.DataFrame(d, index=["a","b","c","d"])
# print(df)

# print(df["one"])

# df["three"]=df["one"]*df["two"]
# print(df)

# df["flag"]=df["one"]>2
# print(df)

# import pandas as pd
# from sklearn.datasets import load_iris

# iris = load_iris()
# iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
# iris_df.head()




# dollar = 1140
# won = 1000000

# hwan = won//dollar
# rest = won%dollar

# print('받을 수 있는 돈은 %d 이고, 거스름돈은 %d 입니다' %(hwan, rest))

# print(1000000%1140)

# a = int(input('첫 번째 숫자 입력:'))
# b = int(input('두 번째 숫자 입력:'))
# print('%d / %d = %.2f' %(a,b,a/b))

# chat = '챗봇>'
# user = '사람>'
# print(chat, "안녕하세요")
# print(chat, "나는 인공지능 챗봇입니다.")
# print(chat, "당신의 이름은?")
# name = input(user)
# print(chat, name, '학생 반가워요')
# print(chat, "전공은 무엇인가요?")
# major = input(user)
# print(name, "학생은 아주 어려운", major, "을 공부하고 계시네요")
# print(chat, "다음 주에 또 만나요")

# num = int(input("파티에 참여할 수 있는 회원들의 숫자:"))

# chicken = num * 1
# beer = num * 2
# coke = num *2

# print("필요한 치킨:" , chicken, "필요한 맥주:" , beer, "필요한 콜라:" , coke)

# lst=[]
# color = input("색깔:")
# lst.append(color)
# color = input("색깔:")
# lst.append(color)

# print(lst)
# lst.sort()
# print(lst)
# print(len(lst))
# print(lst[-1])

# lst = ['로제','아이유']
# print('초기 동아리 회원', lst)
# lst.append('브레이브걸스')
# print(1,lst)
# lst.insert(2,'로제')
# print(2,lst)
# print(3,lst.count('로제'))
# lst.remove('브레이브걸스') #lst.pop(3)
# print(4,lst)
# lst.append('김채원')
# print(5,lst)
# lst.sort()
# print(6,lst)
# print(7, len(lst))

# name={'김밥':2000, '라면':3500, '어묵': 1000}

# menu=input('메뉴를 입력하세요:')
# print(name.get(menu),'원')

# clubA={'kim','park','hwang'}
# clubB={'park','lee','choi'}

# clubC=clubA | clubB # clubA.union(clubB)
# print(clubC)

# print(clubA.intersection(clubB))
# print(clubA.difference(clubB))

# clubA.add('yang')
# clubB.remove('lee')

# print(clubA)
# print(clubB)

phone={}
phone['제니']='010-0000-0000'
phone['로제']='010-0000-0001'
phone['리사']='010-0000-0002'

print(phone)

name=input("이름:")
print(name, phone[name])

name=input("이름 추가:")
tel=input("전화번호 추가:")

phone[name]=tel
print('추가',phone)

name=input("삭제:")
phone.pop(name)
print(phone)

