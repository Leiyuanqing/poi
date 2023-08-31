import scrapy
from meituan.items import MeituanItem
import json
import time


class MeishiSpider(scrapy.Spider):
    name = 'meishi'
    allowed_domains = ['www.meituan.com']    
    start_urls = ['http://www.meituan.com/']
    with open("beijing.json", 'r', encoding='utf-8') as json_f:
        beijing = json.load(json_f)
        urls = []
        city_ids = []
        city_names = []
        for i in beijing:
            city_ids.append(i.get("city_id"))
            city_names.append(i.get("city_name"))
            url = 'http://' + i.get("city_acronym") + ".meituan.com//meishi"
            urls.append(url)
            # cookies = "_lxsdk_cuid=181247a41b4c8-0a853d262ea19f-17333270-1fa400-181247a41b4c8; cityname=%E5%8C%97%E4%BA%AC; IJSESSIONID=node018bg7ptcbqptah9zrshk2340712560886; iuuid=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; _lxsdk=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; webp=1; __utma=74597006.131227594.1654174431.1654174431.1654174431.1; __utmc=74597006; __utmz=74597006.1654174431.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ci3=1; meishi_ci=1; cityid=1; _hc.v=ebcbf12c-125d-67ee-642f-f656c255c9d1.1654174443; latlng=40.00532,116.320601,1654174754205; i_extend=H__a100002__b1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ci=1; rvct=1%2C1122; uuid=a847dfd6507b4f32a90d.1654174869.1.0.0; mtcdn=K; userTicket=ZFPEgqEKwgyxtTQzuefLDwisqbCRmthDppVQNsYE; lt=3BvYRrGjhcDCBvw_nYzcR7fhrw8AAAAAOBIAAPca6f-hKG52vBQWn1Qcnrfp2mYNNOhYPqreCL0cBK1E_CWHJ4gyLclmsRZ-rKcjsA; u=223112229; n=Nkv626778498; token2=3BvYRrGjhcDCBvw_nYzcR7fhrw8AAAAAOBIAAPca6f-hKG52vBQWn1Qcnrfp2mYNNOhYPqreCL0cBK1E_CWHJ4gyLclmsRZ-rKcjsA; unc=Nkv626778498; lat=39.908295; lng=116.297513; client-id=42c3d974-a9ae-4308-a78b-cefa8b7baaa1; firstTime=1654777588331; _lxsdk_s=181485575df-9eb-a03-7ce%7C%7C13"
            # cookies = "_lxsdk_cuid=181247a41b4c8-0a853d262ea19f-17333270-1fa400-181247a41b4c8; cityname=%E5%8C%97%E4%BA%AC; IJSESSIONID=node018bg7ptcbqptah9zrshk2340712560886; iuuid=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; _lxsdk=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; webp=1; __utma=74597006.131227594.1654174431.1654174431.1654174431.1; __utmc=74597006; __utmz=74597006.1654174431.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ci3=1; meishi_ci=1; cityid=1; _hc.v=ebcbf12c-125d-67ee-642f-f656c255c9d1.1654174443; i_extend=H__a100002__b1; ci=1; rvct=1%2C1122; uuid=a847dfd6507b4f32a90d.1654174869.1.0.0; userTicket=ZFPEgqEKwgyxtTQzuefLDwisqbCRmthDppVQNsYE; lat=39.908295; lng=116.297513; __mta=220656167.1654174787382.1654785724646.1654843562900.16; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; mtcdn=K; lt=_zHHf6ZqDkGbIHrOqUwTKldOigAAAAAAexIAAPvZFRVDEREF2MFRBlpx4jGzemlw6SnWCIVQRX2q4hAWD5V5HViV7SZKfXY84pDxkQ; u=223112229; n=Nkv626778498; token2=_zHHf6ZqDkGbIHrOqUwTKldOigAAAAAAexIAAPvZFRVDEREF2MFRBlpx4jGzemlw6SnWCIVQRX2q4hAWD5V5HViV7SZKfXY84pDxkQ; unc=Nkv626778498; client-id=a04e67ae-9090-4d95-b9cc-d55241c83983; firstTime=1656060355712; _lxsdk_s=18194de30df-270-835-3c3%7C%7C26"
            # cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}    

    def parse(self, response):
        print("response")
        print(response)
        url = response.meta['url']
        item = MeituanItem()
        page = response.url.split("/")[-2]
        name = response.meta['city_name']
        filename = 'quotes-%s-%s.html' % (name, page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)
        print("data")
        data = response.selector.xpath('//script[10]/text()').extract()
        '''
        data = response.json()
        # data = exec(data[0])
        print(data)
        print(type(data))
        print(len(data))
        new_data = data['poiLists']['poiInfos']
        for i in new_data:
            item['meishi_poiId'] = i['poiId']
            item['meishi_avgScore'] = i['avgScore']
            yield item
        '''
        for i in data:
            if i.startswith('window._appState'):
                print('---------------------start----------------')
                items = i.split('=', 1)[1]
                new_items = items[:-1]
                data = json.loads(new_items)
                datum = data['poiLists']['poiInfos']
                for j in datum:
                    print("title: " + str(j['title']))
                    print("avgScore: " + str(j['avgScore']))
                    print("avgPrice: " + str(j['avgPrice']))
                    item['name'] = j['title']
                    item['avgScore'] = j['avgScore']
                    item['avgPrice'] = j['avgPrice']
                    item['type'] = "0"
                    yield item
                page = data['pn']
                num = len(data['poiLists']['poiInfos'])
                print("数量： ", num)
                if num == 15:
                    page += 1
                    next_page = '//pn' + str(page) + '/'
                    next_url = url + next_page
                    print("下一页： ", next_url)
                    cookies = "_lxsdk_cuid=181247a41b4c8-0a853d262ea19f-17333270-1fa400-181247a41b4c8; cityname=%E5%8C%97%E4%BA%AC; IJSESSIONID=node018bg7ptcbqptah9zrshk2340712560886; iuuid=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; _lxsdk=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; webp=1; __utma=74597006.131227594.1654174431.1654174431.1654174431.1; __utmc=74597006; __utmz=74597006.1654174431.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ci3=1; meishi_ci=1; cityid=1; _hc.v=ebcbf12c-125d-67ee-642f-f656c255c9d1.1654174443; i_extend=H__a100002__b1; ci=1; rvct=1%2C1122; uuid=a847dfd6507b4f32a90d.1654174869.1.0.0; userTicket=ZFPEgqEKwgyxtTQzuefLDwisqbCRmthDppVQNsYE; lat=39.908295; lng=116.297513; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; mtcdn=K; client-id=a04e67ae-9090-4d95-b9cc-d55241c83983; lt=Epw7BaXQGnoY0HUwIWf4qdyjVOcAAAAAexIAAOIN1K_oLenWsm9x-3zS_xB7PR48uGQxM-xYXB7VQUEFnyfjReU7uHLN2vUo3VCqYQ; u=223112229; n=Nkv626778498; token2=Epw7BaXQGnoY0HUwIWf4qdyjVOcAAAAAexIAAOIN1K_oLenWsm9x-3zS_xB7PR48uGQxM-xYXB7VQUEFnyfjReU7uHLN2vUo3VCqYQ; __mta=220656167.1654174787382.1656080342301.1656080473370.22; firstTime=1656080473376; unc=Nkv626778498; _lxsdk_s=181961492e6-c83-530-61f%7C%7C16"
                    cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
                    request = scrapy.Request(url=next_url, callback=self.parse, cookies=cookies, dont_filter=True)
                    request.meta['url'] = url
                    request.meta['city_name'] = name
                    time.sleep(5)
                    yield request
                else:
                    print('最后一页')

    def start_requests(self):
        for i in range(len(self.urls)):
            # url = 'http://' + i.get("city_acronym") + ".meituan.com//meishi"
            # cookies = "_lxsdk_cuid=181247a41b4c8-0a853d262ea19f-17333270-1fa400-181247a41b4c8; cityname=%E5%8C%97%E4%BA%AC; IJSESSIONID=node018bg7ptcbqptah9zrshk2340712560886; iuuid=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; _lxsdk=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; webp=1; __utma=74597006.131227594.1654174431.1654174431.1654174431.1; __utmc=74597006; __utmz=74597006.1654174431.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ci3=1; meishi_ci=1; cityid=1; _hc.v=ebcbf12c-125d-67ee-642f-f656c255c9d1.1654174443; latlng=40.00532,116.320601,1654174754205; i_extend=H__a100002__b1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ci=1; rvct=1%2C1122; uuid=a847dfd6507b4f32a90d.1654174869.1.0.0; mtcdn=K; userTicket=ZFPEgqEKwgyxtTQzuefLDwisqbCRmthDppVQNsYE; lt=3BvYRrGjhcDCBvw_nYzcR7fhrw8AAAAAOBIAAPca6f-hKG52vBQWn1Qcnrfp2mYNNOhYPqreCL0cBK1E_CWHJ4gyLclmsRZ-rKcjsA; u=223112229; n=Nkv626778498; token2=3BvYRrGjhcDCBvw_nYzcR7fhrw8AAAAAOBIAAPca6f-hKG52vBQWn1Qcnrfp2mYNNOhYPqreCL0cBK1E_CWHJ4gyLclmsRZ-rKcjsA; unc=Nkv626778498; lat=39.908295; lng=116.297513; client-id=42c3d974-a9ae-4308-a78b-cefa8b7baaa1; firstTime=1654777588331; _lxsdk_s=181485575df-9eb-a03-7ce%7C%7C13"
            # cookies = "_lxsdk_cuid=181247a41b4c8-0a853d262ea19f-17333270-1fa400-181247a41b4c8; cityname=%E5%8C%97%E4%BA%AC; IJSESSIONID=node018bg7ptcbqptah9zrshk2340712560886; iuuid=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; _lxsdk=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; webp=1; __utma=74597006.131227594.1654174431.1654174431.1654174431.1; __utmc=74597006; __utmz=74597006.1654174431.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ci3=1; meishi_ci=1; cityid=1; _hc.v=ebcbf12c-125d-67ee-642f-f656c255c9d1.1654174443; i_extend=H__a100002__b1; ci=1; rvct=1%2C1122; uuid=a847dfd6507b4f32a90d.1654174869.1.0.0; userTicket=ZFPEgqEKwgyxtTQzuefLDwisqbCRmthDppVQNsYE; lat=39.908295; lng=116.297513; __mta=220656167.1654174787382.1654785724646.1654843562900.16; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; mtcdn=K; lt=_zHHf6ZqDkGbIHrOqUwTKldOigAAAAAAexIAAPvZFRVDEREF2MFRBlpx4jGzemlw6SnWCIVQRX2q4hAWD5V5HViV7SZKfXY84pDxkQ; u=223112229; n=Nkv626778498; token2=_zHHf6ZqDkGbIHrOqUwTKldOigAAAAAAexIAAPvZFRVDEREF2MFRBlpx4jGzemlw6SnWCIVQRX2q4hAWD5V5HViV7SZKfXY84pDxkQ; unc=Nkv626778498; client-id=a04e67ae-9090-4d95-b9cc-d55241c83983; firstTime=1656060355712; _lxsdk_s=18194de30df-270-835-3c3%7C%7C26"
            # cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
            cookies = "_lxsdk_cuid=181247a41b4c8-0a853d262ea19f-17333270-1fa400-181247a41b4c8; cityname=%E5%8C%97%E4%BA%AC; IJSESSIONID=node018bg7ptcbqptah9zrshk2340712560886; iuuid=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; _lxsdk=D97406811B1633B92CEC48D696E8AA6245A00570D0AF2FDBC2F8A9E2BA431E1D; webp=1; __utma=74597006.131227594.1654174431.1654174431.1654174431.1; __utmc=74597006; __utmz=74597006.1654174431.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ci3=1; meishi_ci=1; cityid=1; _hc.v=ebcbf12c-125d-67ee-642f-f656c255c9d1.1654174443; i_extend=H__a100002__b1; ci=1; rvct=1%2C1122; uuid=a847dfd6507b4f32a90d.1654174869.1.0.0; userTicket=ZFPEgqEKwgyxtTQzuefLDwisqbCRmthDppVQNsYE; lat=39.908295; lng=116.297513; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; mtcdn=K; client-id=a04e67ae-9090-4d95-b9cc-d55241c83983; lt=Epw7BaXQGnoY0HUwIWf4qdyjVOcAAAAAexIAAOIN1K_oLenWsm9x-3zS_xB7PR48uGQxM-xYXB7VQUEFnyfjReU7uHLN2vUo3VCqYQ; u=223112229; n=Nkv626778498; token2=Epw7BaXQGnoY0HUwIWf4qdyjVOcAAAAAexIAAOIN1K_oLenWsm9x-3zS_xB7PR48uGQxM-xYXB7VQUEFnyfjReU7uHLN2vUo3VCqYQ; __mta=220656167.1654174787382.1656080342301.1656080473370.22; firstTime=1656080473376; unc=Nkv626778498; _lxsdk_s=181961492e6-c83-530-61f%7C%7C16"
            cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
            request = scrapy.Request(url=self.urls[i], callback=self.parse, cookies=cookies)
            # request.meta['city_id'] = self.urls[i].get("city_id")
            request.meta['city_id'] = self.city_ids[i]
            request.meta['city_name'] = self.city_names[i]
            request.meta['url'] = self.urls[i]
            print(request)
            yield request
