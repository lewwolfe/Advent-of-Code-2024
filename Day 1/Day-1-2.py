
input_file = open("day-1-input.txt", "r")
left_list = []
right_list = []

#parse file and pull out numbers into a list
for line in input_file:
  numbers = line.split("   ")
  left_list.append(int(numbers[0]))
  right_list.append(int(numbers[1].strip('\n')))

result_similarity = 0
#loop over left items and find how many times they are in right
for left in left_list:
  similarity_score = 0
  
  #find all instances of the left number in the right
  for right in right_list:
    if right == left:
      similarity_score += right
  
  #add those instances to similarity score
  result_similarity += similarity_score


print(result_similarity)
