import requests
from bs4 import BeautifulSoup as bs

url="http://codeforces.com/ratings"
page=requests.get(url)
# print(page)
# print(page.text)
soup=bs(page.text,"html.parser")

res=soup.findAll("a",{"class":"rated-user user-legendary"})

# print(res)
each_url_basic="http://codeforces.com/profile/"
ct=0
my_list=[]
for each_tag in res:
	if(ct<=12):
		ct+=1
	else:

		name=each_tag.__str__().split(" ")[6].split('"')[0]
		my_list.append(name)


for i in my_list:
	each_url=each_url_basic+i
	each_page=requests.get(each_url)
	each_soup=bs(each_page.text,"html.parser")
	each_res=each_soup.findAll("span",{"style":"color:green;font-weight:bold;"})
	each_res2=each_soup.findAll("span",{"class":"format-humantime"})
	if(each_res!=[]):
		contri=(each_res.__str__().split("+")[1].split("<")[0])
		# print(contri)
		# print(i)
		if(each_res2.__str__().find(",")!=-1):
			years=(each_res2.__str__().split(",")[1].split(">")[1].split(" ")[0])
		else:
			years=(each_res2.__str__().split(">")[1].split(" ")[0])
	else:
		contri="0"
	print(i+"\t=>\n\t\t"+contri+" contributions in "+years+" years ")