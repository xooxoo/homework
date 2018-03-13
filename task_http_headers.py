import json


def http_headers_to_json(headers, results):
    with open(headers) as fuck:
        dick = {}
        for i in fuck:
            line = i.strip().split(': ', 1)
            if 'HTTP/1.1' in i and 'H' == i[0]:
                for j in line:
                    j = j.split(' ', 2)
                    dick.setdefault('protocol', j[0])
                    dick.setdefault('status_code', j[1])
                    dick.setdefault('status_message', j[2])
            elif line == ['']:
                pass
            elif 'HTTP' in i and 'H' != i[0]:
                for j in line:
                    j = j.split(' ')
                    print(j)
                    dick.setdefault('method', j[0])
                    dick.setdefault('uri', j[1])
                    dick.setdefault('protocol', j[2])
            else:
                if line[0] in dick.keys():
                    dick[line[0]] = line[1]
                else:
                    dick.setdefault(line[0], line[1])
    with open(results, 'w') as res:
        json.dump(dick, res)
    return

