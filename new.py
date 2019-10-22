path = r"C:\Users\帅就完事了\Desktop\text.txt"
with open(path) as file_project:
    lines = file_project.readlines()

pi_string = ''
for line in lines:
   pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
