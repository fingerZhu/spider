import random
import datetime
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

pages = set()
allExtLinks = set()
allIntLinks = set()

random.seed(datetime.datetime.now())


def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是:"+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

def getInternalLinks(bsObj, includeUrl):
    """
    获取页面所有内链的列表
    """
    internalLinks = []
    # 找出所有以 "/" or .* 开头的连接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs["href"] is not None and link.attrs["href"] not in internalLinks:
            internalLinks.append(link.attrs["href"])
    return internalLinks


def getExternalLinks(bsObj, excludeUrl):
    """
    获取页面所有外链的列表
    """
    externalLinks = []
    # 找出所有以 "http" or "www" 开头且不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs["href"] is not None and link.attrs["href"] not in externalLinks:
            externalLinks.append(link.attrs["href"])
    return externalLinks


def splitAddress(address):
    return address.replace("http://", "").split("/")


def getRandomExternalLink(startingPage):
    """
    获取随机外链
    """
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj,startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("随机外链是:" + externalLink)
    followExternalOnly(externalLink)


getAllExternalLinks("http://douban.com")
