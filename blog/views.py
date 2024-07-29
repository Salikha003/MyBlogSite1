from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import MessagePageForm, CommentForm
from .models import PortfolioPage, PortfolioPost, StatisticsPage, ServicesPage, TeamPage, AboutMePage, Skill, BlogDetailPage, CommentPage


class home(View):
    def get(self, request):
        if request.user.is_authenticated:
            portfolio_objects = PortfolioPage.objects.all()
            portfolio_post_objects = PortfolioPost.manager_objects.all()
            statistics_objects = StatisticsPage.objects.all().last()
            services_page_objects = ServicesPage.manager.all()
            team_page_objects = TeamPage.manager.all()
            about_me_page_object = AboutMePage.objects.all().first()
            blog_page_objects = BlogDetailPage.manager.all()   
            form = MessagePageForm() 


            context = {
                'portfolio_objects': portfolio_objects,
                'portfolio_post_objects': portfolio_post_objects,
                'statistics_objects' : statistics_objects,
                'services_page_objects' : services_page_objects,
                'team_page_objects' : team_page_objects,
                'about_me_page_object' : about_me_page_object,
                'blog_page_objects' : blog_page_objects,
                'form' : form,
            }

            return render(request=request, template_name='index.html', context=context)
    
        else:
            return redirect('/login/')


    def post(self, request):
        if request.method == 'POST':
            form =  MessagePageForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')

        return render(request=request, template_name='index.html', context={'form':form})
    


class single(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            blogpost = BlogDetailPage.objects.get(pk=pk)
            recent_post = BlogDetailPage.objects.all().order_by('-pk')[:3]
            archives = BlogDetailPage.objects.all()[:3]
            tags = BlogDetailPage.objects.all()
            comment = blogpost.comments.filter(status=True)
            form = CommentForm()

            context = {
                'form': form,
                'blogpost': blogpost,
                'recent_post':recent_post,
                'archives':archives,
                'tags': tags,
                'comment': comment,
            }
            return render(request=request, template_name='blog-single.html', context=context)
        
        else:
            return redirect('/login/')
        


    def post(self, request, pk):
        if request.user.is_authenticated:
            blogpost = BlogDetailPage.objects.get(pk=pk)
            if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.blog = blogpost
                    form.save()
                    return redirect('/home/blog/' + str(blogpost.pk))
                
            else:
                form = CommentForm()

            return render(request=request, template_name='blog-single.html', context={'form': form})

        else:
            return redirect('/login/')



class login_view(View):
    def get(self, request):
        return render(request=request, template_name='register.html')
     

    def post(self, request):
        log = request.POST.get('login1')
        passw = request.POST.get('password1')
        user = authenticate(username=log, password=passw)
        if user is None:
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('home_page')
        


class logout_view(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')
    


class register_view(View):
    def get(self, request):
        return render(request=request, template_name='register.html')
    

    def post(self, request):
        log = request.POST.get('login1')
        passw = request.POST.get('password1')
        User.objects.create_user(username=log, password=passw)
        return redirect('/login/')
        

