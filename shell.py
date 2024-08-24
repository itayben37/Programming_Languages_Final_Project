import basic

cont = True
fn = None
while cont:
	fn = input("enter a file name that end with .lambda\n")
	if fn.endswith('.lambda'):
		cont = False

while True:
		text = input('program> ')

		result, error = basic.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)
