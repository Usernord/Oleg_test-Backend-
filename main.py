from collections import defaultdict


class TreeStore:

    def __init__(self, items: list):
        self.__items = sorted(items, key=lambda x: x['id'])
        self.__children = self.__getChildren()
        self.__parent = self.__getParent()

    def __getParent(self) -> dict:
        """Возвращает всех родителей"""
        parent_dict = defaultdict(list)
        for indx, val in enumerate(self.__items):
            elem = indx + 1
            while True:
                parent = val.get('parent')
                if parent == 'root':
                    break
                val = self.__items[parent - 1]
                parent_dict[elem].append(val)
        return dict(parent_dict)

    def __getChildren(self) -> dict:
        """Возвращает всех детей"""
        children_dict = defaultdict(list)
        for indx, val in enumerate(self.__items):
            parent = val.get('parent')
            children_dict[parent].append(self.__items[indx])
        return dict(children_dict)

    def getAll(self):
        """Возвращает весь массив"""
        return self.__items

    def getItem(self, elem_id: int) -> dict:
        """Метод возвращает елемент по его id или пустой словарь если элемент не найден"""
        ind = elem_id - 1
        return self.__items[ind] if ind <= len(self.__items) else {}

    def getChildren(self, elem_id: int) -> list:
        """Метод возвращает детей по id элемента если элемент не существует или нет детей пустой список"""
        return self.__children.get(elem_id, [])

    def getAllParents(self, elem_id: int) -> dict:
        """Метод возвращает родителей по id элемента если элемент не существует или нет детей пустой список"""
        return self.__parent.get(elem_id, [])


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    ts = TreeStore(items)

    all_list = ts.getAll()
    element = ts.getItem(7)
    children_for_elem4 = ts.getChildren(4)
    children_for_elem5 = ts.getChildren(5)
    parent_for_elem7 = ts.getAllParents(7)
    print(f'Весь массив: {all_list}')
    print(f'Объект с id 7: {element}')
    print(f'Дети 4-го объекта: {children_for_elem4}')
    print(f'Дети 5-го объекта: {children_for_elem5}')
    print(f'Родители 7-го объекта: {parent_for_elem7}')

