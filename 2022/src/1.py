from generic import get_raw_data, get_raw_data_example


def get_data():

    data = []
    elf = []
    for line in get_raw_data():
        if line == '':
            data.append(elf)
            elf = []
        else:
            elf.append(int(line))

    # because the last elf wants to enjoy the party too
    data.append(elf)

    return data

def exo1():
    data = get_data()

    fattest_elf_index = 0
    fattest_elf_cal = 0

    for i in range(len(data)):
        cal = 0
        for food in data[i]:
            cal += food
        if cal > fattest_elf_cal:
            fattest_elf_cal = cal
            fattest_elf_index = i

    return f'the fattest is the {fattest_elf_index} (starting from 0)\nhe is carrying {fattest_elf_cal} calories'

def exo2():
    data = get_data()

    fattest_elves_index = []
    fattest_elves_cal = []


    # fill the initial values
    cal = []
    cal.append((0, sum(cal for cal in data[0])))
    cal.append((1, sum(cal for cal in data[1])))
    cal.append((2, sum(cal for cal in data[2])))

    cal = sorted(cal, key=lambda x: -x[1])
    for i, c in cal:
        fattest_elves_index.append(i)
        fattest_elves_cal.append(c)


    for i in range(len(data)):
        if i in fattest_elves_index:
            continue
        
        calories = sum(cal for cal in data[i])

        for max_cal_index in range(len(fattest_elves_cal)):
            max_calories = fattest_elves_cal[max_cal_index]
            if calories > max_calories:
                #print(f'{i} is fatter than {max_cal_index}')
                end_index = len(fattest_elves_cal) -1
                while (end_index != max_cal_index):
                    fattest_elves_index[end_index] = fattest_elves_index[end_index -1]
                    fattest_elves_cal[end_index] = fattest_elves_cal[end_index -1]
                    end_index -= 1
                
                fattest_elves_index[max_cal_index] = i
                fattest_elves_cal[max_cal_index] = calories
                break


    return sum(fattest_elves_cal)




def main():
    print(exo1())
    print(exo2())

if __name__ == '__main__':
    main()
