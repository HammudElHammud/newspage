from django.shortcuts import render,get_object_or_404,redirect
from .models import Main
from category.models import Category
from subcategory.models import subCategory
from news.models import News
from contantform.models import Cont
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib.auth import authenticate,login, logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse


def home(requeste):
    news = News.objects.all().order_by('-pk')
    lnews = News.objects.all().order_by('-pk')[:3]
    pageName = Main.objects.get(pk=2)
    popNews = News.objects.all().order_by('-newShow')[:3]

    cat = Category.objects.all()
    scat = subCategory.objects.all()


    return render(requeste,'front/home.html',{'pageName':pageName , 'news':news, 'cat':cat, 'scat':scat, 'lnews':lnews,'popNews':popNews})

# Create your views here.
def about(requeste):
    name = Main.objects.get(pk= 2)
    news = News.objects.all()
    lnews = News.objects.all()
    pageName = Main.objects.get(pk=2)
    popNews = News.objects.all().order_by('-newShow')[:3]

    cat = Category.objects.all()
    scat = subCategory.objects.all()

    return render(requeste,"front/aboutus.html",{'name':name,'pageName':pageName , 'news':news, 'cat':cat, 'scat':scat, 'lnews':lnews,'popNews':popNews})

def news(requste):

    return render(requste,'home.html')

def news_datile(requeste, pk):
    site  = Main.objects.all()
    news = News.objects.filter(pk= pk)
    cat = Category.objects.all()
    newShow = News.objects.filter(pk =pk)
    popNews = News.objects.all().order_by('-newShow')[:3]
    tag = News.objects.get(pk = pk).tag

    try:
         myShow = News.objects.get(pk = pk)
         myShow.newShow = myShow.newShow + 1
         myShow.save()
    except:
        print("you can not add show")

    return render(requeste,'front/news_datile.html',{ 'news':news ,'cat':cat,'site':site,'popNews':popNews,'tag':tag})
def panel(requste):
    if  not requste.user.is_authenticated:
        return render(requste,'back/login.html')


    return render(requste,'back/panel.html')


def nowNewsDtaile(requeste):
    news  = News.objects.all()
    site = Main.objects.get(pk = 2)

    return render(requeste,'back/nowNewsDatile.html',{'news':news, 'site':site})

def newAdd(requeste):

    cat = Category.objects.all()

    if requeste.method == 'POST':
        newTitle = requeste.POST.get('newtitle')
        # newDate = requeste.POST.get('newdate')
        newshort = requeste.POST.get('newshort')
        newbody = requeste.POST.get('newbody')
        newcategory = requeste.POST.get('category')
        newwriter = requeste.POST.get('writer')
        newTag = requeste.POST.get('tag')
        if newTitle == '' or newTitle == '' or newshort == '' or newbody == ''  or newcategory == '' or newwriter == '' :
            error = 'All Fialled Requirded'
            return render(requeste,'back/error.html',{'error':error})
        try:
          myfile = requeste.FILES['myImg']
          fs = FileSystemStorage()
          fileName = fs.save(myfile.name,myfile)
          url = fs.url(fileName)
          # categoryName = subCategory.objects.get(pk = newcategory).name
          # OcategoryName = subCategory.objects.get(pk = newcategory).categoryId

          b = News(name = newTitle,short_txt = newshort, date = datetime.datetime.now(), newBody = newbody,picName= fileName,picUrl = url,writer =newwriter,newCategory =newcategory ,newShow = 0,catId= 1,OcatId = 1,tag = newTag)
          b.save()

        # return render(requeste,'back/nowNewsDatile.html')
        except:
           error = 'Please enter your image'
           return render(requeste, 'back/error.html',{'error':error})

    return render(requeste,'back/newAdd.html',{'cat':cat})

def newsDelete(requeste,pk):
    news = News.objects.all()
    b = News.objects.filter(pk = pk)
    b.delete()

    return render(requeste,'back/nowNewsDatile.html',{'news':news})

def news_edit(request,pk):
    news = News.objects.get(pk = pk)
    cat = Category.objects.all()
    # if request.method == 'POST':
    #     newTitle = request.POST.get('newtitle')
    #     # newDate = requeste.POST.get('newdate')
    #     newshort = request.POST.get('newshort')
    #     newbody = request.POST.get('newbody')
    #     newcategory = request.POST.get('category')
    #     newwriter = request.POST.get('writer')
    #     if newTitle == '' or newTitle == '' or newshort == '' or newbody == ''  or newcategory == '' or newwriter == '' :
    #         error = 'All Fialled Requirded'
    #         return render(request,'back/error.html',{'error':error})
    #     try:
    #       myfile = request.FILES['myImg']
    #       fs = FileSystemStorage()
    #       fileName = fs.save(myfile.name,myfile)
    #       url = fs.url(fileName)
    #       b = News.objects.get(pk = pk)
    #       fss = FileSystemStorage()
    #       fss.delete(b.picname)
    #
    #       b.name = newTitle
    #       b.short_txt = newshort
    #       b.date = datetime.datetime.now()
    #       b.newBody = newbody
    #       b.picname = fileName
    #       b.picurl = url
    #       b.writer = newwriter
    #       b.newCategory = newcategory
    #
    #       b.save()
    #     # return render(requeste,'back/nowNewsDatile.html')
    #     except:
    #        error = 'Please enter your image'
    #        return render(request, 'back/error.html',{'error':error})
    #     b = News.objects.get(pk=pk)
    #     b.name = newTitle
    #     b.short_txt = newshort
    #     b.date = datetime.datetime.now()
    #     b.newBody = newbody
    #     b.writer = newwriter
    #     b.newCategory = newcategory
    #     b.save()


    return render(request,'back/newsEdit.html',{'news':news,'cat':cat})

def CategoryList(request):
    cat = Category.objects.all()


    return render(request,'back/CategoryListe.html',{'cat':cat})


def addCategory(requeste):

    cat = Category.objects.all()
    if requeste.method == 'POST':
      category = requeste.POST.get('category')

      if category == '':

         error = 'All Fialled Requirded'
         return render(requeste,'back/error.html',{'error':error})


      if len(Category.objects.filter(name= category)) != 0:
         error = 'You can not add this name of category because its find in the list  '
         return render(requeste, 'back/error.html', {'error': error})


      b = Category(name= category)
      b.save()
      return render(requeste,'back/CategoryListe.html',{'cat':cat} )
    return render(requeste,'back/addCategory.html')


def categoryDelete(requeste,pk):

     cat = Category.objects.all()
     b  = Category.objects.filter(pk = pk)
     b.delete()
     return render(requeste, 'back/CategoryListe.html', {'cat': cat})

def subCategoryList(requeste):
    cat = subCategory.objects.all()


    return render(requeste,'back/subCategoryList.html',{'cat':cat})


def addSubCategory(requeste):
    category = Category.objects.all()


    cat = subCategory.objects.all()
    if requeste.method == 'POST':

        name = requeste.POST.get('name')
        categoryId = requeste.POST.get("category")

        if name == '' :
         error = 'All Fialled Requirded'
         return render(requeste,'back/error.html',{'error':error})

         if len(subCategory.objects.filter(name= name)) != 0 :

             error = 'You can not add this name of category because its find in the list'
             return render(requeste, 'back/error.html', {'error': error})



        categoryName = Category.objects.get(pk = categoryId).name
        # categoryFatherId = Category.objects.get(pk = categoryId).pk
        # count = len(subCategory.objects.get(categoryId = categoryFatherId))
        # category.count= count
        # print(count)
        # category.save()

        b = subCategory(name= name, categoryName = categoryName, categoryId = categoryId)
        b.save()
        return render(requeste,'back/subCategoryList.html',{'cat':cat,'category':category})
    return render(requeste,'back/addSubCategory.html',{'category':category})


def subcategoryDelete(requeste , pk):


    cat = subCategory.objects.all()
    b  = subCategory.objects.filter(pk = pk)
    b.delete()
    return render(requeste, 'back/subCategoryList.html', {'cat': cat})


def login(requeste):
    if requeste.method == 'POST':
        uuser = requeste.POST.get('username')
        ppassword = requeste.POST.get('password')
        if uuser != '' and ppassword != '':
            user = authenticate(username = uuser,password = ppassword)

            if user is not None:

                auth.login(requeste,user)
                return render(requeste,'back/panel.html')




    return render(requeste,'back/login.html')
def logout(requste):



    auth.logout(requste)


    return render(requste,'back/login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('email')
        userpassword = request.POST.get('password')
        userconfpass = request.POST.get('confpassword')
        if username != '' and useremail != '' and userpassword != '' and userconfpass != '':
            if userpassword == userconfpass :
                if len(User.objects.filter(username=username)) == 0 and len(User.objects.filter(email= useremail)) == 0:
                    user = User.objects.create_user(username,useremail,userpassword)


            else:
                error = 'The password most be same the conferim password'
                return render(request,'back/error.html',{'error':error})

    return render(request,'back/login.html')

def settingPage(requeste):

    site = Main.objects.get(pk = 2)

    if requeste.method == 'POST':

        pageTel = requeste.POST.get('pageTel')
        pageName = requeste.POST.get('pageName')
        pagefac = requeste.POST.get('pageFac')
        pageYout = requeste.POST.get('pageYout')
        pageAbout = requeste.POST.get('pageAbout')
        pageTwi = requeste.POST.get('pageTw')
        pageLink = requeste.POST.get('pageLink')

        if  pagefac == '' : pagefac == '#'
        if pageLink == '' : pagefac == '#'
        if pageTwi == '' : pageTwi == '#'
        if pageYout == '' : pageYout == '#'
        if pageName == '' : pageName == '#'
        if pageAbout == '' or pageTel == '':
            error = "the tel or about is empty"
            return render(requeste, 'back/error.html', {'error': error})


        try:
            myfile = requeste.FILES['myFil']
            fs = FileSystemStorage()
            fileName = fs.save(myfile.name, myfile)
            url = fs.url(fileName)
            b = Main.objects.get(pk = 2)
            b.name = pageName
            b.pageTe = pageTel
            b.about = pageAbout
            b.pagefa = pagefac
            b.pageyt = pageYout
            b.pageLink = pageLink
            b.pagetw = pageTwi
            b.picurl = url
            b.picname = fileName
            b.save()
        except:
            b = Main.objects.get(pk=2)
            b.name = pageName
            b.pageTe = pageTel
            b.about = pageAbout
            b.pagefa = pagefac
            b.pageyt = pageYout
            b.pageLink = pageLink
            b.pagetw = pageTwi
            b.picurl = url
            b.picname = fileName
            b.save()

    return render(requeste,'back/setting.html', {'site': site})
def contant(requeste):
    name = Main.objects.get(pk = 2)
    news = News.objects.all()
    lnews = News.objects.all()
    pageName = Main.objects.get(pk=2)
    popNews = News.objects.all().order_by('-newShow')[:3]
    cat = Category.objects.all()
    scat = subCategory.objects.all()
    if requeste.method == 'POST':
        name = requeste.POST.get('name')
        email = requeste.POST.get('email')
        website = requeste.POST.get('website')
        message = requeste.POST.get('msg')
        if name == '' or email == '' or website == '' or message == '':
            meg = 'you have some things empty'
            return render(requeste,'front/message.html',{'meg':meg})
        b  = Cont(Name = name,Email = email,message = message,website= website)
        b.save()
        meg = 'your message is send'
        return render(requeste,'front/message.html',{'meg':meg})

        # Contant = Contantform.objects.all()
        # Contant.name = name
        # Contant.emial = email
        # Contant.wibsite = website
        # Contant.message = message
        # Contant.save()
        # print(name,email)


    return render(requeste,'front/contant.html',{'pageName':pageName , 'news':news, 'cat':cat, 'scat':scat, 'lnews':lnews,'popNews':popNews})

def adminMessage(request):
    ConT = Cont.objects.all()
    return render(request,'back/message.html', {'Cont':ConT})

def contentDelete(requeste , pk):
    ConT = Cont.objects.all()
    b = Cont.objects.get(pk = pk )
    b.delete()

    return render(requeste,'back/message.html', {'Cont':ConT})



