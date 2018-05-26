names_list = ["Вася", "Валера", "Маша", "Петя", "Саша", "Даша"] 
while names_list.pop() != "Валера":
	if len(names_list) == 0:
		print("Валер нету")
		break
else:
	print("Валера нашелся")
		
