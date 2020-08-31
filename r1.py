
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Phoenix Hsu':
			person = 'Phoenix Hsu'
			continue
		elif line == '蔡真真':
			person = '蔡真真'
			continue
		if person:
			new.append(person + ' : ' + line) # continue是為了跳過這行，不把人名該行也加入新清單
		# 並把對話內容加上人名後丟入new中
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')# f檔案, write寫入功能

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)
	
main()
