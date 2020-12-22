
def count(dictionary):

    new_dict = {}
    for netID in dictionary:
        name = dictionary[netID]
        new_dict[name] = new_dict.get(name, 0) + 1
        # if name in new_dict:
        #     new_dict[name] += 1
        #
        # else:
        #     new_dict[name] = 1

    return new_dict


test = {"f001": "Jon", "f003": "Mary", "f002": "Anna", "f005": "Jon", "f007": "Anna"}
print(count(test))