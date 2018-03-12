# a = (100, '3:1')
# b = (15, 1)


def get_free_land(garden, len_wid):
    ratio = (float((garden[0]) * 100) / (float(garden[1][0])*float(garden[1][2]))) ** (1/2)
    side_a = ratio * float(garden[1][0])
    side_b = ratio * float(garden[1][2])
    if garden[0] == 0:
        raise ValueError("Не задана площадь участка")
    if len_wid[0] == 0 or len_wid[1] == 0:
        raise ValueError("Не задана площадь грядки")
    if len_wid[0] > max(side_a, side_b) or len_wid[1] > max(side_a, side_b):
        raise ValueError("Размер грядки больше размера участка")
    else:
        return garden[0] * 100 % (len_wid[0] * len_wid[1])


# print(get_free_land(a, b))
