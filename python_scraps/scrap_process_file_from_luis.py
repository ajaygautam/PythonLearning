import os

import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def dump_db_stuff_to_file(folder, server, db_name):
    mkdir_p(folder)

    client_props_file = os.path.join(folder, "config.properties")
    with open(client_props_file, 'w') as fp:
        fp.write("{}={}\n".format('database.server', server))
        fp.write("{}={}\n".format('database.name', db_name))

    print(code, server, db_name, " ==> ", client_props_file)


filepath="/Users/agautam/Downloads/luis.txt"

p4_root = "/Users/agautam/work/p4/hsconfig/hsconfig"

with open(filepath) as data_file:
    while True:
        code = data_file.readline()
        if not code:
            break
        code = code.strip()
        server = data_file.readline().strip()
        db_name = data_file.readline().strip()

        client_folder_uat = os.path.join(p4_root, "Uat", code, "hsmain")
        dump_db_stuff_to_file(client_folder_uat, server.replace("HSS", "HST").replace("PRDSQL", "UATSQL"), db_name)

        client_folder_prod = os.path.join(p4_root, "Prod", code, "hsmain")
        dump_db_stuff_to_file(client_folder_prod, server, db_name)

        # client_folder_prod = os.path.join(p4_root, "Prod", code, "hsmain")
        # mkdir_p(client_folder_prod)
