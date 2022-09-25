"""
  作者  马增龙
      时间  2019 8 13
     版本号 5.0
     案例描述  根据输入的数据判断是美元还是人民币，进行相应的转换
             并且根据用户需求来判断是否退出
             程序可以一直运行 直到用户选择退出
             将汇率兑换功能封装到函数中实现功能模块化
             1.使程序结构化 2. 简单函数的定义

     案例分析
     1. 据输入判断是人名币还是美元
         ·使输入的数据带有单位 便可以区分美元还是人民币
     2.  具体计算
         ·人民币 除于 汇率 = 美元
         · 美元  乘  汇率 =  人民币
"""
# """
# 使用函数进行汇率转换
# """
#
#
# # 货币转换函数
# def convert_currency(im, er):
#     out = im * er
#     return out


"""
主函数
"""


def main():
    #   原始汇率
    RMB_VS_RMB = 5

    #   带单位货币输入
    currency_str_value = input('请输入带单位的货币金额:')

    #   获取输入数据的单位
    dan_wei = currency_str_value[-3:]

    #   判断是否是人名币
    if dan_wei == 'RMB':
        # #   真实汇率
        HuiLv = 1/RMB_VS_RMB
    elif dan_wei == 'USD':
        # #   真实汇率
        HuiLv = RMB_VS_RMB
    else:
        # #   真实汇率
        HuiLv = -1
    if HuiLv != -1:
        # 获取输入的货币数值并且将字符串转换成数值
        the_value = eval(currency_str_value[:-3])
        # 使用lambad进行函数简化定义
        convert_currency = lambda x : x * HuiLv

        # 调用lambad进行计算
        out_value = convert_currency(the_value)

        print('转换后的货币数值是', out_value)
    else:
        # #     其他情况
        print('**************************************************')
        print('目前版本尚不支持该货币')

"""
直接使用函数进行功能实现
"""

if __name__ == '__main__':
    main()