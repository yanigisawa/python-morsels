import csv
import io


def condense_csv(txt, id_name=None):
    """
        Blech, this needs more refactoring, but it passes the tests.
    """
    file_obj = io.StringIO(txt)
    csv_reader = csv.reader(file_obj)
    obj = {}
    headers = []
    if id_name is None:
        headers = next(csv_reader)
    for item, header, value in csv_reader:
        if item not in obj:
            obj[item] = {}
        obj[item][header] = value
        headers.append(header)

    out_obj = io.StringIO()
    if id_name is None:
        id_name = headers[0]
    fieldnames = [id_name] + list(obj[list(obj.keys())[0]].keys())

    writer = csv.DictWriter(out_obj, fieldnames=fieldnames)
    writer.writeheader()
    for key in obj.keys():
        out = {}
        if id_name is not None:
            out = {id_name: key}
        out.update(obj[key])
        writer.writerow(out)
    return out_obj.getvalue()
