'''
     作者  马增龙
     时间  2019 3 9
    版本号 3.0
    案例描述  根据输入的数据判断是美元还是人民币，进行相应的转换
            并且根据用户需求来判断是否退出
            程序可以一直运行 直到用户选择退出
    案例分析
    1. 据输入判断是人名币还是美元
        ·使输入的数据带有单位 便可以区分美元还是人民币
    2.  具体计算
        ·人民币 除于 汇率 = 美元
        · 美元  乘  汇率 =  人民币
'''

#   带单位货币输入
currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q):')

i = 0

while currency_str_value != 'Q':
    i = i + 1
    print('运行了', i, '次')
    #   获取输入数据的单位
    dan_wei = currency_str_value[-3:]

    #   判断是否是人名币
    if dan_wei == 'RMB' :

        # pass        占位符
        # 输入的是人民币
        rmb_str_value = currency_str_value[:-3]
        #   将字符串转换成数值（人民币真值）
        rmb_value = eval(rmb_str_value)
        #   汇率转换
        USE_VS_RMB = 5
        #   美元真值
        usb_a_value = rmb_value / USE_VS_RMB
        #   美元输出
        print('美元（USD）金额是：', usb_a_value,'USD')
    elif dan_wei == 'USD' :
        # pass        占位符
        # print(currency_str_value[:3])
        # 输入的是美元
        usd_str_value = currency_str_value[:-3]
        #   将字符串转换成数值（人民币真值）
        usd_value = eval(usd_str_value)
        #   汇率转转换
        RMB_VS_RMB = 5
        #   美元真值
        rmb_a_value = usd_value * RMB_VS_RMB
        #   美元输出
        print('人民币（RMB）金额是：', rmb_a_value,'RMB')

    else:
    #     其他情况
        print('目前版本尚不支持该货币')
    print('**************************************************')
    # 带单位货币输入
    currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q):')

print('程序已经退出')