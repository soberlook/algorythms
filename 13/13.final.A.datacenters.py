# Посылка 35023983

def max_photo_replica(datacenters_list):
    if len(datacenters_list) <= 1:
        return 0
    res = 0
    while len(datacenters_list) > 1:
        datacenters_list = sorted(datacenters_list, reverse=True)
        datacenters_list[0] -= 1
        datacenters_list[-1] -= 1
        res += 1
        if datacenters_list[-1] == 0:
            datacenters_list.pop()
        if datacenters_list[0] == 0:
            datacenters_list.pop(0)
    return res


if __name__ == '__main__':
    n = input()
    datacenters_capacity = list(map(int, input().split()))
    print(max_photo_replica(datacenters_capacity))
