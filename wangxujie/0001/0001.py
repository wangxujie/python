import random

def generateCode():
	f = open('code.txt','w')
	char_seq = 'abcdefghijklmnopqrstuvwxyz0123456789'
	for i in range(200):
		code = ''
		for j in range(9):
			code += random.choice(char_seq)
		f.write(code+'\n')
	f.close()

if __name__ == '__main__':
	generateCode()
