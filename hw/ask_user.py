def ask_user():
	answer_user = input("Как дела? ")
	answer_user = answer_user.lower()
	while answer_user != "хорошо":
		answer_user = input("Как дела? ")
		answer_user = answer_user.lower()
	else:
		print("Хорошо, что хорошо кончается")

ask_user()