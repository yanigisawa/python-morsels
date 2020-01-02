from itertools import zip_longest


def interleave(*args):
    random_fill = object()
    return (
        item
        for zipped_item in zip_longest(*args, fillvalue=random_fill)
        for item in zipped_item
        if item is not random_fill
    )

    # for t in zip_longest(*args, fillvalue=random_fill):
    #     for item in t:
    #         if item is not random_fill:
    #             yield item

