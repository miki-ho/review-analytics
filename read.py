import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
		# if count % 1000 == 0:
		# 	print(len(data))
print('檔案讀取完了, 總共有', len(data), "筆資料")

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度<100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')		

# print(good[0])

# good = [d for d in data if 'good' in d]
# print(good[0])

# good = [1 for d in data if 'good' in d]
# print(good[0])

# bad = ['bad' in d for d in data]
# print(bad[0])

# bad = []
# for d in data:
# 	bad.append('bad' in d)
# print(bad[1])

#count word
start_time = time.time()
wc = {} #word_count
for d in data:
	words =d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #add new key in wc

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('spend', end_time - start_time, 'seconds')
print(len(wc))

while True:
	word = input('what word you like to search:')
	if word == 'q':
		break
	if word in wc:
		print(word, 'display', wc[word])
	else:
		print('no display')

print('thanks use this')






