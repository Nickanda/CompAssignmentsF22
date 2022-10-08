def remove_smallest(dict):
    if dict:
        min = min(dict.values())
        for key in dict:
            if dict[key] == min:
                del dict[key]
                break
    return dict