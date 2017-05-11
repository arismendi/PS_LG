#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_divisors(n):
    return [i for i in range(1, n) if n % i == 0]


def classify(num_list):
    for num in num_list:
        divs_sum = sum(get_divisors(num))
        if divs_sum > num:
            print('El número {} es abundante'.format(num))
        elif divs_sum < num:
            print('El número {} es deficiente'.format(num))
        elif divs_sum == num:
            print('El número {} es perfecto'.format(num))
        
        
classify(range(1, 15))
