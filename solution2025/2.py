input = "328412-412772,1610-2974,163-270,7693600637-7693779967,352-586,65728-111612,734895-926350,68-130,183511-264058,8181752851-8181892713,32291-63049,6658-12472,720-1326,21836182-21869091,983931-1016370,467936-607122,31-48,6549987-6603447,8282771161-8282886238,7659673-7828029,2-18,7549306131-7549468715,3177-5305,20522-31608,763697750-763835073,5252512393-5252544612,6622957-6731483,9786096-9876355,53488585-53570896"

input = input.split(",")

def part_one():
    total = 0
    for put in input:
        values = put.split("-")
        start_int = int(values[0])
        end_int = int(values[1])
        for i in range(start_int, end_int+1):
            comp = str(i)
            if len(comp) % 2 == 0:
                if comp[0:len(comp)//2] == comp[(len(comp)//2):]:
                    total += i
    return total

def part_two():
    total = 0
    for put in input:
        values = put.split("-")
        start_int = int(values[0])
        end_int = int(values[1])
        for i in range(start_int, end_int+1):
            comp = str(i)
            add = False
            for j in range(1, len(comp)):
                if len(comp) % j == 0:
                    check = True
                    for k in range(len(comp)//j):
                        if comp[0:j] != comp[k*j:(k+1)*j]:
                            check = False
                            break
                    if check:
                        add = True
            if add:
                total += i
    return total

def main():
    print(part_one())
    print(part_two())
    comp = "asdasd"
    print(comp[0:len(comp)//2], comp[(len(comp)//2):])

main()
comp = "asdas"
for j in range(1, len(comp)):
    if len(comp) % j == 0:
        check = True
        for k in range(len(comp)//j):
            if comp[0:j] != comp[k*j:(k+1)*j]:
                check = False
                break
if check:
    print("hello")