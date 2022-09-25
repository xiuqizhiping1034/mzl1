"""    作者  马增龙
    时间  2019 3 9
    功能  汇率转换(将人名币转换成美元)
    版本号  v_1
"""
#   人民币输入
#   输入的是字符串
rmb_str_value = input('请输入人名币金额：')
#   将字符串转换成数值（人民币真值）
rmb_value = eval(rmb_str_value)
#   汇率转转换
USE_VS_RMB = 5
#   美元真值
use_value = rmb_value / USE_VS_RMB
#   美元输出
print('美元（USE）金额是：', use_value)




