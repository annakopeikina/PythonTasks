# Напишите функцию same by характеристика objects которая проверяет все ли
# объекты имеют одинаковое значение некоторых характеристики и возвращают
# true если это так если значение характеристики для разных объектов
# отличаются то fals для пустого набора объектов функция должна возвращать
# true аргумент характеристик - это функция которая принимает объекты
# вычисляет его характеристику.
def same_by(characteristic, objects):
    return not objects or all(characteristic(obj) == characteristic(objects[0]) for obj in objects)


input_str = input("Введите список объектов через запятую: ")
values = input_str.split(",")
values = [int(val) for val in values]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
