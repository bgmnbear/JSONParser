from toy_parser import *
from utils import log


def ensure(condition, message):
    if not condition:
        print('*** 测试失败 ***:', message)
    else:
        print('*** 测试成功 ***')


def test_common_element():
    s1 = '''"employees": [
{ "firstName":"John" , "lastName":"Doe" },
{ "firstName":"Anna" , "lastName":"Smith" }
'''
    s2 = '123 , "lastName":"Smith" }'

    ensure(common_element(s1) == '"employees"', 'common_element 测试1')
    ensure(common_element(s2) == '123', 'common_element 测试2')


def test_json_list():
    s1 = '''{
"employees": [
{ "firstName":-12.34 , "lastName":null },
{ "firstName":true , "lastName":["Smith", 123] }
]
}'''


def test_tree():
    s1 = '''{
"employees": [
{ "firstName":-12.34 , "lastName":null },
{ "firstName":true , "lastName":["Smith", 123] }
]
}'''
    print('字符串：', s1)
    print('>>>')
    print(json_list(s1))
    print('>>>')
    print('结果：', tree(s1))

    s2 = '''{
   "achievement" : [ "ach1", "ach2", "ach3" ],
   "age" : 23,
   "name" : "Tsybius",
   "partner" : {
      "partner_age" : 21,
      "partner_name" : "Galatea",
      "partner_sex_is_male" : false
   },
   "sex_is_male" : true
}'''
    print('\n\n')
    print('字符串：', s2)
    print('>>>')
    print(json_list(s2))
    print('>>>')
    print('结果：', tree(s2))


def test():
    test_common_element()
    test_json_list()
    test_tree()


if __name__ == '__main__':
    test()
