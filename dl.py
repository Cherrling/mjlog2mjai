import gzip
import urllib.request
import tqdm



# 读取某一文件中的全部行，返回一个列表
def readfile(filename):
    with open(filename, 'r') as f:
        # return f.readlines()
        # 去掉每一行最后的换行符
        return [x.strip() for x in f.readlines()]


def dllinks(links):
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    # 改为tqdm
    # for i in tqdm.tqdm(links):
    for i in links:
        url = i
        req = urllib.request.Request(url=url, headers=HEADER)
        opener = urllib.request.build_opener()
        response = opener.open(req)
        response = gzip.decompress(response.read()).decode('utf-8')
        # 保存到文件，使用url最后8位作为文件名，使用utf-8编码
        with open("logs/"+i[-8:], 'w', encoding='utf-8') as f:
            f.write(response)
            
            
            
links = readfile('paipu_links')
dllinks(links)
# from concurrent.futures import ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=10) as executor:
#     executor.map(dllinks, links)