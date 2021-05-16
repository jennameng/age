driving = input('你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能回答 有/沒有')
	raise SystemExit	
age = input('請問你幾歲?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你棒棒')
	else:
		print('你這樣不可以喔')
elif driving == '沒有':
	if age >= 18:
		print('要去考駕照嗎')
	else:
		print('再等幾年就可以考駕照囉~')


