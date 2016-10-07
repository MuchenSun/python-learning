#!/usr/bin/env python2
# -*- coding: utf8 -*-

'major structure of the system'

_author_ = 'MuchenSun'

from system_function import *
from file_operate import *

print '\n-student information center-\n'
judge = raw_input('restore information[y/N]: ')

if judge == 'y':
    information_import() # to restore all information
else:
    pass

while 1:
    choice = raw_input('\noperation list:\n0.quit\n1.check all\n2.search\n3.update\n4.delete\n5.new\nselection: ')
    if choice == '0':
        judge = raw_input('quit[y/N]: ')
        if judge == 'y':
            break
        elif judge == 'N':
            continue
        else:
            print 'input error!'
            continue

    elif choice == '1':
        check()

    elif choice == '2':
        search()

    elif choice == '3':
        update()

    elif choice == '4':
        delete()

    elif choice == '5':
        new();

    else:
        print 'input error!'
        continue
