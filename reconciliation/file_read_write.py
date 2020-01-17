import time
import os
import sys

def fun_date():   #获取系统时间
    m=(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    #print (m)
    return m
#print(fun_date())

def fun_time():   #获取系统时间
    m=(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    #print (m)
    return m
#print(fun_date())

def create_available_file(file_str): #判断文件是否存在
    file_name='./../reconciliation/Log/Log_available_'+fun_date()+'.txt'
    #if os.path.exists(file_name):

        #print('已存在')
    #else:
        #print('不存在')
    #sys.stdout = open(file_name, "w")
    f=open(file_name,'a+')
    f.write(file_str+'\n')

    #print(file_name)
#create_file('家里的花瓶')
#fun_time()

def create_frozen_file(file_str): #判断文件是否存在
    file_name='./../reconciliation/Log/Log_frozen_'+fun_date()+'.txt'
    #if os.path.exists(file_name):

    #print('已存在')
    #else:
    #print('不存在')
    #sys.stdout = open(file_name, "w")
    f=open(file_name,'a+')
    f.write(file_str+'\n')


