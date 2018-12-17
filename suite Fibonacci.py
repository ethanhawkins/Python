def calc(caster):
	i = 0
	n = 0
	t=0
	liste=[1]
	while i <= caster :
		i = n + liste[t-1]
		n = i 
		liste.append(i)
		t=t+1
		print str (n) + "+" + str (liste[t-1]) + "=" + str (i)  
		


number = raw_input("Enter a number")
caster = int(number)
calc(caster)

