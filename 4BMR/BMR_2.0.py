"""
    作者 马增龙
    功能 1.BMR计算器
         2. 可以实现连续计算（直至用户选择推出）
    版本号 2.0
    日期 2019/8/23
"""


def main():
    """
    主函数
    """
    # 询问是否退出
    y_or_n = input('是否退出程序(y/n):')
    while y_or_n != 'y':
        # 性别
        sex = input('请输入性别:(男性/女性)')
        # print(type(sex))
        # 身高
        height = float(eval(input('请输入身高(cm):')))
        # print(type(height))
        # 体重
        weight = float(eval(input('请输入体重(kg):')))
        # print(type(weight))
        # 年龄
        age = int(eval(input('请输入年龄:')))
        # print(type(age))
        # 性别判断
        if sex == '男性':
            BMR = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
            print('该男性BMR为:', BMR)
        elif sex == '女性':
                BMR = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
                print('该女性BMR为:', BMR)
        else:
            print('暂不支持该性别BMR计算')
        print('***********************************************************')
        # 询问是否退出
        y_or_n = input('是否退出程序(y/n):')

    if y_or_n == 'y':
        print('您已经成功推出本程序')

if __name__ == '__main__':
    main()
