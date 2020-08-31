# 清單的切割也可以使用在字串上(把字串中的一部分取出來)
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f: # sig清除格式
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)