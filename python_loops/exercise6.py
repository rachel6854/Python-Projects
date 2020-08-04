from random import randint

print("Useless processes should be removed")
idle_process_ids = [17, 18, 32, 6, 41, 8, 23, 88, 91]
count = 0
while len(idle_process_ids) > 5:
    rand_num = randint(0, 100)
    count += 1
    if rand_num in idle_process_ids:
        idle_process_ids.remove(rand_num)
print(idle_process_ids)
print("numner of iteration: " + str(count))
