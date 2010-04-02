import logging
import logging.config
import os
import os.path
import sys
import xmlrpclib

base_path = os.path.dirname(os.path.realpath(__file__))
logging.config.fileConfig(os.path.join(base_path, 'aria2_ctl.logging.conf'))
logger = logging.getLogger('aria2_ctl')

def path_for_uri(uri, base_path):
    uri_split = uri.split('://', 1)
    if len(uri_split) == 1:
        server_path = uri_split[0]
    else:
        server_path = uri_split[1]
    server_path_components = server_path.split('/')[:-1]
    return os.path.join(base_path, *server_path_components)

if __name__ == '__main__':
    logger.debug('Arguments: ' + '|'.join(sys.argv))
    base_path = 't:\\download'
    if len(sys.argv) == 1:
        exit(1)
    uri = sys.argv[1]
    path = path_for_uri(uri, base_path)
    if not os.access(path, os.F_OK):
        os.makedirs(path)

    s = xmlrpclib.ServerProxy('http://localhost:6800/rpc')
    s.aria2.addUri([uri], {'dir': path, 'remote-time': 'true'})
