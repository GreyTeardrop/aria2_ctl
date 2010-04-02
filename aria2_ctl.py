import logging
import logging.config
import os
import os.path
import xmlrpclib

from optparse import OptionParser

def path_for_url(url, base_path):
    url_split = url.split('://', 1)
    if len(url_split) == 1:
        server_path = url_split[0]
    else:
        server_path = url_split[1]
    server_path_components = server_path.split('/')[:-1]
    return os.path.join(base_path, *server_path_components)

def collect_options(url, options):
    download_options = {}
    download_options['remote-time'] = 'true'
    if options.dest_folder:
        path = path_for_url(url, options.dest_folder)
        if not os.path.exists(path):
            os.makedirs(path)
        download_options['dir'] = path
    if options.referer:
        download_options['referer'] = options.referer
    if options.cookie:
        download_options['header'] = 'Cookie:' + options.cookie
    return download_options

base_path = os.path.dirname(os.path.realpath(__file__))
logging.config.fileConfig(os.path.join(base_path, 'aria2_ctl.logging.conf'))
logger = logging.getLogger('aria2_ctl')

parser = OptionParser()
parser.add_option('-d', '--dest-folder')
parser.add_option('-i', '--input')
parser.add_option('--referer')
parser.add_option('--cookie')
(options, args) = parser.parse_args()

if options.input:
    url_source = open(options.input, 'r')
elif len(args) > 0:
    url_source = (args[0],)
else:
    parser.error('Either -i or url required')

s = xmlrpclib.ServerProxy('http://localhost:6800/rpc')

for url in url_source:
    url_options = collect_options(url, options)
    logger.debug('Fetching %s with options %s' % (url, url_options))
    s.aria2.addUri([url], url_options)
