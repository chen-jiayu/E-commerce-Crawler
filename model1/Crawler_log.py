import os
import time
import logging
def model_log(file_path,exe_status):
    record_time = time.strftime("%Y%m%d %H:%M:%S")
    log_file = open(f'../log/{record_time[0:8]}.log',mode='a',encoding='utf-8')
    log_file.write('執行程式:'+str(file_path)+'\n')
    log_file.write('執行時間:'+record_time+'\n')
    log_file.write('執行狀態:'+str(exe_status)+'\n')
    log_file.write('---------------------------------------'+'\n')

