import json


def http_headers_to_json(headers, results):
    with open(headers) as fuck:
        dick = {}
        for i in fuck:
            line = i.strip().split(':', 1)
            if 'HTTP' in i and 'H' == i[0]:
                for j in line:
                    j = j.split(' ')
                    dick.setdefault('protocol', j[0])
                    dick.setdefault('status_code', j[1])
                    dick.setdefault('status_message', j[2])
            elif 'HTTP' in i and 'H' != i[0]:
                for j in line:
                    j = j.split(' ')
                    dick.setdefault('method', j[0])
                    dick.setdefault('uri', j[1])
                    dick.setdefault('protocol', j[2])
            else:
                if line[0] in dick.keys():
                    dick[line[0]] = line[1]
                else:
                    dick.setdefault(line[0], line[1])
    for i in headers:
        if i.isdigit():
            results = 'results-{}.json'.format(i)
            with open(results, 'w') as res:
                json.dump(dick, res)
    return

"""
    я тут немного запутался, но этот кусок на случай, если второй аргумент будет просто results.json,
    то я его переделаю на results-i в соответствии с заголовком
"""
# headers = 'headers-2.txt'
# results = 'results'
# http_headers_to_json(headers,results)
