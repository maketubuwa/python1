from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from cmdb import models
from cmdb import forms
from django.db import transaction
from cmdb.cmdbBiz import InventoryBiz,InStockBillBiz
# Create your views here.


def index(request):
    # return HttpResponse('hello world')
    # return render(request, "index.html",)
    user_list = [
        {'user': 'caowei', 'password': 'abc'},
        {'user': 'zhangsan', 'password': '1234'},
    ]
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        models.UserInfo.objects.create(user=username, password=password)
        user_list = models.UserInfo.objects.all()
        # temp={'user':username,'password':password}
        # user_list.append(temp)
        # print(username,password)
    return render(request, "index.html", {'data': user_list})

#查找框
def search_form(request):
    return render_to_response('search_form.html')

# 在数据库查找内容并将结果显示到result.html 中
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 10:
            error = True
        else:
            items = models.Item.objects.filter(ItemName=q)
            return render_to_response('result.html',
                                      {'items': items, 'query': q})
        # message=r'you searched for: %r' % request.GET['q']
    return render_to_response('search_form.html', {'error': True})

# 添加物料清单
@transaction.atomic
def AddInStockBill(request):

        ##版本一：不使用Forms模版##
    # errors = []
    # items = models.Item.objects.all()
    # ItemId = ''
    # if request.method == 'POST':
    #     if not request.POST.get('InStockBillCode', ''):
    #         errors.append('Enter a In Stock Bill Code.')
    #     if not request.POST.get('InStockDate', ''):
    #         errors.append('Enter a In Stock Date.')
    #     if not request.POST.get('Amount', ''):
    #         errors.append('Enter a Amount.')
    #     if not request.POST.get('Operator', ''):
    #         errors.append('Enter a Operator.')
    #     else:
    #         ItemId = int(request.POST.get('ItemId', ''))
    #     if not errors:
    #         inStockBill = models.InStockBill()
    #         inStockBill.InStockBillCode = request.POST.get(
    #             'InStockBillCode', '')
    #         inStockBill.InStockDate = request.POST.get('InStockDate', '')
    #         inStockBill.Amount = request.POST.get('Amount', '')
    #         inStockBill.Operator = request.POST.get('Operator', '')
    #         itemId = request.POST.get('ItemId', '')
    #         inStockBill.Item = models.Item.objects.get(
    #             ItemId=itemId)  # 注意物料需要保持Model对象
    #         inStockBill.save()
    #         return HttpResponseRedirect('/success/')
    # return render(request, 'InStockAdd.html', {'errors': errors, 'items': items,
    #                                            'InStockBillCode': request.POST.get('InStockBillCode', ''),
    #                                            'InStockDate': request.POST.get('InStockDate', ''),
    #                                            'Amount': request.POST.get('Amount', ''),
    #                                            'ItemId': ItemId,
    #                                            'Operator': request.POST.get('Operator', ''), })

    ##版本二：使用Forms模版##
    if request.method == "POST":
        form = forms.InStockBillForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            inStockBill = models.InStockBill()
            inStockBill.InStockBillCode = cd["InStockBillCode"]
            inStockBill.InStockDate = cd["InStockDate"]
            inStockBill.Amount = cd['Amount']
            inStockBill.Operator = cd['Operator']
            inStockBill.Item = cd['Item']
            # inventorys=inStockBill.Item.inventory_set.all()
            # if (inventorys.count()==0):
            #     # currentInventory.Item=inStockBill.Item
            #     # currentInventory.Amount=inStockBill.Amount
            #     currentInventory=models.Inventory()
            # else:
            #     # currentInventory=inventorys[0]
            #     # currentInventory.Amount=currentInventory.Amount+inStockBill.Amount
            #     currentInventory=models.Inventory[0]
            biz=InventoryBiz()
            currentInventory=biz.getInventoryByItem(inStockBill.Item)#获得入库单物料库存
            biz.UpdatingInventoryIn(inStockBill, currentInventory)#更新库存数量
            currentInventory.save() #提交更新后的库存数据
            billBiz=InStockBillBiz()
            billBiz.save(inStockBill)#保存入库单数据
            return HttpResponseRedirect('/success/')
    else:
    	form = forms.InStockBillForm()
    return render(request,'InStockAdd.html',{'form':form})	


# 成功显示图
def success(request):
    return HttpResponse('success')


# 添加物料种类
def AddItem(request):
    if request.method == "POST":
        form = forms.ItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            item = models.Item()
            item.ItemCode = cd["ItemCode"]
            item.ItemName = cd["ItemName"]
            item.Remark = cd["Remark"]
            item.save()
            return HttpResponseRedirect('/success/')
    else:
        form = forms.ItemForm()
    return render(request, 'ItemAdd.html', {'form': form})

# 更新库存 已移植到cmdbBiz.py
# def UpdatingInventoryIn(inStockBill,inventory):
#     if (inventory.InventoryId==None):
#         inventory.Item=inStockBill.Item
#         inventory.Amount=0
#     inventory.Amount = inventory.Amount + inStockBill.Amount

def inventoryQuery(request):
    error=False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error=True
        elif len(q)>20:
            error=True
        else:
            biz=InventoryBiz()
            inventorys = biz.getInventoryByItemName(q)
            return render(request,'inventoryQuery.html',{'inventorys':inventorys,'query':q})
    return render(request,"inventoryQuery.html", {'error': error})

def getInventoryByItemName(request):
    error=False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error=True
        elif len(q)>20:
            error=True
        else:
            biz=InventoryBiz()
            inventorys = biz.getInventoryByItemName(q)
            inventorysJson=u'['
            for inventory in inventorys:
                inventorysJson=inventorysJson+u'{"InventoryId":"' + str( inventory.InventoryId)
                +u'","ItemName":"' + inventory.Item.ItemName
                +u'","Amount":"' + str( inventory.Amount) + u'"}'
            inventorysJson = inventorysJson +u']'
    return HttpResponse(inventorysJson)         
               
def inventoryQueryExtjs(request):

    return render_to_response('inventoryQueryExtjs.html')