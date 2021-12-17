with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    fish_status = [int(0) for i in range(0, 9)] # days passed, number of fish at that day

    lantern_fish = lines[0].split(',')

    for fish in lantern_fish: 
        fish_status[int(fish)] += 1

    for day in range(1, 257):
        fish_to_produce = fish_status[0]
        for i in range(1,9):
            fish_status[i-1] = fish_status[i]
        fish_status[6] = fish_status[6] + fish_to_produce
        fish_status[8] = fish_to_produce


    print(sum(fish_status))