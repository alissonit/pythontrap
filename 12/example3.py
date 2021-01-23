
def attendance_person(persons):
    for p in persons:
        yield p

if __name__ == '__main__':

    list_persons = [1,2,3,4,5,6]
    queue = attendance_person(list_persons)

    n = 0
    while n < list_persons[-1]:
        print(f"attending the person: {next(queue)}")
        n+=1

