
input_file = open("day-1-input.txt", "r")
left_list = []
right_list = []

#parse file and pull out numbers into a list
for line in input_file:
  numbers = line.split("   ")
  left_list.append(int(numbers[0]))
  right_list.append(int(numbers[1].strip('\n')))

#sort lists
left_list.sort()
right_list.sort()
result_distance = 0

#loop over and match smallest with smallest
for index, left in enumerate(left_list):
    distance = left - right_list[index]
    result_distance += -distance if distance < 0 else distance 

print(result_distance)
