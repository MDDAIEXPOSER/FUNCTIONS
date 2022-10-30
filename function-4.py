"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def control_imt(weight,height):
    imt = weight / (height ** 2)
    return weight
    return height
    return imt

def control_out_imt():
    print('Enter your parametres: ')
    control_imt(weight = int(input()), height = int(input()))
    if imt < 18.5:
        print('Eat more')
    elif imt >= 18.5 and imt < 25:
        print('IMT - good --')
    else:
        print('Eat a little bit less')
def control_output():
    control_out_imt()

def main():
    control_output()


if __name__ == "__main__":
    main()
