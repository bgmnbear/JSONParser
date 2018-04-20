from utils import log


def string_element(s):
    r = '"'
    # 判断字段中是否包含引号
    include_quote = False

    for e in s[1:]:
        r += e
        if include_quote:
            include_quote = False
            continue
        elif e == '\\':
            include_quote = True
        elif e == '"':
            break
    return r


def cut_blank(s):
    r = s
    start = True
    end = True
    blank_tokens = ' \n'

    if len(r) == 0:
        start = False
        end = False

    while start:
        if r[0] in blank_tokens:
            r = r[1:]
        else:
            start = False
    while end:
        if r[-1] in blank_tokens:
            r = r[:-1]
        else:
            end = False
    return r


def common_element(s):
    r = ''
    end_tokens = ']},:'
    if s[0] == '"':
        r = string_element(s)
    else:
        for i, e in enumerate(s):
            if e in end_tokens:
                r = s[:i]
                r = cut_blank(r)
                break
    return r


def format_element(s):
    r = s
    num = '-0123456789'
    if r[0] in num:
        if '.' in r:
            return float(r)
        else:
            return int(r)
    elif r[0] == '"':
        r = r[1:-1]
        return r
    elif r == 'true':
        return True
    elif r == 'false':
        return False
    elif r == 'null':
        return None
    else:
        return r


def json_list(s):
    l = []
    count = 0
    tokens = '{}[],:'
    blank_tokens = ' \n'
    for i, e in enumerate(s):
        # skip token
        if count > 0:
            count -= 1
            continue
        elif e in blank_tokens:
            continue
        elif e in tokens:
            l.append(e)
        else:
            token = common_element(s[i:])
            count = len(token) - 1
            token = format_element(token)
            l.append(token)
    return l


def list_element(l):
    r = []
    count = 0
    self_count = 0
    for i, e in enumerate(l):
        self_count += 1
        if count > 0:
            count -= 1
            continue
        if e == ']':
            break
        else:
            token, child_count = parser(l[i:])
            r.append(token)
            count += child_count
            if l[i + child_count + 1] == ',':
                count += 1
    return r, self_count


def dict_element(l):
    r = {}
    count = 0
    self_count = 0
    offset = 2
    for i, e in enumerate(l):
        self_count += 1
        if count > 0:
            count -= 1
            continue
        if e == '}':
            break
        else:
            k = e
            v, child_count = parser(l[i + offset:])
            r[k] = v
            count += (child_count + offset)
            if l[i + count + 1] == ',':
                count += 1
    return r, self_count


def parser(l):
    c = 0
    if l[0] == '{':
        r, child_count = dict_element(l[1:])
        c = child_count
    elif l[0] == '[':
        r, child_count = list_element(l[1:])
        c = child_count
    else:
        r = l[0]
    return r, c


def tree(s):
    l = json_list(s)
    r, c = parser(l)
    return r
