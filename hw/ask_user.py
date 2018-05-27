def ask_user():
	try:
		answer_user = input("Как дела? ")
		answer_user = answer_user.lower()
		while answer_user != "хорошо":
			answer_user = input("Как дела? ")
			answer_user = answer_user.lower()
		else:
			return("Хорошо, что хорошо кончается")
	except KeyboardInterrupt:
		return("""
Забочусь тут о тебе, а ты меня Cntrl+C. Ну пока.""")

print(ask_user())