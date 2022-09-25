# """
#     作者 马增龙
#     功能 1.  BMR计算器
#          2. 可以实现连续计算（直至用户选择推出）
#          3. 提示一次 直接输入全部信息  同时 输出带单位的信息
#          4. 处理异常操作
#     版本号 4.0
#     日期 2019/12/03
# """
#
#
def main():
    """
    主函数
    """
    # 询问是否退出
    y_or_n = input('是否退出程序(y/n):')
    while y_or_n != 'y':
        # # 性别
        # sex = input('请输入性别:(男性/女性)')
        # # print(type(sex))
        # # 身高
        # height = float(eval(input('请输入身高(cm):')))
        # # print(type(height))
        # # 体重
        # weight = float(eval(input('请输入体重(kg):')))
        # # print(type(weight))
        # # 年龄
        # age = int(eval(input('请输入年龄:')))
        # # print(type(age))
        #
        print('请输入以下信息,使用空格分隔开')
        # 直接赋值到字符串 input_str
        input_str = input('性别(男性/女性) 年龄 身高(cm) 体重(kg):')
        input_list = input_str.split(' ')
        # 性别
        sex = input_list[0]
        # 身高
        height = float(eval(input_list[2]))
        # 体重
        weight = float(eval(input_list[3]))
        # 年龄
        age = int(eval(input_list[1]))

        # 性别判断
        if sex == '男性':
            BMR = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
            print('您的性别:{},年龄:{}岁,体重:{}kg,身高:{}cm'.format(sex,age,weight,height))
            print('您的基础代谢率为{}大卡'.format(BMR))
        elif sex == '女性':
                BMR = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
                print('您的性别:{},年龄:{}岁,体重:{}kg,身高:{}cm'.format(sex, age, weight, height))
                print('您的基础代谢率为{}大卡'.format(BMR))
        else:
            print('暂不支持该性别BMR计算')
        print('***********************************************************')
        # 询问是否退出
        y_or_n = input('是否退出程序(y/n):')

    if y_or_n == 'y':
        print('您已经成功推出本程序')

if __name__ == '__main__':
    main()
