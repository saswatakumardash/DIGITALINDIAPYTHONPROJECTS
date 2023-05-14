######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########



temp_records=dict()
final_records=dict()
total=[20,100,100,50]
weight=[0.15,0.4,0.2,0.25]


def read_marks(var):

	roll=var[0]
	for i in range(1,5):
		try:
			if eval(var[i])<0 or eval(var[i])>total[i-1]:
				raise exception
		except Exception:
			var[i]="None"    #changing invalid marks to None

	temp_records[roll]=[None,None,None]
	temp_records[roll][0]=[var[1],var[2],var[3],var[4]]
	compute_gpa(roll)
	assign_grade(roll)


def compute_gpa(roll):
	gpa=0.0
	marks=temp_records[roll][0]
	for i in range(0,4):
		if(marks[i]=="None"):
			marks[i]="0"
		gpa+=(float(marks[i])/total[i]*weight[i])
	gpa*=10
	gpa=round(gpa,2)
	temp_records[roll][1]=gpa





def assign_grade(roll):
	gpa=temp_records[roll][1]
	grade=''

	if gpa==10:
		grade="0"
	elif gpa>=9 and gpa<10:
		grade="A"
	elif gpa>=8 and gpa<9:
		grade="B"
	elif gpa>=6.5 and gpa<8:
		grade="C"
	elif gpa>=5 and gpa<6.5:
		grade="D"
	else:
		grade="F"
	temp_records[roll][2]=grade

def generate_records():
	final_records.update(temp_records)



# This is required to ensure that we can import your solve function without activating other parts of code
def main():
	f=open("marks.txt",'r')
	i=0
	f2=open("results.txt","w")
	for l in f:
		if (i in [0,1,2]):
			f2.write(l)
			i+=1
			continue

		var=l.split(" ")
		read_marks(var)
		i+=1

	f.close()
	generate_records()

	for record in sorted(final_records):

		line=str(record)+" "

		marks=" ".join(final_records[record][0])
		line+=marks+" "
		line+=str(final_records[record][1])+" "
		line+=str(final_records[record][2])
		line+="\n"
		f2.write(line)

	f2.close()

if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########
