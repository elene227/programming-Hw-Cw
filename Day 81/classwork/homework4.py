def abbrev_name(name):
    return '.'.join([word[0].upper() for word in name.split()])[:3]
