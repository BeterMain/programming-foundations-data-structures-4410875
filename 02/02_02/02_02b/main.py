''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [1, 8, 4, 3, 4, 5, 6, 2, 1, 3, 9, 10]
average = 0

for i in range(len(student_pet_count_list)):
  average += student_pet_count_list[i]

average /= len(student_pet_count_list)
print(int(average))