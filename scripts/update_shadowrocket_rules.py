import requests

URL = "https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_cnip_ad.conf"
ORIGINAL = "sr_cnip_ad.conf"
OUTPUT = "sr_cnip_ad_m.conf"
GROUP = """
[Proxy Group]

CORE = select,香港节点,台湾节点,日本节点,policy-select-name=香港节点

香港节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=HK|Hong|hong|香港|深港|沪港|京港|港
台湾节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=TW|Taiwan|taiwan|台湾|台北|台中|新北|彰化
韩国节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=KR|Korea|korea|KOR|韩国|首尔|韩|韓|春川
日本节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=JP|Japan|japan|Tokyo|tokyo|日本|东京|大阪|京日|苏日|沪日|上日|川日|深日|广日
新加坡节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=SG|Sing|sing|新加坡|狮城|沪新|京新|深新|杭新|广新
美国节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=US|USA|America|america|United States|美国|凤凰城|洛杉矶|西雅图|芝加哥|纽约|沪美|美
欧洲节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=EU|Europe|europe|英国|伦敦|德国|法兰克福|法国|巴黎|荷兰|阿姆斯特丹|意大利|米兰|西班牙|马德里|瑞典|斯德哥尔摩|瑞士|苏黎世|比利时|布鲁塞尔|英|德|法|荷|意|西|瑞|比
南美节点 = url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=BR|Brazil|brazil|巴西|圣保罗|里约热内卢|智利|智利圣地亚哥|阿根廷|阿根廷布宜诺斯艾利斯|墨西哥|墨西哥城|拉美|南美|巴|智|阿|墨
""".strip()


def main():
    # 1. download the file to local
    response = requests.get(URL, timeout=30)
    if response.status_code != 200:
        print(f"Failed to download file: {response.status_code}")
    else:
        with open("dotfiles/" + ORIGINAL, "wb") as f:
            f.write(response.content)
        print(f"Downloaded file: dotfiles/{ORIGINAL}")

    # 2. update the file
    #  replace ,PROXY\n with ,CORE\n
    with open("dotfiles/" + ORIGINAL, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace(",PROXY\n", ",CORE\n")
    content = content.replace(",Proxy\n", ",CORE\n")
    with open("dotfiles/" + OUTPUT, "w", encoding="utf-8") as f:
        f.write(content)

    with open("dotfiles/" + OUTPUT, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(GROUP)
    print(f"Updated file: dotfiles/{OUTPUT}")

if __name__ == "__main__":
    main()
