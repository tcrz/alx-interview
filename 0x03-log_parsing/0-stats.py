#!/usr/bin/python3
import sys


def split_str(stdin):
    str_list = stdin.split(" ")
    status_code = str_list[-2].replace('\n', '')
    file_size = str_list[-1][:-1]
    return {'status_code':int(status_code), 'file_size': int(file_size)}

count = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_data = { code:0 for code in status_codes }
file_size = 0
try:
    for line in sys.stdin:
            count += 1
            data = split_str(line)
            status_code_data[data['status_code']] += 1
            file_size += data['file_size']
            if count%10 == 0:
                print('File size:', file_size)
                for k, v in status_code_data.items():
                    if v != 0:
                        print('{}: {}'.format(k, v))
except KeyboardInterrupt:
    print('File size: ', file_size)
    for k, v in status_code_data.items():
        if v != 0:
            print('{}: {}'.format(k, v))
