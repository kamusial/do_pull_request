def usun_puste(content):
    list = []
    for line in content:
        if len(line) != 0:
            list.append(line)
    return list


