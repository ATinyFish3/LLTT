import subprocess
import io


fileName = '/bin/ls'


p = subprocess.Popen(['readelf', fileName, '--sections'], stdout=subprocess.PIPE)


nums = []

for line in io.TextIOWrapper(p.stdout, encoding='utf-8'):
	num = line[3:5].strip()
	if num.isdigit():
		nums.append(num)
		
print(nums)

sections = []

for num in nums:
	p = subprocess.Popen(['readelf', fileName, '-x', num,], stdout=subprocess.PIPE)
	output = p.stdout.read().splitlines()[1:2]
	if str(output)[24:-4] != '':
		sections.append(str(output)[24:-4])

print(sections)


for section in sections:
	p = subprocess.Popen(['objdump', '-d', '-j', section,  fileName], stdout=subprocess.PIPE)
	for line in io.TextIOWrapper(p.stdout, encoding='utf-8'):
		print(line.strip())
