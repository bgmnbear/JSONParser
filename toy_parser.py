def string_element(s):
    r = '"'
    ec = False
    for i, e in enumerate(s[1:]):
        r += e
        if ec:
            ec = False
            continue
        elif e == '\\':
            ec = True
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
        return r
    for i, e in enumerate(s):
        if e in end_tokens:
            r = s[:i]
            r = cut_blank(r)
            break
    return r


def fomatted_element(s):
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
        if count > 0:
            count -= 1
            continue
        elif e in blank_tokens:
            continue
        elif e in tokens:
            l.append(e)
        elif e == ' ':
            pass
        else:
            token = common_element(s[i:])
            count = len(token) - 1
            token = fomatted_element(token)
            l.append(token)
    return l


def list_element(l, t='l'):
    # log('l', l)
    if t == 'l':
        r = []
    elif t == 'd':
        r = {}
    count = 0
    self_count = 0
    for i, e in enumerate(l):
        if count > 0:
            count -= 1
            continue
        self_count += 1
        if e == ']':
            break
        if e == '}':
            break
        elif e == '[':
            le, child_count = list_element(l[i + 1:])
            count = child_count
            self_count += child_count
            r.append(le)
            if (len(l) > (i + child_count + 1)) and (l[i + child_count + 1] == ','):
                count += 1
                self_count += 1
        elif e == '{':
            le, child_count = list_element(l[i + 1:], 'd')
            count = child_count
            self_count += child_count
            r.append(le)
            if (len(l) > (i + child_count + 1)) and (l[i + child_count + 1] == ','):
                count += 1
                self_count += 1
        elif t == 'l':
            r.append(e)
            if l[i + 1] == ',':
                count += 1
                self_count += 1
        elif t == 'd':
            k = l[i]
            # log('l[i:]', l[i:])
            if l[i + 2] == '{':
                v, child_count = list_element(l[i + 3:], 'd')
                count += child_count
                self_count += child_count
            elif l[i + 2] == '[':
                v, child_count = list_element(l[i + 3:], 'l')
                count += child_count
                self_count += child_count
            else:
                v = l[i + 2]
            # log('k, v', k, v)
            r[k] = v
            if l[i + 3] == ',':
                count += 3
                self_count += 3
            else:
                count += 2
                self_count += 2

    # log('self_count', self_count)
    # log('r', r)
    return r, self_count


def tree(s):
    l = json_list(s)
    # log('tree_l', l)
    r, c = list_element(l)
    return r[0]
