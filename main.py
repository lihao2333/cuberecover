#! /usr/bin/python
from kociemba import solve
def getPicture():
	print "get picture"
def recognize():
	data = "DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD"
	return data
def calculate(data):
	seq_raw = solve(data)
	seq_new = []
	for seq in seq_raw.split(" "):
		if len(seq)==1:
			seq_new.append(seq)
		else:
			if seq[1]=="'":
				seq_new.append(seq[0].lower())
			else:
				seq_new.extend([seq[0],seq[0]])
	return seq_new
def rotate_single(seq,orien_arm,cmd):
	if seq<'^':
		direction = '1'
	else:
		direction = '-1'
	axes = orien_arm[0][seq.upper()]
	if axes == "XP":
		cmd.append(["R",direction,"0","0","0"])
		if direction = "1"
	elif axes == "XN":
		cmd.append(["R","0",direction,"0","0"])
	elif axes == "YP":
		cmd.append(["R","0","0",direction,"0"])
	elif axes == "YN":
		cmd.append(["R","0","0","0",direction])
def rotate_orien_arm(orien_arm, orien_seq):#0<-1;1<-2;2<-3;3<-0
	orien_arm_T = {}
	for key in orien_arm[0]:
		orien_arm_T[orien_arm[key]] = key
	temp  = orien_arm_T[orien_seq[0]]
	orien_arm_T[orien_seq[0]] = orien_arm_T[orien_seq[1]]
	orien_arm_T[orien_seq[1]] = orien_arm_T[orien_seq[2]]
	orien_arm_T[orien_seq[2]] = orien_arm_T[orien_seq[3]]
	orien_arm_T[orien_seq[3]] = temp
	for key in orien_arm_T:
		orien_arm[0][orien_arm_T[key]] = key
	
def rotate_double(axes, orien_arm, cmd):
	orien_arm_T = {}
	for key in orien_arm[0]:
		orien_arm_T[orien_arm[key]] = key
	if axes == "X":
		cmd.append(["P","0","0","-1","-1"])
		cmd.append(["R","1","-1","0","0"])
		cmd.append(["P","0","0","1","1"])
		temp = orien_arm_T["YP"]
		orien_arm_T["YP"] = orien_arm_T["ZP"]
		orien_arm_T["ZP"] = orien_arm_T["YN"]
		orien_arm_T["YN"] = orien_arm_T["ZN"]
		orien_arm_T["ZN"] = temp
	elif axes == "x":
		cmd.append(["P","-1","-1","0","0"])
		cmd.append(["R","0","0","-1","1"])
		cmd.append(["P","1","1","0","0"])
	elif axes == "Y":
		cmd.append(["P","-1","-1","0","0"])
		cmd.append(["R","0","0","1","-1"])
		cmd.append(["P","1","1","0","0"])
	elif axes == "y":
		cmd.append(["P","-1","-1","0","0"])
		cmd.append(["R","0","0","-1","1"])
		cmd.append(["P","1","1","0","0"])
	

def map(seqs):
	orien_arm = [{
		"R":"XP",
		"L":"XN",
		"B":"YP",
		"F":"YN",
		"U":"ZP",
		"D":"ZN"
	}]
	cmd = []
	for seq in seqs:
		##get orien
		orien = seq.upper()
		## top -> side
		if orien_arm[0][orien] == 'ZN' or orien_arm[0][orien] == 'ZP':
			rotate_double("X",orien_arm,cmd)
		##get direction
		rotate_single(seq, orien_arm, cmd)
	return cmd	
if __name__ == "__main__":
	data = recognize()
	seq = calculate(data)
	cmd = map(seq)
	print seq
	print cmd
