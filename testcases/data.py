#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
#import os
#import sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import dir_util




# data=[{'id': 0, 'txnNo': 'CMB202310071420295230000000795', 'supplierCode': 'TN2022011200000607', 'busCode': 'N39010', 'bu
# sMod': '00001', 'totalAmt': 9999.9, 'transCnt': 1, 'successAmt': 9999.9, 'successCnt': 1, 'agreementCode': 'AB0980', 'agreementT
# ype': 'BYSA', 'currency': '10', 'currencyType': None, 'bbkCode': None, 'bankAcct': '755915678710501', 'authAcct': '755915678710606', 'trans
# Remark': '砼联数科-联动代发测试', 'msgContentType': None, 'expectDate': '20231007', 'expectTime': '000000', 'operateDate': '20231007', 'nlaFlag': 'N', 'r
# eqCode': 'B150092414', 'reqStat': 'FIN', 'reqFlag': 'S', 'errorCode': None, 'errorMsg': None, 'rtbFlag': None, 'createTime': None, 'updateTime': None, '
# createUserId': None, 'updateUserId': None}, {'id': 0, 'txnNo': 'CMB202310071442268010000000797', 'supplierCode': 'TN2022011200000607', 'busCode': 'N39010
# ', 'busMod': '00001', 'totalAmt': 35000.0, 'transCnt': 3, 'successAmt': 35000.0, 'successCnt': 3, 'agreementCode': 'AB0980', 'agreementType': 'BYSA', 'curren
# cy': '10', 'currencyType': None, 'bbkCode': None, 'bankAcct': '755915678710501', 'authAcct': '755915678710606', 'transRemark': '砼联数科-联动代发测试', 'msgContent
# Type': None, 'expectDate': '20231007', 'expectTime': '000000', 'operateDate': '20231007', 'nlaFlag': 'N', 'reqCode': 'B150092415', 'reqStat': 'FIN', 'reqFlag': '
# S', 'errorCode': None, 'errorMsg': None, 'rtbFlag': None, 'createTime': None, 'updateTime': None, 'createUserId': None, 'updateUserId': None}, {'id': 0, 'txnNo':
# 'CMB202310071605049910000000799', 'supplierCode': 'TN2022011200000607', 'busCode': 'N39010', 'busMod': '00001', 'totalAmt': 5.55, 'transCnt': 5, 'successAmt': 0.0,
# 'successCnt': 0, 'agreementCode': 'AB0980', 'agreementType': 'BYSA', 'currency': '10', 'currencyType': None, 'bbkCode': None, 'bankAcct': '755915678710501', 'authA
# cct': '755915678710606', 'transRemark': '联动代发测试', 'msgContentType': '9', 'expectDate': '20231008', 'expectTime': '092000', 'operateDate': '20231007', 'nlaFlag':
# 'N', 'reqCode': 'B150092416', 'reqStat': 'NTE', 'reqFlag': None, 'errorCode': None, 'errorMsg': None, 'rtbFlag': None, 'createTime': None, 'updateTime': None, 'crea
# teUserId': None, 'updateUserId': None}, {'id': 0, 'txnNo': 'CMB202310071422134520000000796', 'supplierCode': 'TN2022011200000607', 'busCode': 'N39010', 'busMod': '0
# 0001', 'totalAmt': 35000.0, 'transCnt': 3, 'successAmt': 35000.0, 'successCnt': 3, 'agreementCode': 'AB0980', 'agreementType': 'BYSA', 'currency': '10', 'currencyTy
# pe': None, 'bbkCode': None, 'bankAcct': '755915678710501', 'authAcct': '755915678710606', 'transRemark': '砼联数科-联动代发测试', 'msgContentType': None, 'expectDate':
# '20231007', 'expectTime': '000000', 'operateDate': '20231007', 'nlaFlag': 'N', 'reqCode': 'B150092425', 'reqStat': 'FIN', 'reqFlag': 'S', 'errorCode': None, 'error
# Msg': None, 'rtbFlag': None, 'createTime': None, 'updateTime': None, 'createUserId': None, 'updateUserId': None}, {'id': 0, 'txnNo': 'CMB20231007211256514000000080
# 4', 'supplierCode': 'TN2022011200000607', 'busCode': 'N39010', 'busMod': '00001', 'totalAmt': 5.55, 'transCnt': 5, 'successAmt': 0.0, 'successCnt': 0, 'agreementC
# ode': 'AB0980', 'agreementType': 'BYSA', 'currency': '10', 'currencyType': None, 'bbkCode': None, 'bankAcct': '755915678710501', 'authAcct': '755915678710606', 't
# ransRemark': '联动代发测试', 'msgContentType': '9', 'expectDate': '20231007', 'expectTime': '235959', 'operateDate': '20231007', 'nlaFlag': 'N', 'reqCode': 'B1500924
# 26', 'reqStat': 'NTE', 'reqFlag': None, 'errorCode': None, 'errorMsg': None, 'rtbFlag': None, 'createTime': None, 'updateTime': None, 'createUserId': None, 'update
# UserId': None}, {'id': 0, 'txnNo': 'CMB202310071630088180000000803', 'supplierCode': 'TN2022011200000607', 'busCode': 'N39010', 'busMod': '00001', 'totalAmt': 5.55
# , 'transCnt': 5, 'successAmt': 0.0, 'successCnt': 0, 'agreementCode': 'AB0980', 'agreementType': 'BYSA', 'currency': '10', 'currencyType': None, 'bbkCode': None, '
# bankAcct': '755915678710501', 'authAcct': '755915678710606', 'transRemark': '联动代发测试', 'msgContentType': '9', 'expectDate': '20231007', 'expectTime': '235959',
# 'operateDate': '20231007', 'nlaFlag': 'N', 'reqCode': 'B150092427', 'reqStat': 'NTE', 'reqFlag': None, 'errorCode': None, 'errorMsg': None, 'rtbFlag': None, 'creat
# eTime': None, 'updateTime': None, 'createUserId': None, 'updateUserId': None}, {'id': 0, 'txnNo': 'CMB202310072117205220000000805', 'supplierCode': 'TN202201120000
# 0607', 'busCode': 'N39010', 'busMod': '00001', 'totalAmt': 5.55, 'transCnt': 5, 'successAmt': 0.0, 'successCnt': 0, 'agreementCode': 'AB0980', 'agreementType': 'BY
# SA', 'currency': '10', 'currencyType': None, 'bbkCode': None, 'bankAcct': '755915678710501', 'authAcct': '755915678710606', 'transRemark': '联动代发测试', 'msgConten
# tType': '9', 'expectDate': '20231007', 'expectTime': '235959', 'operateDate': '20231007', 'nlaFlag': 'N', 'reqCode': 'B150092428', 'reqStat': 'NTE', 'reqFlag': Non
# e, 'errorCode': None, 'errorMsg': None, 'rtbFlag': None, 'createTime': None, 'updateTime': None, 'createUserId': None, 'updateUserId': None}, {'id': 0, 'txnNo': '
# flag=False
# for i in range(0,i-1):
#     print(data[i]['txnNo']+'****'+'CMB202310072158166630000000818')
#     if data[i]['txnNo'] == 'CMB202310072158166630000000818':
#
#         flag=True
#
# assert flag ==True

# data={'params': {'productType': 'P00005'}, 'headers': {'Host': '172.24.100.75:10006', 'Cookie': 'Token=eyJ1c2VySWQiOiIxMzQ3NTQ3NTU0NyIsInRva2VuIjoiYzFlYzg2MGE3ZGU1NDIxOWJiZmJmMWU5NjJmMTA0MzMifQ==', 'Token': 'eyJ1c2VySWQiOiIxMzQ3NTQ3NTU0NyIsInRva2VuIjoiYzFlYzg2MGE3ZGU1NDIxOWJiZmJmMWU5NjJmMTA0MzMifQ=='}}
#
# for item in data.items():
#     if item[0] == 'params' or item[0] == 'data':
#         print("请求数据为：%s" % item[1])
#     if item[0] == 'headers':
#         print("请求头为：%s" % item[1])

#print(time_util.now_date)
path = dir_util.dir + 'data/'
print(path)
filenamelsit=['invoice01.jpg','invoice02.jpg']
print(filenamelsit)
# files = []
# i=0
# for item in filenamelsit:
#     files.append('')
#     files[i]=('file',(item,open(path+item,'rb')))
#     i = i+1
#
# print(files)

# list=[{'msg': '识别成功', 'code': 200, 'data': {'fileNo': '0496d0ed541d4e5fbb30ab830a17e5b3', 'title': '江苏增值税普通发票', 'invoiceCode': '032002200804', 'invoiceNumber': '06638835', 'invoiceType': 'normal', 'billingDate': '20230202', 'totalAmount': 99120.0, 'invoiceAmount': 98138.61, 'taxAmount': 981.39, 'checkCode': '09525969533197740116'}}, {'msg': '识别成功', 'code': 200, 'data': {'fileNo': '98a469012f714512ae4619ef2e881de6', 'title': '江苏增值税普通发票', 'invoiceCode': '032002200804', 'invoiceNumber': '06638830', 'invoiceType': 'normal', 'billingDate': '20230202', 'totalAmount': 99120.0, 'invoiceAmount': 98138.61, 'taxAmount': 981.39, 'checkCode': '0994071367810251737'}}]
#
#
# for invios,filename in zip(list,filenamelsit):
    #print(invios['data'].keys(),invios['data'].values())
    #for i,j in zip(invios['data'].keys(),invios['data'].values()):
# data=YamlUtil().read_yaml('invoiceList')[0]['data']['fileNo']
# print(data)



#print(list[0]['data'].keys(),list[0]['data'].values())


