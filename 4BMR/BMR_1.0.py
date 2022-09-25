"""
    作者 马增龙
    功能 BMR计算器
    版本号 1.0
    日期 2019/8/23
"""
import pymssql


def main():
    """
    主函数
    """
    sex = input('请输入性别')
    height = eval(input('请输入身高'))
    weight = eval(input('请输入体重'))
    age = eval(input('请输入年龄'))
    if sex == '男性':
        BMR = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        print('该男性BMR为', BMR)
    elif sex == '女性':
            BMR = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
            print('该女性BMR为', BMR)
    else:
        print('暂不支持该性别BMR计算')


if __name__ == '__main__':
    main()


