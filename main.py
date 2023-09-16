import my_select
from seed import subjects


def print_subjects(subjects: list):
    counter = 0
    for i in range(len(subjects)):
        counter += 1
        print(f'{counter} - {subjects[i]}')
        
def ask_subject_id(subjects: list):
    print_subjects(subjects)
    subject_id = int(input(f'Enter subject id (1-{len(subjects)}): '))
    return subject_id

def ask_group_id():
    group_id = int(input('Enter group (1-3): '))
    return group_id
        

def main():
    
    run = True
    
    while run:
    
        query_num = input("Enter query number 1-10 or 0 to exit: ")
        
        match query_num:
            case '1':
                my_select.select_1()
            case '2':
                subject_id = ask_subject_id(subjects)
                my_select.select_2(subject_id)
            case '3':
                subject_id = ask_subject_id(subjects)
                my_select.select_3(subject_id)
            case '4':
                my_select.select_4()
            case '5':
                my_select.select_5()
            case '6':
                group_id = ask_group_id()
                my_select.select_6(group_id)
            case '7':
                group_id = ask_group_id()
                subject_id = ask_subject_id(subjects)
                my_select.select_7(group_id, subject_id)
            case '8':
                my_select.select_8()
            case '9':
                student_id = int(input('Enter student id (1-30): '))
                my_select.select_9(student_id)
            case '10':    
                student_id = int(input('Enter student id (1-30): '))
                teacher_id = int(input('Enter teacher id (1-3): '))
                my_select.select_10(student_id, teacher_id)
            case '':
                print('No values')
            case '0':
                run = False
            case _:
                print('Wrong value')
    
    
if __name__ == '__main__':
    main()