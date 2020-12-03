"""
input: the test scores
initiate a interator (counter) and accumulator (sum) and set it to the zero
loop through the list test scores
add all the test scores
increment the counter by one
once the loop ends, there are no more scores to add
divide the accumulator (sum) by counter
display the output to the user
output: print the average of the class scores
"""

"""
scores
iterator, accumulator = 0
loop through scores
    accumulator = accumulator + scores
    iterator = iterator + 1
output = accumulator / total score

print output
"""
def calculate_average(scores):
      iterator = 0
  accumulator = 0
  student_count = len(scores)
  print("length is : ", len(scores))

  while iterator < len(scores):
    print(f"item at index {iterator} is:", scores[iterator])
    accumulator = accumulator = scores[iterator]

  print("sum is: ", accumulator)
  average = accumulator / student_count
  print("the average of total scores in the class is:", average)
  return average

output = calculate_average([50, 0, 100, 90, 70, 50, 95, 60]

print("output", output)
