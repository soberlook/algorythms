import datetime


def convert_contest_string_to_dt_pair_list(string):
    pair = string.split()
    for j in range(len(pair)):
        if '.' in pair[j]:
            hours_minutes = pair[j].split('.')
            hours = hours_minutes[0]
            if len(hours_minutes[1]) == 1:
                minutes = int(hours_minutes[1]) * 10
            else:
                minutes = int(hours_minutes[1])
            time_str = f'{hours}:{minutes}'
            try:
                pair[j] = datetime.datetime.strptime(time_str, '%H:%M')
            except ValueError as e:
                return 'Wrong time format'
        else:
            hours = pair[j]
            minutes = '00'
            time_str = f'{hours}:{minutes}'
            try:
                pair[j] = datetime.datetime.strptime(time_str, '%H:%M')
            except ValueError as e:
                return 'Wrong time format'
    return pair


def convert_dt_pair_list_to_contest_string(dt_pair):
    res = ''
    for el in dt_pair:
        hours = el.strftime('%H')
        hours = int(hours)
        minutes = int(el.strftime('%M'))
        if minutes == 0:
            el_str = f'{hours}'
        elif minutes % 10 == 0:
            minutes_str = str(int(minutes / 10))
            el_str = f'{hours}.{minutes_str}'
        else:
            minutes_str = str(minutes)
            el_str = f'{hours}.{minutes_str}'
        res = f'{res}{el_str} '
    return res


def schedule(time_pairs_list):
    result_sequence = []
    time_pairs_list = sorted(time_pairs_list, key=lambda x: (x[1], x[0]))
    result_sequence.append(time_pairs_list[0])
    for i in range(1, len(time_pairs_list)):
        if time_pairs_list[i][0] >= result_sequence[-1][1]:
            result_sequence.append(time_pairs_list[i])
    return result_sequence


if __name__ == '__main__':
    times = []
    no_of_classes = int(input())
    for i in range(no_of_classes):
        pair = input().split()
        for j in range(len(pair)):
            pair[j] = float(pair[j])
        times.append(pair)

    res = schedule(times)

    print(len(res))
    for pair in res:
        print('%g' % (pair[0]), '%g' % (pair[1]))


# Задача A Расписание
   
def scheduler(n):
    time_lesson = [0]*n
    for i in range(n):
        time_lesson[i] = list(map(float, input().split()))
    time_lesson = sorted(time_lesson, key=lambda k: k[1])
    final_list = []
    final_list.append(time_lesson[0])
    for j in range(1, len(time_lesson)):
        max_time = final_list[-1][1]
        start_l = time_lesson[j][0]
        if start_l >= max_time:
            final_list.append(time_lesson[j])
    print(len(final_list))
    for lesson in final_list:
        start = ('%f' % lesson[0]).rstrip('0').rstrip('.')
        finish = ('%f' % lesson[1]).rstrip('0').rstrip('.')
        print(f'{start} {finish}')

if __name__ == '__main__':
    n = int(input())
    scheduler(n)



# Задача B Биржа

def count_profit(n, price_list):
    i = 0
    result = 0
    while i < len(price_list)-1:
        diff = price_list[i+1] - price_list[i]
        if diff > 0:
            result += diff
        i += 1
    return result
            

if __name__ == '__main__':
    n = int(input())
    price_list = list(map(int, input().split()))
    print(count_profit(n, price_list))



# Задача C Подпоследовательность

def search_sequence(s, t):
    if not s:
        return True
    i = 0
    for el in t:
        if el == s[i]:
            i += 1
            if i == len(s):
                return True
    return False

if __name__ == '__main__':
    s = list(input())
    t = input()
    print(search_sequence(s, t))


# Задача D Ценный рюкзак

def select_item(size, n):
    items_list = [0]*n
    for i in range(n):
        items_list[i] = list(map(int, input().split()))
        items_list[i].append(i)
    items_list = sorted(items_list, key=lambda para: (-para[0], para[1]))
    selected_items = []
    sum_weight = 0
    for j in range(len(items_list)):
        next_item = items_list[j]
        if next_item[1] <= (size-sum_weight):
            selected_items.append(next_item)
            sum_weight += next_item[1]
    selected_items = sorted(selected_items, key=lambda k: k[2])
    for item in selected_items:
        print(item[2], end=' ')
    

if __name__ == '__main__':
    size = int(input())
    n = int(input())
    select_item(size, n)


# Задача E Печеньки

def happy_children_counter(greed_factor, number_cookies, size_cookie):
    greed_factor = sorted(greed_factor, reverse=True)
    size_cookie = sorted(size_cookie, reverse=True)
    counter = 0
    i = 0
    for greed in greed_factor:
        if greed > size_cookie[i]:
            continue
        counter += 1
        i += 1
        if i == number_cookies:
            return counter
    return counter
        

if __name__ == '__main__':
    n = int(input())
    greed_factor = list(map(int, input().split()))
    m = int(input())
    size_cookie = list(map(int, input().split()))
    print(happy_children_counter(greed_factor, m, size_cookie))




# Задача F Отсортированные строки

def sorting_list(n_str, m_len):
    list_for_sorting = [0]*n_str
    for i in range(n_str):
        list_for_sorting[i] = list(input())
    counter = 0
    for el in range(m_len):
        for j in range(n_str-1):
            if list_for_sorting[j][el] > list_for_sorting[j+1][el]:
                counter += 1
                break
    return counter
      

if __name__ == '__main__': 
    n = int(input())
    m = int(input())
    print(sorting_list(n, m))