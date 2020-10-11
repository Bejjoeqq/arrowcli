import msvcrt,os
def cls():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
def arrow(text,char="»"):
	nn=0
	cls()
	for y,x in enumerate(text):
		if y==nn:
			print(char+" "+x)
		else:
			print(x)
	while True:
		if msvcrt.kbhit():
			n = ord(msvcrt.getch())
			if n==224:
				n = ord(msvcrt.getch())
				if n==72:
					if nn>0:
						nn-=1
					cls()
					for y,x in enumerate(text):
						if y==nn:
							print(char+" "+x)
						else:
							print(x)
				elif n==80:
					if nn<len(text)-1:
						nn+=1
					cls()
					for y,x in enumerate(text):
						if y==nn:
							print(char+" "+x)
						else:
							print(x)
			elif n==13:
				break
	return nn
def main():
	txt = ["1. Menu","2. Info","3. Exit","4. Asw","5. Let"]
	hasil = arrow(txt)
	print(hasil)
if __name__ == '__main__':
	main()