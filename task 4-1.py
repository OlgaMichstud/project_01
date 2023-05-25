# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qSKphVCVuSW-PKJrTRUS18DuTIqbWS4s
"""

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()
  
def get_school_name(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM Students WHERE Student_Id = ?"
    cursor.execute(sqlquery, (student_id,))
    school_id = cursor.fetchone()
    sqlquery = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(sqlquery, (school_id[2],))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print('Ошибка в получении данных', error)

def get_student_info(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT * FROM Students WHERE Student_ID = ?"
    cursor.execute(sqlquery, (student_id,))
    records = cursor.fetchall()
    for row in records:
      print('ID студента: ', row[0])
      print('Имя студента: ', row[1])
      print('ID школы: ', row[2])
      print('Название школы: ', get_school_name(student_id), '\n')
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print('Ошибка в получении данных', error)

get_student_info(201)