import msvcrt,os
def cls(title):
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")
	if title is not None:
		print(title)
def arrow(*text,title=None,desc=None,index=False,char="»",loc="l",align=True):
	if len(text)==1 and type(text[0])!="str":
		text=list(text[0])
	if index:
		for y,x in enumerate(text):
			text[y] = f"{y+1}. {x}"
	if align:
		maxi = len(text[0])
		for x in text:
			if len(x)>maxi:
				maxi=len(x)
		for y,x in enumerate(text):
			text[y] = f"{' '*(len(char)+1)}{x}"
			text[y] = f"{text[y]}{' '*(maxi-len(x))}"
	nn=0
	cls(title)
	for y,x in enumerate(text):
		if y==nn:
			if loc.lower()=="lr" or loc.lower()=="rl":
				if align:
					print(f"{char} {x[len(char)+1:]} {char}")
				else:
					print(f"{char} {x} {char}")
			elif loc.lower()=="r":
				if align:
					print(f"{x[len(char)+1:]} {char}")
				else:
					print(f"{x} {char}")
			else:
				if align:
					print(f"{char} {x[len(char)+1:]}")
				else:
					print(f"{char} {x}")
		else:
			if loc.lower()=="r" and align:
				print(x[len(char)+1:])
			else:
				print(x)
	if desc is not None:
		print(desc)
	while True:
		if msvcrt.kbhit():
			n = ord(msvcrt.getch())
			if n==224:
				n = ord(msvcrt.getch())
				if n==72:
					if nn>0:
						nn-=1
					cls(title)
					for y,x in enumerate(text):
						if y==nn:
							if loc.lower()=="lr" or loc.lower()=="rl":
								if align:
									print(f"{char} {x[len(char)+1:]} {char}")
								else:
									print(f"{char} {x} {char}")
							elif loc.lower()=="r":
								if align:
									print(f"{x[len(char)+1:]} {char}")
								else:
									print(f"{x} {char}")
							else:
								if align:
									print(f"{char} {x[len(char)+1:]}")
								else:
									print(f"{char} {x}")
						else:
							if loc.lower()=="r" and align:
								print(x[len(char)+1:])
							else:
								print(x)
					if desc is not None:
						print(desc)
				elif n==80:
					if nn<len(text)-1:
						nn+=1
					cls(title)
					for y,x in enumerate(text):
						if y==nn:
							if loc.lower()=="lr" or loc.lower()=="rl":
								if align:
									print(f"{char} {x[len(char)+1:]} {char}")
								else:
									print(f"{char} {x} {char}")
							elif loc.lower()=="r":
								if align:
									print(f"{x[len(char)+1:]} {char}")
								else:
									print(f"{x} {char}")
							else:
								if align:
									print(f"{char} {x[len(char)+1:]}")
								else:
									print(f"{char} {x}")
						else:
							if loc.lower()=="r" and align:
								print(x[len(char)+1:])
							else:
								print(x)
					if desc is not None:
						print(desc)
			elif n==13:
				break
	return nn
def main():
	txt = ["1. Menu","2. Info","3. Exit","4. Asw","5. Let"]
	txt1 = "asd","sad","asem","askduaueb"
	hasil = arrow(txt1,title="Welcome",desc="Note : use arrow",char="<->",index=True,loc="rl",align=False)
	print(hasil)
if __name__ == '__main__':
	main()