def num_let(num):
	index = [("",""),("MIL","MIL"),("MILLON","MILLONES"),("MIL","MIL")]
	inter = int(num)
	count = 0
	num_letter = ""
		
	
	if num == 0:
			num_letter = "CERO"

	while inter >0:
		a = inter % 1000
		if count == 0:
			in_letter = convert(a,1).strip()
		else :
			in_letter = convert(a,0).strip()

		if a==0:
			num_letter = in_letter+" "+num_letter
		elif a==1:
			if count in (1,3):
				num_letter = index[count][0]+" "+num_letter
			else:
				num_letter = in_letter+" "+index[count][0]+" "+num_letter
		else:
			num_letter = in_letter+" "+index[count][1]+" "+num_letter

		num_letter = num_letter.strip()
		count = count + 1
		inter = int(inter / 1000)
		
		if num == 1000000000:
			num_letter = "UN BILLÓN"
	
	return num_letter
 
 
def convert(num, sw):
	list_cent = ["",("CIEN","CIENTO"),"DOSCIENTOS","TRESCIENTOS","CUATROCIENTOS","QUINIENTOS","SEISCIENTOS","SETECIENTOS","OCHOCIENTOS","NOVECIENTOS"]
	list_dec = ["",("DIEZ","ONCE","DOCE","TRECE","CATORCE","QUINCE","DIECISEIS","DIECISIETE","DIECIOCHO","DIECINUEVE"),
				("VEINTE","VEINTI"),("TREINTA","TREINTA Y "),("CUARENTA" , "CUARENTA Y "),
				("CINCUENTA" , "CINCUENTA Y "),("SESENTA" , "SESENTA Y "),
				("SETENTA" , "SETENTA Y "),("OCHENTA" , "OCHENTA Y "),
				("NOVENTA" , "NOVENTA Y ")]
	list_uni = ["",("UN" , "UNO"),"DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE"]

	cent = int (num / 100)
	dec = int((num -(cent * 100))/10)
	uni = int(num - (cent * 100 + dec * 10))
 
	text_cent = ""
	text_dec = ""
	text_uni = ""
 
	text_cent = list_cent[cent]
	if cent == 1:
		if (dec + uni)!=0:
			text_cent = text_cent[1]
		else :
	 		text_cent = text_cent[0]

	text_dec = list_dec[dec]
	if dec == 1:
		text_dec = text_dec[uni]
	elif dec > 1:
		if uni != 0:
 			text_dec = text_dec[1]
		else:
 			text_dec = text_dec[0]

	if dec != 1:
 		text_uni = list_uni[uni]
 		if uni == 1:
 			text_uni = text_uni[sw]
 
	return "{} {} {}" .format(text_cent,text_dec,text_uni)