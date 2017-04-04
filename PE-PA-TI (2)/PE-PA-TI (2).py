num=31
salir=False
while (salir==False):
	if (num%7==0) or (num%7==1):
		J1="PE"
	if (num%7==2) or (num%7==3) or (num%7==6):
		J1="PA"
	if (num%7==4) or (num%7==5):
		J1="TI"
	if (num%5==0) or (num%5==1):
		J2="PE"
	if (num%5==2) or (num%5==3) or (num%5==6):
		J2="PA"
	if (num%5==4) or (num%5==5):
		J2="TI"
	if (J1==J2):
		print "EMPATE"
	if ((J1=="PE" and J2=="TI") or
	   (J1=="PA" and J2=="PE") or
	   (J1=="TI" and J2=="PA")):
		print "J1 ELIGE ", J1	
		print "J2 ELIGE ", J2
		print "J1 WIN"
	else:
		print "J1 ELIGE ", J1	
		print "J2 ELIGE ", J2
		print "J2 WIN"
	if (num==57):
		salir=True
	num=num+1
