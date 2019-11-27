import os


# def window(items, n):
#     if n == 0:
#         return []
#     result = []
#     l_items = list(items)
#     for idx, value in enumerate(list(l_items)):
#         if n == 1:
#             result.append((l_items[idx],))
#             continue
#         tmp = []
#         for i in range(n):
#             if idx + i >= len(list(l_items)):
#                 break
#             tmp.append(l_items[idx + i])
#         if len(tmp) < n:
#             break
#         result.append(tuple(tmp))
#     return result


def window(items, n):
    current = ()
    for item in items:
        if len(current) < n:
            current = (*current, item)
        else:
            current = (*current[1:], item)
        if len(current) == n:
            yield current


# def window(items, n):
#     if n == 0:
#         return []
#     result = []
#     for idx, value in enumerate(items):
#         if n == 1:
#             yield (items[idx],)
#             continue
#         yield from (items[idx : idx + n])
# tmp = []
# for i in range(n):
#     if idx + i >= len(list(items)):
#         break
#     tmp.append(items[idx + i])
# if len(tmp) != n:
#     break
# yield tuple(tmp)

# raise StopIteration
