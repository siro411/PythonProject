import requests
url='https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png'
resp=requests.get(url)

#保存到本地
with open('logo.png','wb') as file:
    file.write(resp.content)