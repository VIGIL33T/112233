print("Распознователь Максов\n\n\n                         От Виги\n\n")
num = ["1","2","3","4","5","6","7","8","9","0"]
a = input("Привет как тебя зовут?\n").lower()
if a == "":
	print("Напиши что-то еблан")
	exit()
for x in a:
	if x in num:
		print("пошол нафик")
		exit()
else:
	if a == "макс" or a == "максим" or a == "мокс" or a == "макщ" or a == "мокщ":
		print(a.capitalize() + ", иди нахуй")
	else:
		print("пошол нахуй")