#!/usr/bin/env python2
# -*- coding: utf8 -*-

'main functions of the system'

_author_ = 'MuchenSun'

import sqlite3
from file_operate import *

label = ['id:','name:','gender:','school:','major:','class:']

#
def check():
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    student_id = student_id_open()
    for i in student_id:
        cursor.execute('select * from student where id=?',(i[0],))
        #
        print ''
        for i in cursor.fetchall():
            k = 0
            for j in i:
                print label[k]+j+'    ',
                k = k+1
                if k == 2:
                    print ''
            print ''
        #
    cursor.close()
    con.commit()
    con.close()

#
def search():
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    while 1:
        n = raw_input('\ninput id(0 to quit): ')
        if n == '0':
            break
        cursor.execute('select * from student where id=?',(n,))
        result_list = cursor.fetchall()
        if result_list: # print informaiton
            print ''
            for i in result_list:
                k = 0
                for j in i:
                    print label[k]+j+'    ',
                    k = k+1
                    if k == 2:
                        print ''
                print ''
        else:
            print 'not found!' # another case
    cursor.close()
    con.commit()
    con.close()

#
def update():
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    while 1:
        n = raw_input('\ninput id(0 to quit): ') # whose information to change
        if n == '0':
            break
        cursor.execute('select * from student where id=?',(n,))
        result_list = cursor.fetchall()
        if result_list:
            # between two '#' implements the function of print
            print ''
            for i in result_list:
                k = 0
                for j in i:
                    print label[k]+j+'    ',
                    k = k+1
                    if k == 2:
                        print ''
                print '\n'
            #
        else:
            print 'not found!'
            continue
        while 1:
            obj = raw_input('field(1:0 to quit 2:can not change id and gender): ') # which field to change
            if obj == '0':
                break
            # like 'switch' in c
            elif obj == 'name':
                content = raw_input('change to: ')
                cursor.execute('update student set name=? where id=?',(content,n))
                print 'name:changed to',content
                cursor.execute('select * from student where id=?',(n,))
                #
                print ''
                for i in cursor.fetchall():
                    k = 0
                    for j in i:
                        print label[k]+j+'    ',
                        k = k+1
                        if k == 2:
                            print ''
                    print '\n'
                #
            elif obj == 'school':
                content = raw_input('change to: ')
                cursor.execute('update student set school=? where id=?',(content,n))
                print 'school:changed to',content
                cursor.execute('select * from student where id=?',(n,))
                #
                print ''
                for i in cursor.fetchall():
                    k = 0
                    for j in i:
                        print label[k]+j+'    ',
                        k = k+1
                        if k == 2:
                            print ''
                    print '\n'
                #

            elif obj == 'major':
                content = raw_input('change to: ')
                cursor.execute('update student set major=? where id=?',(content,n))
                print 'major:changed to',content
                cursor.execute('select * from student where id=?',(n,))
                #
                print ''
                for i in cursor.fetchall():
                    k = 0
                    for j in i:
                        print label[k]+j+'    ',
                        k = k+1
                        if k == 2:
                            print ''
                    print '\n'
                #

            elif obj == 'class':
                content = raw_input('change to: ')
                cursor.execute('update student set class=? where id=?',(content,n))
                print 'class:changed to',content
                cursor.execute('select * from student where id=?',(n,))
                #
                print ''
                for i in cursor.fetchall():
                    k = 0
                    for j in i:
                        print label[k]+j+'    ',
                        k = k+1
                        if k == 2:
                            print ''
                    print '\n'
                #

            else:
                print 'input error!'
                continue

    cursor.close()
    con.commit()
    con.close()

#
def delete():
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    while 1:
        n = raw_input('\ninput id(0 to quit): ') # use id to choose
        if n == '0':
            break
        cursor.execute('select * from student where id=?',(n,))
        result_list = cursor.fetchall()
        if result_list:
            #
            print ''
            for i in result_list:
                k = 0
                for j in i:
                    print label[k]+j+'    ',
                    k = k+1
                    if k == 2:
                        print ''
                print '\n'
            #
        else:
            print 'not found!'
            continue
        yN = raw_input('delete[y/N]: ')
        if yN == 'y':
            cursor.execute('delete from student where id=?',(n,))
            print 'information deleted!'
        elif yN == 'N':
            print 'permission canceled!'
            continue
        else:
            print 'input error!'
            continue
    cursor.close()
    con.commit()
    con.close()

#
def new():
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    while 1:
        new_id = raw_input('\ninput new id(0 to quit): ')
        if new_id == '0':
            break
        elif new_id == '':
            print 'id can not be NULL!'
            continue
        cursor.execute('select * from student where id=?',(new_id,))
        if cursor.fetchall():
            print 'id already existed!'
            continue
        student_id = student_id_open()
        for t in student_id:
            judge = 0
            if int(new_id) == int(t[0]):
                judge = 1
        if judge == 1:
            print 'id was used before!'
            continue
        student_id_add(new_id) # add new id to the list which includes all students' information
        new_name = raw_input('input new name: ')
        new_gender = raw_input('input new gender: ')
        new_school = raw_input('input new school: ')
        new_major = raw_input('input new major: ')
        new_class = raw_input('input new class: ')
        new_student = [new_id,new_name,new_gender,new_school,new_major,new_class]
        cursor.execute('insert into student values (?,?,?,?,?,?)',new_student)
        print 'information created!'
        cursor.execute('select * from student where id=?',(new_id,))
        result_list = cursor.fetchall()
        print ''
        for i in result_list:
            k = 0
            for j in i:
                print label[k]+j+'    ',
                k = k+1
                if k == 2:
                    print ''
            print '\n'
    cursor.close()
    con.commit()
    con.close()
