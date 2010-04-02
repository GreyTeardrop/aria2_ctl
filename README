==================================================
Aria2_ctl: XML-RPC controller for Aria2 downloader
==================================================

Aria2_ctl is simple XML-RPC controller for Aria2_ downloader. It is written as a quick hack to allow one to use single Aria2 instance as a download manager from Firefox (FlashGot), althogh it cound be used on its own.

.. _Aria2: http://aria2.sourceforge.net/

In order to use Aria2_ctl, Aria2 has to be running in XML-RPC mode (``--enable-xml-rpc``) option.

Usage::

    aria2_ctl.py [-i|--input <url list>] [-d|--dest-folder <distination folder>] [--referer <referer string>] [--cookie <cookies>] [<url>]

either ``<url list>`` or ``<url>`` is required.

FlashGot configuration
----------------------
Custom download manager settings for FlashGot:

:Executable path: *python interpreter path*
:Command line arguments template: *aria2_ctl.py path* ``[URL] [-i UFILE] [-d FOLDER] [--referer=REFERER] [--cookie=COOKIE]``
