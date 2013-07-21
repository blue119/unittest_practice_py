#!/usr/bin/python

# -*- coding: utf-8 -*-
# this unitest script clone from zim of Jaap

import os
import sys
import shutil
import getopt
import logging

import tests
from tests import unittest

def main(argv=None):
    '''Run either all tests, or those specified in argv'''

    if argv is None:
        argv = sys.argv

    coverage = None
    loglevel = logging.WARNING
    opts, args = getopt.gnu_getopt(argv[1:],
        'hVD', ['help', 'debug', 'verbose', 'coverage'])
    for o, a in opts:
        if o in ('-h', '--help'):
            print '''\
usage: %s [OPTIONS] [MODULES]

Where MODULE should a module name from ./tests/
If no module is given the whole test suite is run.

Options:
  --coverage     report test coverage statistics
  -h, --help     print this text
  -V, --verbose  run with verbose output from logging
  -D, --debug    run with debug output from logging
''' % argv[0]
            return
        elif o == '--coverage':
            try:
                import coverage as coverage_module
            except ImportError:
                print >>sys.stderr, '''\
Can not run test coverage without module 'coverage'.
On Ubuntu or Debian install package 'python-coverage'.
'''
                sys.exit(1)
            #~ coverage = coverage_module.coverage(data_suffix=True, auto_data=True)
            print "running unittest with coverage."
            coverage = coverage_module.coverage(data_suffix=True)
            coverage.erase() # clean up old date set
            coverage.exclude('assert ')
            coverage.exclude('raise NotImplementedError')
            coverage.start()
        elif o in ('-V', '--verbose'):
            loglevel = logging.INFO
        elif o in ('-D', '--debug'):
            loglevel = logging.DEBUG
        else:
            assert False

    # Set logging handler
    logging.basicConfig(level=loglevel, format='%(levelname)s: %(message)s') #

    # Build the test suite
    loader = unittest.TestLoader()
    suite = tests.load_tests(loader, None, None)

    # And run it
    unittest.installHandler() # Fancy handling for ^C during test
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Create coverage output if asked to do so
    if coverage:
        coverage.stop()
        #~ coverage.combine()
        print 'Writing coverage reports...'
        pyfiles = list(tests.all_files())
        #~ coverage.report(pyfiles, show_missing=False)
        #~ coverage.html_report(pyfiles, directory='./coverage', omit=['zim/inc/*'])
        coverage_report(coverage, pyfiles, './coverage')
        print 'Done - Coverage reports can be found in ./coverage/'

def coverage_report(coverage, pyfiles, directory):
    '''Produce annotated text and html reports.
    Alternative for coverage.html_report().
    '''
    if os.path.exists(directory):
        shutil.rmtree(directory) # cleanup
    os.mkdir(directory)

    # reports per source file
    index = []
    for path in pyfiles:
        if any(n in path for n in ('inc', '_version', '__main__')):
            continue

        txtfile = path[:-3].replace('/', '.') + '.txt'
        htmlfile = path[:-3].replace('/', '.') + '.html'

        p, statements, excluded, missing, l = coverage.analysis2(path)
        nstat = len(statements)
        nexec = nstat - len(missing)
        index.append((path, htmlfile, nstat, nexec))

        write_coverage_txt(path, directory+'/'+txtfile, missing, excluded, statements)
        write_coverage_html(path, directory+'/'+htmlfile, missing, excluded, statements)

    # Index for detailed reports
    html = open(directory + '/index.html', 'w')
    html.write('''\
<html>
<head>
<title>Test Coverage Index</title>
<style>
    .good    { background-color: #9f9; text-align: right }
    .close   { background-color: #cf9; text-align: right }
    .ontrack { background-color: #ff9; text-align: right }
    .lacking { background-color: #fc9; text-align: right }
    .bad     { background-color: #f99; text-align: right }
    .int     { text-align: right }
</style>
</head>
<body>
<h1>Test Coverage Index</h1>
<table>
<tr><td><b>File</b></td><td><b>Stmts</b></td><td><b>Exec</b></td><td><b>Cover</b></td></tr>
''')

    total_stat = reduce(int.__add__, [r[2] for r in index])
    total_exec = reduce(int.__add__, [r[3] for r in index])
    total_perc = int( float(total_exec) / total_stat * 100 )
    if total_perc >= 90: type = 'good'
    elif total_perc >= 80: type = 'close'
    elif total_perc >= 60: type = 'ontrack'
    elif total_perc >= 40: type = 'lacking'
    else: type = 'bad'
    html.write('<tr><td><b>Total</b></td>'
               '<td class="int">%i</td><td class="int">%i</td>'
               '<td class="%s">%.0f%%</td></tr>\n'
                   % (total_stat, total_exec, type, total_perc) )

    for report in index:
        pyfile, htmlfile, statements, executed = report
        if statements: percentage = int( float(executed) / statements * 100 )
        else: percentage = 100
        if percentage >= 90: type = 'good'
        elif percentage >= 80: type = 'close'
        elif percentage >= 60: type = 'ontrack'
        elif percentage >= 40: type = 'lacking'
        else: type = 'bad'
        html.write('<tr><td><a href="%s">%s</a></td>'
                   '<td class="int">%i</td><td class="int">%i</td>'
                   '<td class="%s">%.0f%%</td></tr>\n'
                   % (htmlfile, pyfile, statements, executed, type, percentage) )
    html.write('''\
</table>
</body>
</html>
''')
    html.close()


def write_coverage_txt(sourcefile, txtfile, missing, excluded, statements):
    txt = open(txtfile, 'w')
    file = open(sourcefile)
    i = 0
    for line in file:
        i += 1
        if   i in missing: prefix = '!'
        elif i in excluded: prefix = '.'
        elif i in statements: prefix = ' '
        else: prefix = ' '
        txt.write(prefix + line)
    txt.close()


def write_coverage_html(sourcefile, htmlfile, missing, excluded, statements):
    html = open(htmlfile, 'w')
    html.write('''\
<html>
<head>
<title>Coverage report for %s</title>
<style>
    .code { white-space: pre; font-family: monospace }
    .executed { background-color: #9f9 }
    .excluded { background-color: #ccc }
    .missing  { background-color: #f99 }
    .comment  { }
</style>
</head>
<body>
<h1>Coverage report for %s</h1>
<table width="100%%">
<tr><td class="executed">&nbsp;</td><td>Executed statement</td></tr>
<tr><td class="missing">&nbsp;</td><td>Untested statement</td></tr>
<tr><td class="excluded">&nbsp;</td><td>Ignored statement</td></tr>
<tr><td>&nbsp</td><td>&nbsp</td></tr>
''' % (sourcefile, sourcefile))

    file = open(sourcefile)
    i = 0
    for line in file:
        i += 1
        if   i in missing: type = 'missing'
        elif i in excluded: type = 'excluded'
        elif i in statements: type = 'executed'
        else: type = 'comment'

        line = line.rstrip().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        html.write('<tr><td class="%s">%i</td><td class="code">%s</td></tr>\n'
                        % (type, i, line) )
    html.write('''\
</table>
</body>
</html>
''')
    html.close()


if __name__ == '__main__':
    main()

