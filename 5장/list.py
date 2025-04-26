subway = [10, 20, 30]
print(subway)
print(subway.index(20))
subway.append(40)
print(subway)
subway.insert(1, 15)
print(subway)
subway.pop()
print(subway)
subway.clear()
print(subway)

animal = ["푸", "피그렛", "티거", "푸"]
print(animal.count("푸"))

num = [4, 1, 3, 9, 0]
num.sort() # 오름차순
print(num)

num.sort(reverse=True) # 내림차순
print(num)

num.reverse()
print(num)

max = ['감', True, 1]
num.extend(max)
print(num)