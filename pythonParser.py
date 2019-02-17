#Parses words from a html drop down menu

#probably bad coding style
#hopefully parses everything fine

from parse import * #requires installing parse if not installed

parse_list= list()

with open("toParse.txt", "r") as f: 
  parse_list.append(f.read())

l = ','.join(r.fixed[0] for r in findall("\">{}</li>", parse_list[0]))
list = l.split(',')

print(list)

changedList = parse_list[0]
for i in range(len(list)):

    changedList = changedList.replace(list[i],"Put_String_Here"+str(i))
print(changedList)

#uncomment code below to write to new txt files

#with open("parsedText.txt","w") as f:
#    f.write(l)
#with open("newText.txt", "w") as f:
#    f.write(changedList)
