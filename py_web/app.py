#!/usr/bin/python3
# -*- coding=utf-8 -*- 
import json
import web 
urls = (
    '/', 'index', # 将url交给index类处理 
    '/editor[/]?.*', 'editor',
    '/static/(.*)', 'StaticFile'
) 
data = json.load(open('../dc.json','r',encoding='utf-8') )
    
def login(name,pwd):
    if name=="admin" & pwd == "admin":
        return True
    return False

# render = web.template.render('templates',base="layout") # your templates
render = web.template.render('templates',base="layout",globals={'data': data}) # your templates
class index:
    def GET(self): 
        return render.index()

class editor:
    def GET(self): 
        return render.editor() 
class admin:
    def GET(self): 
        return render.admin()

class StaticFile:
    def GET(self, filename):  
        web.seeother('/static/'+filename); #重定向

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
