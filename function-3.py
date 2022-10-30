"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
print('que studs: ')
points_desk = {}
def control_que(que):
    for students in range(que):
        print('points for test:')
        points = int(input())
        if points > 50:
            print('True')
        else:
            print('False')
    return points

def control_output():
    control_que(int(input()))
def main():
    control_output()
if __name__ == "__main__":
  main()
