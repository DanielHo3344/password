password = 'a123456'
x = 3
x = int(x)
while x != 0 :
	word = input('請輸入密碼')
	if word != 'a123456':
		x = x - 1
		if x == 0:
			break
		print('密碼錯誤!還剩下',x,'次機會')
	
	if word == 'a123456':
		print ('登入成功!')
		break


