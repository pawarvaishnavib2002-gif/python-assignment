	
# 9. Shortlist Students for a Job role Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

# 	Show every students record in form of tuples if matches all required criteria.

# 	It is assumed that there will be only one primry skill.

# 	If no such candidate found, print No such candidate

# 	Input:

# 	Enter No of records- 2
# 	Enter Details of student-1
# 	Enter Student name- Manohar
# 	Enter Higher Education- B.Tech
# 	Enter Primary Skill- Python
# 	Enter Year of Graduation- 2022
# 	Enter Details of student-2
# 	Enter Student name- Ponian
# 	Enter Higher Education- B.Sc.
# 	Enter Primary Skill- C++
# 	Enter Year of Graduation- 2020

# 	Enter Job Role Requirement
# 	Enter Skill- Python
# 	Enter Higher Education- B.Tech
# 	Enter Year of Graduation- 2022
# 	Output

# 	('Manohar', 'B.tech', 'Python', '2022')

# Step 1: Take number of records
n = int(input("Enter No of records: "))

students = []

# Step 2: Input student details
for i in range(n):
    print(f"\nEnter Details of student-{i+1}")
    
    name = input("Enter Student name: ")
    education = input("Enter Higher Education: ")
    skill = input("Enter Primary Skill: ")
    year = input("Enter Year of Graduation: ")
    
    # Store as tuple
    students.append((name, education.lower(), skill.lower(), year))

# Step 3: Job requirements input
print("\nEnter Job Role Requirement")

req_skill = input("Enter Skill: ").lower()
req_education = input("Enter Higher Education: ").lower()
req_year = input("Enter Year of Graduation: ")

# Step 4: Filter matching students
found = False

for student in students:
    if (student[1] == req_education and 
        student[2] == req_skill and 
        student[3] == req_year):
        
        print(student)
        found = True

# Step 5: If no match
if not found:
    print("No such candidate")