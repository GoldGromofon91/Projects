def fibo(num):
	n1 = n2 = 1
	fibo_obj = [n1,n2]
	if num < 2 and num == 1: 
		return fibo_obj[:1]
	elif num < 2 and num == 2: 
		return fibo_obj
	else: 
		for i in range(2, num):
		    n1, n2 = n2, n1 + n2
		    fibo_obj.append(n2)
		return fibo_obj

 
def fibo_start():
	try:
		usr_num = int(input('Введите число: '))
	except (TypeError,ValueError):
		print('ОШИБКА!ВВЕДИТЕ ЧИСЛО!')
	else:
		list = fibo(usr_num)
		list.insert(0,0)
		for_dr_web = [list[i] for i in range(len(list)) if list[i] % 2 == 0]
		print(f"Числу:{usr_num} соответсвует следующий ряд Фибоначи: {list}\nВсе четные числа из текущего ряда Фибоначи:{for_dr_web}")


if __name__ == "__main__":
	fibo_start()