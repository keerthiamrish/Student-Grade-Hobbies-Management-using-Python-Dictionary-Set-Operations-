
#Dictionary Students DGrade Details
#Create Dictionary
student_details={'john':'A+','sobha':'B','Ramesh':'A','Rakesh':'c'}
print(student_details)
#add values
student_details['Aarthi'] = 'A'
print(student_details)
#update values
student_details.update({'keerthi':'B','Adhi':'A+','dev':'c'})
print(student_details)
#set of hobbies
hobbies_details=set()
hobbies_1=input("Enter hobby1:")
hobbies_details.add(hobbies_1)
hobbies_2=input("Enter hobby2:")
hobbies_details.add(hobbies_2)
hobbies_3=input("Enter hobby3:")
hobbies_details.add(hobbies_3)
print("hobbies set:",hobbies_details)
freeze_hobbies=frozenset(hobbies_details)
print(freeze_hobbies)