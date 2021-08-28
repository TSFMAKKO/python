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