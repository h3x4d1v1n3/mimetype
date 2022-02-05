import mimetype

def of(file_name):
    ext = file_name.split('.')[-1]

    variables = dir(mimetype)
    available_exts = [exts for exts in variables if '__' not in exts]

    if (ext in available_exts):
        return eval(f'mimetype.{ext}')
    elif (f'_{ext}' in available_exts):
        return eval(f'mimetype.{ext}')

    return [None]