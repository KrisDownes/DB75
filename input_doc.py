## Input a document and output a bar chart with freq of each char
import matplotlib.pyplot as plt


filename = input("Enter the input file: ")
inputfile = open(filename,"r")
data = inputfile.read()
values,counts= []
print('Number of character in file : ',len(data))
for ele in data:
    values.append(ele)
    counts.append(data.count(ele))
prod = list(zip(values,counts))

fig = plt.figure(figsize=(20,5))
plt.bar(values,counts,color = 'orange',width=0.4)
plt.xlabel("Characters")
plt.ylabel("Counts of Chars")
plt.show()
