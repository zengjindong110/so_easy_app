# coding=gbk
import tornado.ioloop
import tornado.web
import json

key_list = list()


def get_key(respond: str) -> list:

    # print(respond.encode())
    """
    :param respond:
    :return: ���صĸ�ʽ�����б����ʽչʾ
    ���磺[[a,b,c],[q,w,r],[s,d,f,h,j]]
    �ֵ��keyͬ��㼶������ͬһ���б�����

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
    # d = '{"code":"200","msg":null,"success":false,"t":{"pages":11,"total":105,"pageNum":1,"orderList":[{"orderId":"1291255321225855018","orderSn":"S11291255321209077831","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-06 14:10:34","serviceType":"anz","orderAmount":86.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":0,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200731/E716B6B5609C5DC3E68E2B5704889058_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"��ͷ10��","goodsNum":1.0}],"orderWaitExpireTime":1596953434000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1291247176768290886","orderSn":"S11291247176747319354","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-06 13:38:12","serviceType":"anz","orderAmount":86.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":0,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200731/E716B6B5609C5DC3E68E2B5704889058_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"��ͷ10��","goodsNum":1.0}],"orderWaitExpireTime":1596951492000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1291246085137760300","orderSn":"S11291246085074845751","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-06 13:33:52","serviceType":"anz","orderAmount":86.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":0,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200731/E716B6B5609C5DC3E68E2B5704889058_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"��ͷ10��","goodsNum":1.0}],"orderWaitExpireTime":1596951232000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1290888433106944064","orderSn":"S21290888433090166828","busofferno":null,"aliww":null,"sourceorderId":"","orderType":1,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-05 13:52:41","serviceType":"wx","orderAmount":0.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":2,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":null,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/85D4F54212BACA4E9EE3DA40DE717257_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"1","goodsNum":1.0}],"orderWaitExpireTime":1596865961000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":1},{"orderId":"1290561409075118147","orderSn":"S11290561409045757984","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 16:13:12","serviceType":"anz","orderAmount":100.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147981","offerWorkerImage":"da180eaba1d74ca9bc42a681589be7c0.jpg","workerQuotation":null,"workerName":"�ű��","workerPhone":"15270019245","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/5839965E165CFC87E703F84713A09834_p106552.jpg\"]","goodsName":"����/���ع���װ��","goodsSpace":"��װ","goodsNum":1.0}],"orderWaitExpireTime":1596787992000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290537541467897922","orderSn":"S11290537541451120737","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 14:38:22","serviceType":"anz","orderAmount":104.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"����","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/85D4F54212BACA4E9EE3DA40DE717257_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"��ͷ12��","goodsNum":1.0}],"orderWaitExpireTime":1596782302000,"exceptiontype":null,"isChangeOrderFee":1,"changeOrderFeeVo":[{"time":"2020-08-04 16:33:12","desc":"���ӷ���21.0Ԫ"}],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290536986217545729","orderSn":"S11290536986196574247","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 14:36:09","serviceType":"anz","orderAmount":55.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"����","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/CC3B5F48676D13EB3892F976E94118A5_p106552.jpg\"]","goodsName":"ƽ��_�ִ��໨��","goodsSpace":"70cm��ֱ���������߳�����80cm","goodsNum":1.0}],"orderWaitExpireTime":1596782169000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290523653913444366","orderSn":"S11290523653892472865","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 13:43:11","serviceType":"anz","orderAmount":135.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":8,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"����","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/9D7A95FC9F7163C0E42929EE733AC6A6_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"��ͷ16��","goodsNum":1.0}],"orderWaitExpireTime":1596778991000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":0,"requestDevelopWorker":0},{"orderId":"1290523504650747924","orderSn":"S11290523504629776443","busofferno":null,"aliww":null,"sourceorderId":"","orderType":0,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 13:42:35","serviceType":"anz","orderAmount":122.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":null,"workerName":"����","workerPhone":"17786451825","busofferno":null,"lowestQuotation":null,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/AC6D0E73791811AC846D143615D611A1_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"��ͷ14��","goodsNum":1.0}],"orderWaitExpireTime":1596778955000,"exceptiontype":null,"isChangeOrderFee":1,"changeOrderFeeVo":[{"time":"2020-08-04 14:48:10","desc":"���ӷ���20Ԫ"}],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0},{"orderId":"1290522735289565215","orderSn":"S21290522735272788013","busofferno":null,"aliww":null,"sourceorderId":"","orderType":1,"isMakeGoodsMoney":0,"isUrgent":0,"createTime":"2020-08-04 13:39:31","serviceType":"anz","orderAmount":100.00,"customerName":"����","customerPhone":"17786451825","customerAddress":"�۰�����ر�������������ǰ��һ·ǰ������ǰ��С��","offerWorkerNum":null,"lowestQuotation":0,"orderStatus":5,"isOld":0,"orderTagType":null,"orderTagNotes":null,"payMethod":0,"currentTime":null,"operationTime":null,"refusesToPay":0,"lubanPayMoney":null,"customerDesc":"","originalOrderSn":null,"orderWorkerVos":[{"workerId":"147989","offerWorkerImage":"","workerQuotation":100.00,"workerName":"����","workerPhone":"17786451825","busofferno":null,"lowestQuotation":100.00,"status":1}],"orderGoodsListVos":[{"orderImg":"[\"upload/order/20200804/85D4F54212BACA4E9EE3DA40DE717257_p106552.jpg\"]","goodsName":"ˮ��/ȫͭ/����/��ʯ��֦�͵���","goodsSpace":"1","goodsNum":1.0}],"orderWaitExpireTime":1596778771000,"exceptiontype":null,"isChangeOrderFee":0,"changeOrderFeeVo":[],"refundType":null,"psType":null,"adjustprice":0,"jsMark":0,"offerGuidance":0,"httWorkcardId":null,"relationBusinessId":null,"tbOrderId":null,"canReplenishOrder":1,"requestDevelopWorker":0}],"userType":null}}'
    # x = get_key(d)
    # print(x)