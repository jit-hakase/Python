def get_crud_sql(flds):
    table = str(request.url_rule)[1:]
    method = request.method
    if method != 'GET':
        data = json.loads(request.get_data())
    if method == 'PUT':
        return ('insert into ' + table + '(' + ','.join(flds) + ') values(' + '"{}",'*(len(flds)-1) + '"{}")').format(*tuple(data[fld] for fld in flds))
    elif method == 'DELETE':
        return ('delete from ' + table + ' where ' + flds[0] + ' = "{}"').format(data[flds[0]])
    elif method == 'POST':
        return ('update ' + table + ' set ' + ','.join([fld+'="{}"' for fld in flds])  + ' where ' + flds[0]).format(*tuple(data[fld] for fld in flds))+'="{}"'.format(data[flds[0]])
    elif method == 'GET':
        return ('select ' + '{},' * (len(flds)-1)+ '{}' + ' from ' + table + ' order by id').format(*flds)
