# coding=gbk
import tornado.ioloop
import tornado.web
import json

key_list = list()


def get_key(respond: str) -> list:

    # print(respond.encode())
    """
    :param respond:
    :return: 返回的格式是以列表的形式展示
    列如：[[a,b,c],[q,w,r],[s,d,f,h,j]]
    字典的key同意层级，会在同一个列表里面

    """
    try:

        respond = respond.replace('"[', "[").replace(']"', "]")
    except AttributeError as e:
        pass

    try:
        respond = json.loads(respond)
    except:
        pass
    print(respond)
    print(type(respond))

    if type(respond) == dict:
        key_list.append(list(respond.keys()))
    # print(1,respond)
    # print(type(respond))
    for key in respond.keys():

        if type(respond[key]) == dict and respond[key]:

            get_key(respond[key])

        elif type(respond[key]) == list and respond[key]:
            if type(respond[key][0]) != str:
                get_key(respond[key][0])



        else:
            pass
    [_list.sort() for _list in key_list]

    return key_list


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        data = self.get_body_arguments("confirmationText")

        respond = get_key(json.loads(data[0]))

        # print(respond)
        self.write(str(respond))
        key_list.clear()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # d = '{"code":"200","msg":null,"success":false,"t":{"pages":11,"total":105,"pageNum":1,"orderList":[{"orderId":"1291255321225855018","orderSn":"S11291255321209077831","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-06 14:10:34","serviceType":"anz","orderAmount":86.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":0,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200731/E716B6B5609C5DC3E68E2B5704889058_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"灯头10个","goodsNum":1.0}],"orderWaitExpireTime":1596953434000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1291247176768290886","orderSn":"S11291247176747319354","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-06 13:38:12","serviceType":"anz","orderAmount":86.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":0,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200731/E716B6B5609C5DC3E68E2B5704889058_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"灯头10个","goodsNum":1.0}],"orderWaitExpireTime":1596951492000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1291246085137760300","orderSn":"S11291246085074845751","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-06 13:33:52","serviceType":"anz","orderAmount":86.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":0,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200731/E716B6B5609C5DC3E68E2B5704889058_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"灯头10个","goodsNum":1.0}],"orderWaitExpireTime":1596951232000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1290888433106944064","orderSn":"S21290888433090166828","busofferno":null,"aliww":null,"sourceorderId":"","orderType":1,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-05 13:52:41","serviceType":"wx","orderAmount":0.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":2,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/85D4F54212BACA4E9EE3DA40DE717257_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"1","goodsNum":1.0}],"orderWaitExpireTime":1596865961000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":1},{"orderId":"1290561409075118147","orderSn":"S11290561409045757984","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 16:13:12","serviceType":"anz","orderAmount":100.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147981","offerWorkerImage":"da180eaba1d74ca9bc42a681589be7c0.jpg","workerQuotation":null,"workerName":"张彬彬","workerPhone":"15270019245","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/5839965E165CFC87E703F84713A09834_p106552.jpg\"]","goodsName":"门厅/玄关柜（组装）","goodsSpace":"组装","goodsNum":1.0}],"orderWaitExpireTime":1596787992000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290537541467897922","orderSn":"S11290537541451120737","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 14:38:22","serviceType":"anz","orderAmount":104.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"王涛","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/85D4F54212BACA4E9EE3DA40DE717257_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"灯头12个","goodsNum":1.0}],"orderWaitExpireTime":1596782302000,"exceptiontype":null,"isChangeOrderFee":1,"changeOrderFeeVo":[{"time":"2020-08-04 16:33:12","desc":"增加费用21.0元"}],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290536986217545729","orderSn":"S11290536986196574247","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 14:36:09","serviceType":"anz","orderAmount":55.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"王涛","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/CC3B5F48676D13EB3892F976E94118A5_p106552.jpg\"]","goodsName":"平板_现代类花灯","goodsSpace":"70cm＜直径（或最大边长）≤80cm","goodsNum":1.0}],"orderWaitExpireTime":1596782169000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290523653913444366","orderSn":"S11290523653892472865","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 13:43:11","serviceType":"anz","orderAmount":135.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":8,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"王涛","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/9D7A95FC9F7163C0E42929EE733AC6A6_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"灯头16个","goodsNum":1.0}],"orderWaitExpireTime":1596778991000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1290523504650747924","orderSn":"S11290523504629776443","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 13:42:35","serviceType":"anz","orderAmount":122.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"王涛","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/AC6D0E73791811AC846D143615D611A1_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"灯头14个","goodsNum":1.0}],"orderWaitExpireTime":1596778955000,"exceptiontype":null,"isChangeOrderFee":1,"changeOrderFeeVo":[{"time":"2020-08-04 14:48:10","desc":"增加费用20元"}],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290522735289565215","orderSn":"S21290522735272788013","busofferno":null,"aliww":null,"sourceorderId":"","orderType":1,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 13:39:31","serviceType":"anz","orderAmount":100.00,"customerName":"张三","customerPhone":"17786451825","customerAddress":"港澳香港特别行政区中西区前进一路前进二村前进小区","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":100.00,"workerName":"王涛","workerPhone":"17786451825","busofferno":null,"lowestQuotation":100.00,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/85D4F54212BACA4E9EE3DA40DE717257_p106552.jpg\"]","goodsName":"水晶/全铜/玻璃/云石类枝型吊灯","goodsSpace":"1","goodsNum":1.0}],"orderWaitExpireTime":1596778771000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0}],"userType":null}}'
    # x = get_key(d)
    # print(x)