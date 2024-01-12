<<<<<<< HEAD
#!/usr/bin/python3
# -*- coding=utf-8 -*- 
import json
import web 
urls = (
    '/index[/]?.*', 'index',
    '/editor[/]?.*', 'editor'
) 
data = json.load(open('./dc.json','r') )
    
# render = web.template.render('templates',base="layout") # your templates
render = web.template.render('templates',base="layout",globals={'data': data}) # your templates
class index:
    def GET(self): 
        return render.index()

class editor:
    def GET(self): 
        return render.editor()
    
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
=======
#!/usr/bin/python3
# -*- coding=utf-8 -*- 
import json
import web 
urls = (
    '/index[/]?.*', 'index',
    '/editor[/]?.*', 'editor'
) 
data = json.load(open('./dc.json','r') )
    
# render = web.template.render('templates',base="layout") # your templates
render = web.template.render('templates',base="layout",globals={'data': data}) # your templates
class index:
    def GET(self): 
        return render.index()

class editor:
    def GET(self): 
        return render.editor()
    
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
>>>>>>> 3815180ec89aa119ee3e3a471a6ec6c3db4ff2eb
