age = int( input("""Привет, друг.
Введи, пожалуйста, свой возраст. """))
if age <= 6:
	print('Смею предпрложить, что ты учишься в детском саду.')
elif 6 < age <= 17:
	print('Думаю ты школьник.')
elif age >= 18:
	print('Значит школу ты уже закончил.')
	if 18 <= age <= 25:
		universitystatus = input('Учишься в ВУЗе, верно? ')
		ageanswer = universitystatus.lower()
		if ageanswer == 'да':
			print('Я угадал, иди учись.')
		if ageanswer == 'нет':
			print('Небось уже работаешь, значит.')
		else: 
			universitystatus = input('Не понял тебя...так да или нет? ')
			ageanswer = universitystatus.lower()
			if ageanswer == 'да':
				print('Я угадал, иди учись.')
			elif ageanswer == 'нет':
				print('Небось уже работаешь, значит.')
	else: 
		print('Небось уже работаешь, значит.')

