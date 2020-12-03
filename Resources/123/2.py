#!pypy3
import requests
from bs4 import BeautifulSoup
from bs4 import Tag
import re
from time import *
import random
import pickle
import urllib

class 从者素材类:
    def __init__(self):
        self.index=0
        self.name=''
        self.star=0
        self.class_=''
        #0-3 -> 0-3
        self.tp突破list=[[] for i in range(4)]
        #1-9 -> 0-8
        self.jn技能list=[[] for i in range(9)]

    def __str__(self):
        ret=''
        ret+=self.index
        ret+=','+self.name
        ret+=','+self.star
        ret+=','+self.class_

        for tp突破 in self.tp突破list:
            c=0
            for sc素材 in tp突破:
                ret+=','+sc素材
                c+=1
            for i in range(c,5):
                ret+=','
        for jn技能 in self.jn技能list:
            c=0
            for sc素材 in jn技能:
                ret+=','+sc素材
                c+=1
            for i in range(c,5):
                ret+=','
        return ret





if __name__ == "__main__":
    output=""
    # output_file=open('output','w')
    # output_file.close()

    ret=[]
    file_out=open('2','w')

    import os

    for filename in os.listdir('./1'):
        # print('[*]current_file '+filename)

        file_in=open('./1/'+filename,'r')
        html=file_in.read()

        index=re.search(r'No.(\d{3})',html).group(1)
        index=str(int(index)+1)
        # print(index)

        name=filename
        star=re.search(r'(\d)星.png',html).group(1)
        # print(star)

        class_=re.search(r'alt=".卡(.*?)\.png"',html).group(1)
        # print(class_)


        czsc从者素材=从者素材类()
        czsc从者素材.index=index
        czsc从者素材.name=name
        czsc从者素材.star=star
        czsc从者素材.class_=class_

        
        # break


        # print(html)
        soup = BeautifulSoup(html, 'html.parser')


        def 灵基再临(tag):
            for childTag in tag.children:
                if isinstance(childTag, Tag) and 'id' in childTag.attrs and childTag['id']=='灵基再临（从者进化）':
                    return True
            return False
        info_element = soup.find_all(灵基再临)
        # print(info_element)

        table=info_element[0].next_sibling.next_sibling
        # print(table)
        

        trs=table('tr')
        for tr in trs:
            sc素材list=None
            i=1
            for tag in tr.children:
                if isinstance(tag,Tag):
                    if tag.name=='th':
                        content=tag.contents[0]
                        content=re.sub(r'[\s]','',content)
                        if len(content)>=3:
                            index=int(content[0])
                            sc素材list=czsc从者素材.tp突破list[index]
                        else:
                            sc素材list=None
                    elif tag.name=='td':
                        for dataTag in tag.children:
                            if isinstance(dataTag,Tag):
                                if dataTag.name=='div':
                                    itemName=dataTag('a')[0]['title'] if 'title' in dataTag('a')[0].attrs else 'QP'
                                    itemNumber=dataTag('span')[0].contents[0]
                                    itemNumber=re.sub(r'[^0-9万]','',str(itemNumber))
                                    if sc素材list!=None and itemName!='QP':
                                        sc素材list.append(itemName+'*'+itemNumber)


                # break # tag


            # break #tr

        def 技能强化(tag):
            for childTag in tag.children:
                if isinstance(childTag, Tag) and 'id' in childTag.attrs and childTag['id']=='技能强化':
                    return True
            return False
        info_element = soup.find_all(技能强化)
        # print(info_element)

        table=info_element[0].next_sibling.next_sibling
        # print(table)
        

        trs=table('tr')
        for tr in trs:
            sc素材list=None
            i=1
            for tag in tr.children:
                if isinstance(tag,Tag):
                    if tag.name=='th':
                        content=tag.contents[0]
                        content=re.sub(r'[\s]','',content)
                        if len(content)>=3:
                            index=int(content[0])-1
                            sc素材list=czsc从者素材.jn技能list[index]
                        else:
                            sc素材list=None
                    elif tag.name=='td':
                        for dataTag in tag.descendants:
                            if isinstance(dataTag,Tag):
                                if dataTag.name=='div':
                                    itemName=dataTag('a')[0]['title'] if 'title' in dataTag('a')[0].attrs else 'QP'
                                    itemNumber=dataTag('span')[0].contents[0]
                                    itemNumber=re.sub(r'[^0-9万]','',str(itemNumber))
                                    if sc素材list!=None and itemName!='QP':
                                        sc素材list.append(itemName+'*'+itemNumber)


                # break # tag


            # break #tr

        czsc从者素材str=str(czsc从者素材)
        czsc从者素材str=re.sub(r'巨人的戒指','巨人的指环',czsc从者素材str)
        czsc从者素材str=re.sub(r'祸罪之箭头','祸罪的箭镞',czsc从者素材str)
        print(czsc从者素材str)
        ret.append(czsc从者素材str)
        
        # break #file
    ret.sort(key=lambda x:int(x[:3]))
    for x in ret:
        print(x,file=file_out)

    file_out.close()
        


