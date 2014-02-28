# -*- coding:utf-8 -*-
from selenium import webdriver
#from selenium.webdriver.common.keys import keys
from time import sleep
import os
if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']
dr =webdriver.Chrome()

url ='http://www.baidu.com'
dr.get(url)

print dr.get_cookies()
dr.delete_all_cookies()
dr.add_cookie({'name': 'BAIDUID', 'value': 'C71C8C1AF05D6C685719510D7E7D6EAA'})
dr.add_cookie({'name':'BDUSS','value':'kp3Yml4aVBDOXl4VmdxTFNONWdEVnVuampFdmNuWC1ZQ2NLank1NTJHT3YwalpUQVFBQUFBJCQAAAAAAAAAAAEAAABC2ucozOzo0rCiwcEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK9FD1OvRQ9TT'})

dr.get(url)

sleep(3)
dr.quit()