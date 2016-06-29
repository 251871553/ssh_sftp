#!/usr/bin/env  python 
#coding=utf8
import paramiko
#import  time
import MySQLdb
import sys
import threading

'''
#search info from  mysql
conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='serverdb',port=3306)
cur=conn.cursor()
cur.execute('select  ip,username,password  from  info where groups=2')
info=cur.fetchall()
conn.close()
count= len(info)
'''

host_list=['10.136.51.207','10.254.222.212','10.254.171.96','10.254.175.75','10.254.211.137','10.254.223.212','10.254.178.60','10.254.210.137','10.254.178.59','10.136.59.78','10.254.178.58','10.254.209.149','10.254.188.69','10.254.177.168','10.254.189.69','10.254.179.58']

username='root'
password='xxxx'

count= len(host_list)
#for i in host_list:
#    print i

#sys.exit()


#cmd by paramiko
def ssh(ip,username,password,cmd):
  try:
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(ip,22,username,password)
    stdin,stdout,stderr = s.exec_command(cmd)
    result = stdout.read(),stderr.read()
    s.close()
    print ip
    for i in result:
         print i
  except:
    print '%s is wrong' % ip

def sftp(ip,username,password,localfile,remotefile):
  try:
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    t=paramiko.Transport((ip,22))
    t.connect(username=username,password=password)
    sftp= paramiko.SFTPClient.from_transport(t)
    sftp.put(localfile,remotefile)
    s.close()
    print '%s is ok' % ip
  except:
    print '%s is wrong' % ip



maininfo='''
         1,groups
         2,run cmd
         3,put/get file
         4,back/exit
         
'''

print maininfo

while  True:
         choice=raw_input('please choice:').strip()
         if choice ==' 1':
            print maininfo
            print 'gg' 
         elif choice =='2':
            print maininfo
            while  True:
               cmd=raw_input('please enter your cmd:').strip()
               if cmd == '4':
                  break
               elif  len(cmd)== 0:
                  continue
               else:
                  for i in range(count):
 #                     ip=info[i][0]
 #                     username=info[i][1]
 #                     password=info[i][2]
                      p=threading.Thread(target=ssh,args=(ip,username,password,cmd))
                      p.start()        
         elif choice =='3':
            print maininfo
            while  True:
                print '''
                         1,put file
                         2,get file
                         3.back '''
                choice_file=raw_input('pleace enter 1 or 2 :').strip()
                if choice_file =='1':
                   for i in range(count):
                       ip=info[i][0]
                       username=info[i][1]
                       password=info[i][2]
                       localfile='/etc/fstab'
                       remotefile='/opt/fstab1'
                       p=threading.Thread(target=sftp,args=(ip,username,password,localfile,remotefile))
                       p.start()
                elif choice_file == '2':
                       print 'fasfda' 
                elif choice_file == '3':
                       break
                else:
                       continue    
         elif choice =='4':
            break 
         else:
            print maininfo
            continue


print 'exit'

