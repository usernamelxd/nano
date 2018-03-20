from django.shortcuts import render

# Create your views here.
from.models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodTypes,Goods


def home(request):
    sliderlist = Wheel.objects.all()
    navlist = Nav.objects.all()
    mustbuylist = Mustbuy.objects.all()
    shoplist = Shop.objects.all()
    shoplist1 = shoplist[0]
    shoplist2 = shoplist[1:3]
    shoplist3 = shoplist[3:7]
    shoplist4 = shoplist[7:11]
    mainshowlist = MainShow.objects.all()

    return render(request, "axf/home/home.html",{"sliderlist":sliderlist,"navlist":navlist,"mustbuylist":mustbuylist,"shoplist1":shoplist1,"shoplist2":shoplist2,"shoplist3":shoplist3,"shoplist4":shoplist,"mainshowlist":mainshowlist})
def market(request,gid):
    #左侧分组信息列表
    leftmenu = FoodTypes.objects.all()

    #展示组的商品列表
    productlist = Goods.objects.filter(categoryid=gid)

    #获取子组

    return render(request, "axf/market/market.html",{"leftmenu":leftmenu,"productlist":productlist})
def cart(request):
    return render(request, "axf/cart/cart.html")
def mine(request):
    return render(request, "axf/mine/mine.html")