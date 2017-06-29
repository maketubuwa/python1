from cmdb.models import *


#处理库存表
class InventoryBiz(object):	
	  #更新库存数据————————注意这里类函数要增加一个Self参数
	def UpdatingInventoryIn(self,inStockBill,inventory):
	    if (inventory.InventoryId==None):
	        inventory.Item=inStockBill.Item
	        inventory.Amount=0
	    inventory.Amount = inventory.Amount + inStockBill.Amount
	#获取当前库存
	def getInventoryByItem(self,item):
		if (item!=None):
			inventorys=item.inventory_set.all()
			if (inventorys.count()==0):
				currentInventory=Inventory()
			else:
				currentInventory=inventorys[0]
		return currentInventory
		
	def getInventoryByItemName(self,itemName):
		inventorys=None
		if itemName:
			inventorys=Inventory.objects.filter(Item__ItemName__icontains=itemName)
		else:
			inventorys=Inventory.objects.all()
		return inventorys	

#处理清单表
class InStockBillBiz(object):
	#保存入库清单并且提示输入
	def save(self,inStockBill):
		try:
			if not inStockBill.InStockBillCode:
				validMsg='入库单编号不能为空！'
			if not 	inStockBill.InStockDate:
				validMsg=validMsg+'入库单时间不能为空！'
				if validMsg !='':
					raise validMsg
			inStockBill.save()
		except Exception as e:
			raise e