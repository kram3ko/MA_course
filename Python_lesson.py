def get_reversed_list(items: list) -> list:
    """
    Using slices make copy of list. So you dont have do list.copy()
    :param items: list
    :return: new list . Do not changes original
    second way: with copy and sorting
    #copied_items = reversed(items.copy())
    #return list(copied_items)

    """
    return items[::-1]
