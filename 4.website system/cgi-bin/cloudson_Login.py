#!C:\Users\User\AppData\Local\Programs\Python\Python36-32\python.exe
'''
Created on 4th November 2018

Last changed on 25th November 2018

@author: Wong Tsun Wing, Kenton
'''

import time
import cgi
import pymysql

html5top='''
<!-- {fname} -->
<!DOCTYPE html>
<html>
 <head>
 <style>style</style>
 <img src="https://kentonbit.files.wordpress.com/2018/11/cloudsone58ebbe8838c.png" style="width:160px;height:100px;" id="P1">
 <title>{title}</title>
 <nav	style="float:right;">
  <a href="../cloudson.html">{logout}</a>
 </nav>
 </head>
 <body style = "background: url(https://kentonbit.files.wordpress.com/2018/04/qianlvjianbianguangyuntaobaozhutubeijing_2738899_small.jpg)">
  <h1>{header}</h1>
'''
html5bottom='''
  </body>
 <footer>
 <img src="http://pic.qiantucdn.com/58pic/15/82/19/49758PICyie_1024.jpg" style="width:100%;height:10px;">
 <br>2016-2018 by Cloudson INC. All Rights Reserved.
 <img src="https://www.facebook.com/images/fb_icon_325x325.png" style="width:40px;height:40px;float:right;">
</footer>
</html>
'''
print (html5top.format(fname='logon.py', title='Customer',header='Cloudson Customer System',logout='Logout'))

connection = pymysql.connect(user='root',
                             password='',
                             db='pos', 
                             cursorclass=pymysql.cursors.DictCursor)

form = cgi.FieldStorage()

if  'username' in form and 'password'in form :

    
        with connection.cursor() as cursor:
            cursor.execute('SELECT * from customer where 1;')
            found=False
            for e in cursor.fetchall():
                if form['username'].value ==e['cr_Username'] and form['password'].value==e['cr_Password'] :
                    print ("<br><h1>Welcome, %s !   <img src='http://img2.3png.com/2e0ee6ed6208b27fb4823ecea672989d878c.png' style='width:80px;height:100px'></h1>" % form[ 'username' ].value)
                    print ("<h2>You have [ %s ] shopping point</h2>" % e["shopping_point"])
                    print ("<h3>[Shopping point will auto update in 3 days]</h3><br>")
                    print ("<h3>If you want to use your shopping point, please contect our customer service team.(+852 2233 4445)</h3><br>")                

                    found=True
                
            if found==False:
                print ("<h1>Login Fail! Reason: Incorrect username or password!</h1>" )

            
else:
    print('<h1>Database connection wrong</h1>')

print('<br /><br />')    
print (time.ctime( time.time() ))
print (html5bottom)
