#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Data(object):

    products = {
            'milk': { 'price': 1.50, 'quantity': 10 },
            'eggs': { 'price': 0.20, 'quantity': 100 },
            'cheese': { 'price': 2.00, 'quantity': 10 }
    }


class BusinessLogic(object):

    def __init__(self):
        self.data = Data()

    def product_list(self):
        return self.data.products.keys()

    def product_information(self, product):
        return self.data.products.get(product, None)


class Ui(object):

    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        print('PRODUCT LIST:')
        for product in self.business_logic.product_list():
            print(product)
        print('')

    def get_product_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info is not None:
            print('PRODUCT INFORMATION:')
            print('Name: %s, Price: %.2f, Quantity: %d\n' % \
                  (product.title(), product_info.get('price', 0), \
                   product_info.get('quantity', 0)))
        else:
            print('That product "%s" does not exist in the records' % product)


if __name__ == '__main__':

    ui = Ui()
    ui.get_product_list()
    ui.get_product_information('cheese')
    ui.get_product_information('eggs')
    ui.get_product_information('milk')
    ui.get_product_information('arepas')
