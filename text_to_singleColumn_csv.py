#MrT3st3r
import re
import csv

def text_to_single_column_csv():
    with open('text.txt', 'r') as f:
        mylist=(f.readlines())
    print('Original list is >>> '+ str(mylist))

    tmplist=[]
    for _ in mylist:
        tmplist.append(re.findall(r"[\w']+", _))
    print('cleaned up list is >>> '+ str(tmplist))
    newlist=[]
    for sublist in tmplist:
        for item in sublist:
            newlist.append(item)
    print('new list is >>> '+ str(newlist))

    with open('results.csv', 'w') as f:
        writer = csv.writer(f)
        for i in newlist:
            print(i)
            writer.writerow([i])

text_to_single_column_csv()
