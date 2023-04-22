def sel(cursor, tabl):
    query = f"""SELECT * FROM public.{tabl}"""
    cursor.execute(query)
    array = list(cursor.fetchall())
    return array


def upd(conn, cursor, tabl):
    import parser
    for i in range(15):
        up_query = f"""UPDATE {tabl} SET page_name = '{parser.name[i].text}', price = '{parser.price[i].text}', priceDis = '{parser.priceDis[i].text}', mark = '{parser.mark[i].text}' WHERE id = {i+1}"""
        cursor.execute(up_query)
        conn.commit()

