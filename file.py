import os

print "Cureent working directory is:",os.getcwd()
t=raw_input("Enter the directory in which you want to go:")
path='/home/hema/'+t
os.chdir(path)

files=os.listdir('.')
for name in files:
	print(name)

def dis(d,f):
	os.rename(d,f)
	print("File rename successfully")

def p():
			COUNT =1
			i = 1
			z=0
			y=int(input("Enter 1.MULTI FOLDER 2.SINGLE FOLDER:"))
			if(y==1):
				m=raw_input("Enter file name:")
				k=path+'/'+m
				os.chdir(k)
				ch=os.listdir('.')
				o=raw_input("Enter the new name that you want to change :")
				o1=raw_input("Extension")
				for c in ch:
					print(c)
					bcd = o + str(COUNT) + o1
					dis(c,bcd)
					COUNT +=1
			else:
				l=raw_input("Enter original name that you want to rename:")
				o=raw_input("Enter the new name that you want to change with extension:")
				dis(l,o)
				
	
p()
