from .forms import RegisterForm
from mgl.models import GameList
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


# Create your views here.


def GameListView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('mygamelist/')
    else:
        form = RegisterForm()

    gamelistview = GameList.objects.all()

    paginator = Paginator(gamelistview, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'mgl/pages/index.html', {'form':form, 'gameitems':gamelistview, 'page_obj': page_obj})

'''
class GameListView(ListView):
    
    allow_empty = True
    
    template_name = 'mgl/pages/index.html'
    model = GameList
    paginate_by = PER_PAGE
    context_object_name = 'gamelist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RegisterFormView(FormView):
    template_name = 'mgl/pages/index.html'
    form_class = RegisterForm
    success_url = ''

    def form_valid(self, form):
        return super().form_valid(form)


def RegisterFormView(FormView):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        
        if form.is_valid():
            gimage = form.cleaned_data['game_image']
            gname = form.cleaned_data['game_name']
            ghourstaken = form.cleaned_data['hours_taken']
            gdatefinished = form.cleaned_data['date_finished']
            gabout = form.cleaned_data['about']
            gother = form.cleaned_data['other']
        
       
            p = GameList(game_image=gimage,
                         game_name=gname,
                         hours_taken=ghourstaken,
                         date_finished=gdatefinished,
                         about=gabout,
                         other=gother 
            )
            
            p.save()
            
    else:
        form = RegisterForm()
    return render (request, 'mgl/pages/register.html', {'form':form, "site_title": " - Register"})
'''