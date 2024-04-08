import pytest

from patterns.behavioral.catalog import Catalog, CatalogClass, CatalogInstance, CatalogStatic

def test_catalog_multiple_methods():
    test = Catalog('param_value_2')
    token = test.main_method()
    assert token == 'executed method 2!'

def test_catalog_multiple_instance_methods():
    test = CatalogInstance('param_value_1')
    token = test.main_method()
    assert token == 'Value x1'
    
def test_catalog_multiple_class_methods():
    test = CatalogClass('param_value_2')
    token = test.main_method()
    assert token == 'Value x2'

def test_catalog_multiple_static_methods():
    test = CatalogStatic('param_value_1')
    token = test.main_method()
    assert token == 'executed method 1!'
