from django.db import connection
from django.shortcuts import render

# Create your views here.


from Blog.models import Blog


def new_blog(request):
        user_id=request.POST.get("user_id")
        return render(request, 'blog.html',{'user_id':user_id})

def create_blog(request):
        user_id= request.POST.get("user_id")
        title = request.POST.get("title")
        image = request.POST.get("image")
        summary = request.POST.get("summary")
        content = request.POST.get("content")
        category = request.POST.get("category")
        draft = request.POST.get("draft")
        if draft=='on':
                users = Blog(user=user_id,title=title, image=image, summary=summary, content=content, draft='True', category=category)
        else:
                users = Blog(user=user_id,title=title, image=image, summary=summary, content=content, draft='False', category=category)
        data={'title':title, 'image':image, 'summary':summary,'content':content, 'draft':True, 'category':category,'message': "Blog created successfully"}
        users.save()
        return render(request, 'blog_created.html', data)

def list_blog_doc(request):
        user_id = request.POST.get("user_id")
        cursor = connection.cursor()
        query1 = "select title,image,summary from blog_blog where user='" + user_id + "'and draft=false"
        cursor.execute(query1)
        data = cursor.fetchall()
        all_data=Blog.objects.filter(user=user_id).values()
        for i in all_data:
                if len(i['summary'])>60:
                        i['summary']=i['summary'][:55]+"..."
        return render(request, 'template.html', {'message':all_data})

def list_blog_pat(request):
        user_id = request.POST.get("user_id")
        cursor = connection.cursor()
        query1 = "select title,image,summary from blog_blog where user='" + user_id + "'and draft=false"
        cursor.execute(query1)
        data = cursor.fetchall()
        all_data=Blog.objects.filter(draft=False).values()
        for i in all_data:
                if len(i['summary'])>60:
                        i['summary']=i['summary'][:55]+"..."
        return render(request, 'template_pat.html', {'message':all_data})
