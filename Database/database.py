import sqlite3


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except ConnectionError:
        print("error")
    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except SyntaxError as e:
        print(e)


def create_object(conn, code, object_data):
        if code == 1:
            create_insulator(conn, object_data)
        elif code == 2:
            create_lighting_arrester(conn, object_data)
        elif code == 3:
            create_splice(conn, object_data)
        elif code == 4:
            create_disconnect_switch(conn, object_data)


def create_insulator(conn, insulator):
    """
    Create a new project into the projects table
    :param conn:
    :param insulator:
    """
    sql = ''' INSERT INTO insulators(subtype,code,condition,image_path, latitude, longitude)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, insulator)


def create_lighting_arrester(conn, lightningArrester):
    """
    Create a new project into the projects table
    :param conn:
    :param lightningArrester:
    """
    sql = ''' INSERT INTO lightning_arresters(subtype,code,condition,image_path, latitude, longitude)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, lightningArrester)


def create_splice(conn, splice):
    """
    Create a new project into the projects table
    :param conn:
    :param splice:
    """
    sql = ''' INSERT INTO splices(subtype,code,condition,image_path, latitude, longitude)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, splice)


def create_disconnect_switch(conn, disconnectSwitch):
    """
    Create a new project into the projects table
    :param conn:
    :param disconnectSwitch:
    """
    sql = ''' INSERT INTO disconnect_switch(subtype,code,condition,image_path, latitude, longitude)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, disconnectSwitch)


def select_all_object(conn, code):

    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators")
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters")
    elif code == 3:
        cur.execute("SELECT * FROM splices")
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch")
    rows = cur.fetchall()
    return rows


def select_object_by_condition(conn, code, condition):
    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators WHERE condition=?", (condition,))
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters WHERE condition=?", (condition,))
    elif code == 3:
        cur.execute("SELECT * FROM splices WHERE condition=?", (condition,))
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch WHERE condition=?", (condition,))
    rows = cur.fetchall()
    return rows


def initialize_db():

    sql_create_insulators_table = """CREATE TABLE if not exists insulators (
                                        subtype text,
                                        code integer,
                                        condition text,
                                        image_path text,
                                        latitude text,
                                        longitude text
                                );"""
    sql_create_lightningArresters_table = """ CREATE TABLE if not exists lightning_arresters (
                                                subtype text,
                                                code integer,
                                                condition text,
                                                image_path text,
                                                latitude text,
                                                longitude text
                                        );"""
    sql_create_splices_table = """CREATE TABLE if not exists splices (
                                    subtype text,
                                    code integer,
                                    condition text,
                                    image_path text,
                                    latitude real,
                                    longitude text
                             );"""
    sql_create_disconnectSwitch_table = """ CREATE TABLE if not exists disconnect_switch (
                                            subtype text,
                                            code integer,
                                            condition text,
                                            image_path text,
                                            latitude text,
                                            longitude text
                                      );"""

    conn = create_connection("equipment.db")
    if conn is not None:
        create_table(conn, sql_create_insulators_table)
        create_table(conn, sql_create_lightningArresters_table)
        create_table(conn, sql_create_splices_table)
        create_table(conn, sql_create_disconnectSwitch_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    initialize_db()