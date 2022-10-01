#This creates a list for the trainer's last names

lastName = []

#This creates a list for the members enrolled by each trainer

membersEnrolled = []

#The next three lines initialize counter variables to 0

count0to5 = 0

count6to10 = 0

count11to15 = 0

#The following loop is repeated 15 times

for i in range(5):

   #This prompts the user for the trainer's last name

   name = input("Trainer's last name: ")

   #This prompts the user for the members' enrolled

   member = int(input("Members Enrolled: "))

   #This appends the last name to the list

   lastName.append(name)

   #This appends the members enrolled to the list

   membersEnrolled.append(member)

   #This counts the number of members enrolled in each group

   if member >=0 and member<=5:

       count0to5+=1

   elif member >=6 and member<=10:

       count6to10+=1

   elif member >=11 and member<=15:

       count11to15+=1

#The next three lines print the counter variables

print(count0to5,"enrolled 0 to 5 members")

print(count6to10,"enrolled 6 to 10 members")

print(count11to15,"enrolled 11 to 15 members")