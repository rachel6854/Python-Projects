songs = ["My Heart", "Her Brain", "The Light", "A Shadow", "One Dance", "Two Monkeys", "Happy Jumping"]
play_list = songs[:5:2]
play_list[play_list.index("One Dance")] = "One Dance - Together"
if len(play_list) > 1:
    play_list.pop(1)
# print(play_list)
