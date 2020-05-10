cases = int(input())

for t in range(cases):
	output = ""
	numBases = int(input())
	seq = input()
	for n in range(numBases):
		c = seq[n]
		if c == "A":
			output += "T"
		elif c == "T":
			output += "A"
		elif c == "G":
			output += "C"
		elif c == "C":
			output += "G"
		else:
			output = "Error RNA nucleobases found!"
			break
	print(output)