#定义全局变量
money = 5000000
name=None
#要求输入客户姓名
name=input('请输入您的姓名')
#定义相关查询函数
def query(show_header):#用于控制表头是否显示，如果为show_header为True，则显示，否则就不显示
    if show_header:
        print('---------查询余额---------')
    print(f'您好，您的余额剩余：{money}元')
#定义存款函数
def saving(num):
#使用global在函数内部进行全局变量定义可是修改全局变量的值，不然修改不了
    global money
    money+=num
    print('---------存款-----------')
    print(f'{name},您好，您存款{num}元成功')
#调用查询函数，查询余额，不显示表头
    query(False)
#定义取款函数
def get_money(num):
    global money
    money-=num
    print('--------取款--------')
    print(f'{name},您好，您取款{num}元成功')
    query(False)
#定义主菜单
def main():
    print('---------主菜单---------')
    print(f'{name},您好，欢迎来到黑马银行ATM，请选择操作：')
    print('查询余额\t[输入1]')
    print('存款\t\t[输入2]')
    print('取款\t\t[输入3]')
    print('退出\t\t[输入4]')
    return input('请输入您的选择：')  #返回值为输入的值
#设置无限循环，确保程序不会被退出
while True:         #无限循环
    Keyboard_input=main()   #调取从主函数输入的数字
    if Keyboard_input=='1':
        query(True)
        continue  #通过contiune继续下一次轮换，一进来回到了主菜单
    elif Keyboard_input=='2':
        num=int(input('您想要存入多少钱，请输入：'))
        saving(num)
        continue
    elif Keyboard_input=='3':
        num=int(input('您想要取多少钱，请输入'))
        get_money(num)
        continue
    else:
        print('程序退出了')
        break      #跳出程序
        
    
        
    