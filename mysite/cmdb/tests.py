"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from cmdb.models import *
from cmdb.cmdbBiz import InventoryBiz


class InventoryTest(TestCase):

	def test_updating_inventory_in(self):
		biz= InventoryBiz()
		#1.创建一个Item实例；
		item = Item()
		item.ItemId = 1
		item.ItemCode = '008'
		item.ItemName = '螺丝肉'
		#2.创建一个新入库单对象
		inStockBill = InStockBill()
		inStockBill.InStockBillCode='201501010001'
		inStockBill.InStockDate = '2015-01-01'
		inStockBill.Operator = '张三'
		inStockBill.Amount = 10
		inStockBill.Item = item
		#3.创建当前该物料的库存对象
		inventory = Inventory()
		inventory.InventoryId = 1
		inventory.Item=item
		inventory.Amount=10  #当前库存数量
		# 如何构建更新库存的函数，让其可具备测试调用
		biz.UpdatingInventoryIn(inStockBill,inventory)
		#校验测试是否满足当前场景
		self.assertEqual(inventory.Amount ,20)
		inventory = Inventory()
		biz.UpdatingInventoryIn(inStockBill, inventory)
		self.assertEqual(inventory.Amount, 10)
		self.assertEqual(inventory.Item.ItemId, inStockBill.Item.ItemId)