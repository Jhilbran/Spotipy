def list_item_selector(self, list_name):
    """Prints the items in list_name returning the index of the item 
    selected. Value and Index errors handling built-in

    Args:
        list_name ([iterable]): [Object to choose from]

    Returns:
        [index]: [index of the selected item through an input]
    """
    for i, item in enumerate(list_name, start=1):
        print(f'{i}. {item}')
    try:
        return int(input('>'))-1
    except ValueError:
        print('Please input a numeric value')
        return None
    except IndexError:
        print('The value is not in the list')
        return None
    
def iterable_printer(self, iterable_name):
    """Prints all the item in an iterable object in a readable format using enumerate()

    Args:
        iterable_name (iterable): the iterable to be printed
    """
    for i, item in enumerate(iterable_name, start=1):
        print(f'{i}. {item}')