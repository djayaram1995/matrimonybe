def queryFrame(index, column, value, operator):
    clause = ''
    if index == 0:
        clause=' WHERE '+column+' '
    else:
        clause=' AND '+column+' '
    if operator == '=':
        clause+=operator+' %s'
    elif operator == 'LIKE':
        clause+=operator+' %s'
    elif operator == 'IN':
        clause+=operator+' ('
        for val in value:
            clause+='%s'
        clause+=')'
    elif operator == 'BETWEEN':
        clause+=operator+' %s AND %s'
    return clause