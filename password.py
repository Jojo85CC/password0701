password = 'a123456'
time = 3

while time > 0 :
	key = input('請輸入密碼:')

	if password == key :
		print ('登入成功')
		break #逃出迴圈

	else :
		time = time -1
		print('密碼錯誤! 還有',time,'次機會')





