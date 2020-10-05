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
