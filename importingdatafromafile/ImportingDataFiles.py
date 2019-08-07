#WEEK 2: Importing Data from a File

import csv  #import csv library so we can read the file

total = 0   #this holds the total salary of all employees
num_records = 0 #this holds the total number of records in file

#Field Header Hint
name = "NAME"
age = "AGE"
salary = "SALARY"

print("{:5} \t\t {:5} \t\t {:8} \n".format(name, age, salary))


#right click --> "Properties" to find the file location
with open("E:/intermediate python/lab2A/lab2a.csv") as csvfile: 

    file = csv.reader(csvfile) 

    for rec in file:

        num_records = num_records + 1

        total = total + float(rec[2])
        #you could also do this:
        #rec[2] = float(rec[2])

        #print(rec)

        print("{:5} \t\t {:5} \t\t ${:8.2f}".format(rec[0], rec[1], float(rec[2])))
    


print("Finished processing.")
print("\n\n\n")
print("---------------------------------\n")
print(num_records, " records processed.")
print("ANNUAL PAYROLL: ${:.2f}".format(total))
print("\n---------------------------------\n\n\n\n\n")

