import csv

# Open csv file and report back information
with open("gradebook-54529.csv") as f:
    contents_of_gradebook = csv.reader(f)
    gradebook_information = []
    for each_line in contents_of_gradebook:
        gradebook_information += each_line

row_count = sum(1 for row in csv.reader(open("gradebook-54529.csv")))
grid_count = len(gradebook_information)
coloumn_count = int(grid_count/row_count)


#This for loop will print the names and grades of all students with a weighted avg above 90%
names = []
for i in range(row_count - 1):
    if float(gradebook_information[(i+1)*coloumn_count + 2][:-1]) > 90: 
        print(gradebook_information[(i+1)*coloumn_count], gradebook_information[(i+1)*coloumn_count + 2])


