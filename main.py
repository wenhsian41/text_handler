import re
import collections
from utils import get_num_list, get_txt_list, sort_dict, merge_pct_fabric

# A pre-defined list of clothes' layers
pre_defined_layers = ['outer', 'inner', 'base']

# sample: some pieces of textual data in product description
samples = ['outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool',
           'inner: 10% Cotton, 90% Wool; outer: 90% Cotton, 10% Leather',
           'outer: 10% Viscose, 90% Cotton; base: 100% Cotton',
           'outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool; base: 10% Cotton, 90% Wool',
           'base: 10% Cotton, 90% Wool; outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool']

# TASK 1: handling layers seperately -> solution: regular expression
# TASK 2: make percentages in descending order -> solution: data structure -> dict

def extract_layers(str):
    dict_ = dict()
    str = str.lower()
    for layer in pre_defined_layers:
        if re.search(layer, str):
             i = str.index(layer)
             dict_[i] = layer
    lt = sort_dict(dict_, False)
    return lt

def extract_fabrics(layers, sample):
    final = ''
    for i, layer in enumerate(layers):
        next_i = layers.index(layer) + 1
        if next_i == len(layers):
            next_layer = ''
        else:
            next_layer = layers[next_i]
        pattern = layer + '(.*)' + next_layer
        search = re.search(str(pattern), sample)

        if search:
            result = search.group(1).replace(":", "")
            nums = get_num_list(result)
            txts = get_txt_list(result)
            fabrics = merge_pct_fabric(nums, txts)

            f = ''
            for fabric in fabrics:
                f += str(fabric[0]) + '% ' + fabric[1] + ', '
            f = f[0:len(f)-2]
            f = layer + ': ' + f

            final += f + '; '
    final = final[0:len(final) - 2]
    return final

def do():

    for sample in samples:
        # 1. extract the list of layers with the correct order
        layers = extract_layers(sample)
        # 2. use regular expression to extract corresponding fabrics information
        fabrics = extract_fabrics(layers, sample)

        print(fabrics)

if __name__ == '__main__':
    do()