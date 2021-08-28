# 定義建立生成器函式
def test():
    yield 5
# 呼叫並回傳生成器
gen=test()
print(gen)
# 搭配 for 迴圈中使用
for data in gen:
    print(data) #5