from http.cookies import SimpleCookie
from urllib.parse import urlparse,parse_qs,urlencode
import json

URL='https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.5691421845703%2C%22east%22%3A-80.02943881542967%2C%22south%22%3A25.544151933097154%2C%22north%22%3A25.908002683131727%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D&wants={%22cat1%22:[%22listResults%22],%22cat2%22:[%22total%22]}&requestId=5'

def Cookie_Parser():
    cookie_string='zguid=23|%2452c9e77c-79b4-44f3-9fac-1376ffb16e7b; _ga=GA1.2.1784285188.1624291934; zjs_user_id=null; zjs_anonymous_id=%2252c9e77c-79b4-44f3-9fac-1376ffb16e7b%22; _pxvid=8f0ab4b8-d2ab-11eb-9206-0242ac120008; _gcl_au=1.1.1941327121.1624291936; __pdst=6c01973708b74fe49a5aa220726fb32f; _fbp=fb.1.1624291940385.367276719; _pin_unauth=dWlkPVpqSm1ZamRtTW1ZdE1qTXpNQzAwTlRoaExXRTNNekV0T1RSbE5HVmtaVFU0WVdNdw; __gads=ID=5b6cc5f5d9656e1f-22c0b6efa7c90046:T=1624292131:S=ALNI_MZUimE8EuBPjco2hD0V2SLjkUvcxw; FSsampler=1260394191; zgsession=1|135c1566-c6d3-4abe-afaf-d7ebb03d5da6; _gid=GA1.2.1050988026.1626244110; KruxPixel=true; DoubleClickSession=true; utag_main=v_id:017a2f580ef60002b77b38e19f6004072001706a00978$_sn:6$_se:1$_ss:1$_st:1626245915447$dc_visit:5$ses_id:1626244115447%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session; JSESSIONID=4FA8918367CCBC048C65867612C8FE4A; KruxAddition=true; _pxff_bsco=1; optimizelyEndUserId=oeu1626244577144r0.024670213697753685; _gat=1; _cs_mk=0.4718776799875597_1626244585391; _cs_c=1; _cs_id=fadf6308-bdc4-a2d6-fe47-ad4a2ce8a88e.1626244588.1.1626244588.1626244588.1.1660408588296.Lax.0; _cs_s=1.1.0.1626246388298; __CT_Data=gpv=1&ckp=tld&dm=zillow.com&apv_82_www33=1&cpv_82_www33=1; _px3=03f86e0b799b09e61d5760f3d89b7590eb5f2b7276aff0558f1ea757cb72011a:mHos0DIX00ddAOYq3qIg5uqz2domc9Omp0WdOAl1xmErJ9V0UPgwSuFes1sX4ykbFy+1TBC47mVPAwuoH9boVQ==:1000:J5Wcjwm+PeZnivu6keUhRZzBmg/9twQ+XHcajllJK/7z+B3zy/VrFeacOT5phMESD5yJ3HP5b5mdyl0KGDhaUKTS46VHo0gVTUDw/KtnIGIxxA/gor3Lj6aNUIgODVrjbE7ow39BRK6aQ3mWnmkDDKb7Z7oexnZjrqtzTjFNjszeEgmIC3ofgdKWcuMg3TTxakeY4Hs2tq2v4z4n0NvaUg==; _uetsid=b95b0cb0e46c11ebb903d9df661bed06; _uetvid=7255c3b0d2ab11eb8730ad34a61371ef; AWSALB=nA8k2WFkjLbsbEy2pzeliid61td/lr9f9O4n/BaSmNcoOMR5/Ix5hvdb7H9XQsACwLgdGZ1ZHEe9cY+vkwCzySvOOw+MGtv6KrMcHchDAl8AKB0p1w45wKbEH5/u; AWSALBCORS=nA8k2WFkjLbsbEy2pzeliid61td/lr9f9O4n/BaSmNcoOMR5/Ix5hvdb7H9XQsACwLgdGZ1ZHEe9cY+vkwCzySvOOw+MGtv6KrMcHchDAl8AKB0p1w45wKbEH5/u; search=6|1628836705790%7Crect%3D25.908002683131727%252C-80.02943881542967%252C25.544151933097154%252C-80.5691421845703%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0912700%09%09%09%09%09%09  '
    cookie=SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}
    for key,morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies
    #print(cookie.items())
def parse_new_url(url,page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    #print(type(search_query_state))
    encoded_qs = urlencode(query_string,doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url

    #print(query_string)

#Cookie_Parser()
#parse_new_url(URL,6)
