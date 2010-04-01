import os
import sys
import xmlrpclib

def path_for_uri(uri, base_path):
    uri_split = uri.split('://', 1)
    if len(uri_split) == 1:
        server_path = uri_split[0]
    else:
        server_path = uri_split[1]
    server_path_components = server_path.split('/')[:-1]
    return os.path.join(base_path, *server_path_components)

if __name__ == '__main__':
    base_path = 't:\\download'
    if len(sys.argv) == 1:
        exit(1)
    uri = sys.argv[1]
    path = path_for_uri(uri, base_path)
    if not os.access(path, os.F_OK):
        os.makedirs(path)

    s = xmlrpclib.ServerProxy('http://localhost:6800/rpc')
    s.aria2.addUri([uri], {'dir': path, 'remote-time': 'true'})
