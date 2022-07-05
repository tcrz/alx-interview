#!/usr/bin/python3
"""log parsing"""
import sys


def split_str(stdin):
    str_list = stdin.split()
    # print(len(str_list))
    if len(str_list) < 6:
        return None
    status_code = str_list[-2].replace('\n', '')
    file_size = str_list[-1]
    # print(file_size)
    return {'status_code': status_code, 'file_size': int(file_size)}


if __name__ == '__main__':
    count = 0
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_code_data = {code: 0 for code in status_codes}
    file_size = 0
    try:
        for line in sys.stdin:
            count += 1
            data = split_str(line)
            if data is not None:
                status_code_data[data['status_code']] += 1
                sorted_code_data = dict(sorted(status_code_data.items()))
                file_size += data['file_size']
                if count % 10 == 0:
                    print('File size: {}'.format(file_size))
                    for k, v in sorted_code_data.items():
                        if v != 0:
                            print('{}: {}'.format(k, v))
    except KeyboardInterrupt:
        print('File size: {}'.format(file_size))
        sorted_code_data = dict(sorted(status_code_data.items()))
        for k, v in sorted_code_data.items():
            if v != 0:
                print('{}: {}'.format(k, v))
    else:
        print('File size: {}'.format(file_size))
        sorted_code_data = dict(sorted(status_code_data.items()))
        for k, v in sorted_code_data.items():
            if v != 0:
                print('{}: {}'.format(k, v))
