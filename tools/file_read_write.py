import time
import os
import sys


now_time = time.strftime("%Y-%m-%d_%H_%M_%S")


def create_available_file(file_str): #判断文件是否存在
    file_name='./Log/available/Log_available_'+now_time+'.txt'
    f=open(file_name,'a+')
    f.write(file_str+'\n')


def create_frozen_file(file_str): #判断文件是否存在
    file_name='./Log/frozen/Log_frozen_'+now_time+'.txt'
    f=open(file_name,'a+')
    f.write(file_str+'\n')


