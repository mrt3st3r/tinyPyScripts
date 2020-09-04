import json
import time
import collections

#  takes two files and remove duplicates from file one and adds the unique list to the second file
def removeDuplicatedUrls(originalFile, newFile):
    t0 = time.time()
    with open(originalFile, "r") as f:
        l = f.readlines()
        
    print("Length of original file: " + str(len(l)))
    newList = set(l)
    #  print duplicates 
    duplicates = set([x for x in l if l.count(x) >1])
    print("\nDuplicates are : ")
    [print(x) for x in duplicates]
    

    with open(newFile, "w") as ff:
        for _ in newList:
            ff.write(_)

    with open(newFile, "r") as f:
        l2 = f.readlines()
    print("Length of the new file after removing the duplicates: " + str(len(l2)))

    t1 = time.time()
    print(f"\nTotal time taken: {round((t1-t0),3)} secs." )
    
    
if __name__ == "__main__":
    removeDuplicatedUrls("file1.txt", "file2.txt")
