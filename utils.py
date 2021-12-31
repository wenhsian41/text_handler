import re
import string
import collections
from string import digits

def to_1byte_and_capitalized_word(ustring):
    """把字符串全角转半角"""
    ss = []
    # 首字母大写转换
    if ustring == 'PVC':
        return ustring
    ustring = string.capwords(ustring)

    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                inside_code -= 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return ''.join(ss)

def sort_dict(dict_, reverse):
    lt = list(collections.OrderedDict(sorted(dict_.items(), reverse=reverse)).values())
    return lt

def get_num_list(test_str):
    test_str = to_1byte_and_capitalized_word(test_str)
    num_list = re.findall(r"\d+\.?\d*", test_str)
    return num_list

def get_txt_list(test_str):
    remove_digits = str.maketrans('', '', digits)
    res = test_str.translate(remove_digits)
    lt = res.replace('%', '').replace(' ', '').replace(';','').split(',')
    return lt

def merge_pct_fabric(nums, txts):
    dict_ = dict()
    for i, num in enumerate(nums):
        dict_[int(num)] = txts[i]

    dict_ = sorted(dict_.items(), reverse=True)
    return dict_