from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from firebase import Firebase
from mandel_lib import ListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from mandel_lib import *
from datetime import datetime
import time
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.widget import Widget
from kivy.uix.image import AsyncImage, Image
import tkinter as tk
from tkinter import filedialog

if platform in ('win', 'macosx'):
    Window.size = (414, 736)
    Window.top = 50
config = {'apiKey': '',
    'authDomain': 'comp7510-967e1.firebaseapp.com',
    'databaseURL': 'https://comp7510-967e1-default-rtdb.firebaseio.com/',
    'storageBucket': 'comp7510-967e1.appspot.com',
    'serviceAccount': {
        "type":
        "service_account",
        "project_id":
        "comp7510-967e1",
        "private_key_id":
        "f937fd58418bed9874d52884f4f11d6c8ef9e6f3",
        "private_key":
        "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCg/ZRlbWUp3lYp\nEs2ItstC+2H3IcW5YtpyoRC0bihqPSMlicl1thGb67eJG7p+fhMMTwwPz+Fkw9s1\n2sJIu25vGMzwv0pGM2aQ3bE8jF0F5SNTnYLlAZAP1K9Bm5Z7tZoBPeMkqlmefIO4\novw2Jatuf5TTo1hz32Rti1O1izzJ2DhBjQc7s+k+hGSheZL0bj2nI14RJDluWB0v\n6R6BRHESJuyX25RWX7wTCvBc16F+V7GcVC5wuddVIGNhpKSdZwLP78ADB6WooL4n\nJnqsOYaRC/ASJfCVBzg+h+QdMtEqu/hRbcHubLyXkYfScamCmENDlELGJTEbICVc\nuwBJnzSfAgMBAAECggEACJXCikQdVHBpqigOs38tSLBMxu0on5xgvM3PrRIrb+WR\nuxM6yImsgmLoDH+LiupLNr6ntyzP6VveaTlLX1iLaOZAK4hv5rLKrJKokcDZxxIz\nN5Fwj6jCghhGk5o/RJqTEK+NritdZcELFIIF2WyvKdB+OGj/XbJ90a+lMksEs1i8\nQPimnJLlvLRQx4HHanQ5XeJWgGg7r5a2mIJz5Z2ca91HIcuA0P+9CJztcrqr48yR\nAEQoT5CcnUDAqWxO9sIMSX0t8M/iondQZGzgNbwcTqSjyKiglPimxn7hbNiGE4l1\n+7MSLyXc8fzW/ADllIEFvYOeYABUenoSRWkI5tYTVQKBgQDSPC6oePeMduN74CuI\nmFSbU0Lmsj9tu0bv5/bvypdtI5IHJPZG5pbMgDGiiBKFWpmovm+3hy2AGoaXnJ20\nSZBQfavYPm1xa/1I/JTQcISb6sYTPrnhdeMjNUBm1cbXyu2HmMJx4vcnaw/WEu5k\nUv4SrRxc7VpptEb4wM39hZEvjQKBgQDECSLGP3UHoVnegDFRzI34RH3H+kdMnB9c\nojltCG+BmIijo8GlQJIUpkaBKykmXDv3vQDbF1XzclFho/f6vImxu43Fm/X3jy8V\nngRwepsXsUbR+Z3mpKwwWRyFcS23a2O5b4YrtVyMaCkvTLA3QEin39PMoKR1OnE/\n4zzX/yhj2wKBgQDDkmS9KLrwmnCIfkNBMKQUUmI8BblntP4KkzluXIJ9bsebidDo\np/3Eg8Sos/i2wU+MYIvAqSm0r/hg9brnSj/MAPxpj7lz98eJrB4rwWA7Qy28HXAB\nww7nY9RjVZ9Cg25v47WPCFpu+vOia74E6gedDBkEgXDIQIJ9Sa7Wlvg2yQKBgQCQ\n6OPwwiXDXy1sgTxz6A6mEBMeiU69PccdFbn3dD3hAZ03waw6eNHDO+pwPzRq69FU\nXz1LtyNNExs/XxLHISlz3V1+TrxypEA87ZMAhlExIVVlj+x9+wphru2bYr9Vj6en\nAt6eXrEsBS80jK7SGM3ccmNBJxqKoYnnnRVz4WS88wKBgQC09/0/V9psE0nMLOJn\nPx5dpb+1uh6dyZOP4GUycQX3vJCBL1aPt8xxSXuBGDhbPrhaCRitj4+tmr2SjCg6\n4GmY4uGr4WzAAaZRk9qlEhaUoMd/F5dK7XvTlOJOVTHadF+rcggS6rZDNmPeE/td\nEMrfqCS3Zg/glN4H1kXu7KFr6A==\n-----END PRIVATE KEY-----\n",
        "client_email":
        "firebase-adminsdk-2wad6@comp7510-967e1.iam.gserviceaccount.com",
        "client_id":
        "102729521868578478692",
        "auth_uri":
        "https://accounts.google.com/o/oauth2/auth",
        "token_uri":
        "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":
        "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url":
        "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2wad6%40comp7510-967e1.iam.gserviceaccount.com"
    }
}
myfirebase = Firebase(config)
db = myfirebase.database()
storage = myfirebase.storage()

class MessageItem(ListItem):
    def show_details(self):
        app = MDApp.get_running_app()
        #合并时启用下面三行代码，其余删掉      为了转移到商品详情页面
        # next = ItemDetailScreen(item_id=self.key, back=MDApp.get_running_app().current_screen.name)
        # MDApp.get_running_app().manager.add_widget(next)
        # MDApp.get_running_app().manager.current = next.name
        """
        screen = app.manager.get_screen('DetailScreen')
        screen.key = self.key
        screen.title = self.title
        screen.description = self.description
        screen.publish_time = self.publish_time
        screen.publisher = self.publisher
        screen.price = self.price
        screen.availability = self.availability
        app.manager.transition.direction = 'right'
        app.manager.current = 'DetailScreen'
        """
        

    
class ListScreen2(Screen):             #显示我的商品详情页面
    def __init__(self):
        super().__init__()
        self.item = ""
        
    def on_pre_enter(self):
        result = db.child('Items').get().val()   #从Items下获取所有商品的key和value
        if result == None:
            return
        container = self.ids.container
        username1="userID"      #待链接到需要的用户名    ？？？？？
        # MDApp.get_running_app.manager.get_screen("").item = ""
        for k, v in result.items():
            if v['publisher'] == username1:         #通过用户ID筛选要显示的物品
                item = MessageItem()
                item.title = v['title']
                item.content = v['description']

                item.post_time = datetime.fromtimestamp(int(v['publish_time'])).strftime("%Y-%m-%d %H:%M:%S")
                
                
                item.author = v['publisher']
                item.prize = "HK$"+v['price']
                item.condition = v['fenlei']
                item.key = k

                container.add_widget(item)           #把useID这个人的商品参数加到MessageItem控件里显示

    def clickrelease(self):        #跳转到发布商品页面的按钮所需的功能
        app = MDApp.get_running_app()
        app.manager.transition.direction = 'left'
        app.manager.current = 'signinscreen'
    

    def on_leave(self):         #清除控件，防止再次进入页面控件多次添加
        container = self.ids.container
        container.clear_widgets()  

class SignInScreen(Screen):
    
    
        
        
    
    def show_dialog(self):              #填信息遗漏空格时发布按钮弹dialog
        dialog = MDDialog(
            title = 'Error',
            text = 'The textfield cannot be empty.',
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_release = lambda x: dialog.dismiss()),
            ]
        )
    
        product = self.ids.product_field.text
        product = product.strip()
        details = self.ids.details_field.text
        details = details.strip()
        types = self.ids.type_field.text
        types = types.strip()
        money = self.ids.money_field.text
        money = money.strip()
   
        #root = tk.Tk()
        #root.withdraw() 
        
        #file_path = filedialog.askopenfilename()
        file_path=self.ids.picture.text
        if  len(product) == 0 or len(details) == 0 or len(types) == 0 or len(money) ==0:
            dialog.open()
        
        else:
            self.ids.label.text = 'Released Success!'
            times = int(datetime.now().timestamp())
            storage.child(f'item_img/{product}.jpg').put(file_path)   #以商品名命名图片上传到storage
            money = str(money)
            username1='userID'      #待链接到需要的用户名    ？？？？？
            data = dict(publisher=username1, description=details,publish_time=times,title=product, pictures=f'item_img/{product}.img' ,fenlei=types,price=money,availability = bool(1) ,liulancishu=0)
            response = db.child(f'/Items/').push(data)
            
            self.ids.product_field.text=""
            self.ids.details_field.text=""
            self.ids.type_field.text=""
            self.ids.money_field.text=""

    def Choose_pic(self):   
        root = tk.Tk()
        root.withdraw() 
        
        file_path = filedialog.askopenfilename()
        self.ids.picture.text=f"{file_path}"

    def Clear(self):                       #输入信息时的清除按钮
        
        self.ids.product_field.text=""
        self.ids.details_field.text=""
        self.ids.type_field.text=""
        self.ids.money_field.text=""
        
    
    def Cancel(self):                      #取消并返回我的商品页面按钮
        
        self.ids.product_field.text=""
        self.ids.details_field.text=""
        self.ids.type_field.text=""
        self.ids.money_field.text=""
        app = MDApp.get_running_app()
        app.manager.transition.direction = 'right'
        app.manager.current = 'ListScreen2'
        

class DetailScreen(Screen):               #商品详情的作废class
    def clickme(self):
        app = MDApp.get_running_app()
        app.manager.transition.direction = 'left'
        app.manager.current = 'ListScreen2'



class MyApp(MDApp):
    
    manager = None
    
    def build(self):
        
        Builder.load_file('selllist.kv')
        Builder.load_file('sellrelease.kv')
        self.manager = manager = ScreenManager()
        
        manager.add_widget(ListScreen2())
        manager.add_widget(DetailScreen())
        manager.add_widget(SignInScreen())
        return manager
    
if __name__ == '__main__':
    MyApp().run()
    