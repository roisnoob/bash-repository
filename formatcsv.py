import csv, random, time
import string
def user():
	n = 9000
	resuser = []
	for x in range(perdomain):
		length = 5
		lower = string.ascii_lowercase
		num = string.digits
		kabeh = lower + num
		temp = random.sample(kabeh,length)
		randstr = "".join(temp)
		randstr2 = "".join(temp)
		n += 1
		mail = sernem+str(randstr)+"-"+str(randstr2)+"@"
		resuser.append(mail)
	return resuser

def username():
	email = []
	for x in domain:
		for y in user():
			resemail = y+x
			email.append(resemail)
	return email

def displayname():
	first = ["Angela","Andrew","Katherine","Kyle","Joseph","Sean","Patricia","Daniel","Heather","Kaitlyn","Shannon","Bradley","Edward","Justin",
			"Yolanda","Christine","Tammy","Kelly","Julie","James","Stephen","Michael","Joel","Thomas","Anthony","Robert","Samantha","Brandon",
			"Jesse","Laura","Micheal","Franklin","Alexandra","Amy","Kenneth","Andrea","Matthew","Norma","Donna","Richard","Benjamin","Sara",
			"Makayla","Susan","Alyssa","Maria","Kevin","Robert","Raymond","Pamela","Elizabeth","David","Jennifer","Rachel","Susan","Joseph",
			"Ronald","Kevin","Tom","Jonathan","Phillip","Amanda","Edward","Courtney","Andrea","Matthew","Melissa","Patrick","Kristin","Tracey",
			"Christopher","Richard","Chad","Stephen","Michael","Ashley","Megan","Cynthia","Rodney","Casey","Raymond","Kevin","Jordan","Kendra",
			"Theresa","Emily","Jeremy","Jessica","Tracey","Felicia","Brent","Alexis","Sarah","Hailey","Joseph","James","Danielle","Theresa",
			"Jennifer","Susan"]
	last = ["Pruitt","Simpson","Griffith","Herman","Lynch","Fisher","Contreras","Ruiz","Miller","Smith","Sullivan","Yates","Weiss","White",
			"Harvey","Crane","Hendrix","Johnston","Jordan","Gomez","Bowers","Lowe","Mercado","Knight","Ruiz","Allen","Wheeler","Norris","Young",
			"Jordan","Jimenez","Alvarez","Joseph","Archer","Chavez","Todd","Martinez","Duffy","Murray","Lopez","Hayes","West","Turner","Klein",
			"Wise","Roach","Mcneil","Sandoval","Ray","Gould","Bryant","Walsh","Miller","Young","Montgomery","Chapman","Williams","Pollard",
			"Harmon","Ortiz","Morris","Massey","Conner","Byrd","Miller","Wilson","Welch","Villanueva","Burnett","Thompson","Farmer","Cox",
			"Sims","Moses","Garcia","Levy","Cruz","Koch","Smith","Webb","Ibarra","Williams","Frederick","Willis","Benson","Davis","Carter",
			"Ferguson","Taylor","Thomas","Harrison","Jordan","Nunez","Wells","Griffith","Orozco","Jones","Soto","Rangel","Petersen"]
	dm = []
	for x in range(len(username())):
		resdm = random.choice(first)+" "+random.choice(last)
		dm.append(resdm)
	return dm

def password():
	pas = []
	for x in range(len(username())):
		euy = "Badut123"
		pas.append(euy)
	return pas

def location():
	loc = []
	for x in range(len(username())):
		euy = "US"
		loc.append(euy)
	return loc

def license():
	lic = []
	license = open(flicense, "r").read().split("\n")
	for x in license:
		for i in range(len(username())):
			lic.append(x)
	return lic

print("FORMATTER STOD")
fdomain = input("file domain : ")
perdomain = int(input("user per domain : "))
sernem = input("sample username (contoh: no-reply) : ")
flicense = input("file license : ")
print("")

domain = open(fdomain, "r").read().split("\n")
header1 = ["version:v1.0"]
header2 = ["username", "displayname", "Password", "Location", "License"]
data_row = []
for a, b, c, d, e in zip(username(), displayname(), password(), location(), license()):
	data = a, b, c, d, e
	data_row.append(data)

print("[+] PROCESSING ...")
time.sleep(1)
with open("all.csv", "w", newline="") as kabeh:
	write = csv.writer(kabeh)
#	write.writerow(header1)
	write.writerow(header2)
	write.writerows(data_row)
	print("\n[-] DONE => all.csv")
	time.sleep(1)

#partial = sum(1 for line in data_row) / 5
#splitLen = int(partial)
#at = 1
#for lines in range(0, len(data_row), splitLen):
#	outputData = data_row[lines:lines+splitLen]
#	gfn = str(at) + ".csv"
#	with open(gfn, "w", newline="") as kabeh:
#		write = csv.writer(kabeh)
#		write.writerow(header2)
#		write.writerows(outputData)
#		at += 1
#		print("[-] DONE => "+gfn)
#		time.sleep(0.5)