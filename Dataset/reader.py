def datafn(file):
	with open(file,"r") as fileObj:
		import csv
		d = list(csv.reader(fileObj))
		arr = []
		for i in d:
			#i.remove(i[-1])
			#i.remove("")
			arr.append(i)
		return arr
def sqlexec(file):
	import sqlite3
	db = sqlite3.connect(r"A:\Abhijith _files\Abhijith\PythonProjects\1.DJANGO PROJECTS\Pragyaan 2\Build_1\db.sqlite3")
	crsr = db.cursor()
	data = datafn(file)
	for i in range(1,len(data)):
		a = "INSERT INTO App_1_harrier VALUES (?,?,?,?,?,?,?,?,?)"
		args = (i, data[i][0],data[i][1],data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7])
		print(args)
		crsr.execute(a,args)
		db.commit()

        

sqlexec(r"harrier.csv")




