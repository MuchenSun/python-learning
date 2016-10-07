#!/usr/bin/env python2
# -*- coding: utf8 -*-

'operation to file'

_author_ = 'MuchenSun'

import sqlite3

# restore inforation
def information_import():
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    f = open('student_id.txt','w') # cover the former file

    cursor.execute('drop table student') # delete old database and create a new one in next statement
    cursor.execute('create table student (id varchar(20) primary key,name varchar(20),gender varchar(20),school varchar(20),major varchar(20),class varchar(20))')
    cursor.execute("insert into student values ('201500001','MuchenSun','male','School of Information Science and Engineering','Computer Science','2015-2')")
    f.write('201500001') # when create a new piece of information, add the id to the 'student.txt'
    cursor.execute("insert into student values ('201500002','JunzhiLu','male','School of Information Science and Engineering','Information Security','2015-1')")
    f.write('\n201500002')
    cursor.execute("insert into student values ('201500003','HaotianBai','male','School of Information Science and Engineering','Computer Science','2015-1')")
    f.write('\n201500003')
    cursor.execute("insert into student values ('201500004','KailinZhong','male','School of Information Science and Engineering','Communication Engineering','2015-2')")
    f.write('\n201500004')

    cursor.rowcount
    cursor.close()
    con.commit()
    print('\ninformation restored!')
    con.close()
    f.close()

# return a list which mainly used in function 'check()' to print all students' information
def student_id_open():
    id = []
    with open('student_id.txt','r') as f:
        for line in f.readlines():
            id.append(list(map(str,line.split())))
    return id

# mainly used in function 'new' to add a new id to 'student_id.txt' / the list
def student_id_add(new_id):
    with open('student_id.txt','a') as f:
        f.write('\n'+new_id)
