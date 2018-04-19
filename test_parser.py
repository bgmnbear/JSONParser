from toy_parser import *
from utils import log


def ensure(condition, message):
    if not condition:
        print('*** 测试失败 ***:', message)
    else:
        print('*** 测试成功 ***')


def test_common_element():
    s1 = '''
    "employees": [
        { "firstName":"John" , "lastName":"Doe" },
        { "firstName":"Anna" , "lastName":"Smith" }],
    '''
    s2 = '123 , "lastName":"Smith" '

    ensure(common_element(s1) == '"employees"', 'common_element 测试1')
    ensure(common_element(s2) == '123', 'common_element 测试2')


def test_json_list():
    s1 = '''
    {
        "employees": [
        { "firstName":-12.34 , "lastName":null },
        { "firstName":true , "lastName":["Smith", 123] }
        ]
    }
    '''
    # l1 = ['{', '"employees"', ':', '[', '{', '"firstName"', ':', '"John"', ',', '"lastName"', ':', '"Doe"', '}', ',', '{', '"firstName"', ':', '123', ',', '"lastName"', ':', '"Smith"', '}', ']', '}']

    print(s1)
    print('>>>')
    print(json_list(s1))


def test_tree():
    s1 = '''
    {
        "employees": [
        { "firstName":-12.34 , "lastName":null },
        { "firstName":true , "lastName":["Smith", 123] }
        ]
    }
    '''
    # s1 = '''{"employees": [{ "firstName":-12.34 , "lastName":null }]}'''

    print('>>>')
    print(tree(s1))


def test():
    test_common_element()
    test_json_list()
    test_tree()


if __name__ == '__main__':
    test()
