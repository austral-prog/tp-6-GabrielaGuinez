def remove_elements(list_to_remove_elements): 
    if len(list_to_remove_elements)>=6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements)>=5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements)>=1:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    else:
        list_to_remove_elements = list_to_remove_elements
        return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0,"Pink")
    return list_to_add_elements

def is_empty(list_to_check):
    if len(list_to_check)==0:
        return True
    else:
        return False

def check_lists(list_to_compare1,list_to_compare2): 
    if len(list_to_compare1)>2 and len(list_to_compare2)>2:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else: 
        return False

def list_of_lists(list_of_lists_to_modify): 
    list1=list_of_lists_to_modify[0][:2]
    list2=list_of_lists_to_modify[1][1:4]
    list3=list_of_lists_to_modify[2][-2:]
    return [list1,list2,list3]
