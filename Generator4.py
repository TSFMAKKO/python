# 定義建立生成器函式
def test():
    print('階段一1')
    print('階段一2')
    yield 5
    print('階段二1')
    print('階段二2')
    yield 10
# 呼叫並回傳生成器
gen=test()
print(gen)
# 搭配 for 迴圈中使用
for i,data in enumerate(gen):
    print(i,data) 


# 0/2/4
def generateEven():
    number=0
    yield number
    number+=2
    yield number
    number+=2
    yield number
    
evehGenerate=generateEven()

for data in evehGenerate:
    print(data)


# 產生無限多的偶數
# def generateEven2():
#     number=0
#     while True:
#         yield number
#         number+=2

    
# evehGenerate2=generateEven2()

# for data in evehGenerate2:
#     print(data)

print('~~~~~~~~~~~~')
# 產生n組
def generateEven3(n):
    number=0
    
    for i in range(n):
        yield number
        number+=2


evehGenerate3=generateEven3(3)

for data in evehGenerate3:
    print(data)

print('~~~~~~~~~~~~')
    