# 等额本息月供计算，P=贷款总额，nlx=年利率，month=贷款月数     【返回值】A=月供
def debx_calac(P, nlx, month):
    # 公式里用的为月利率，年利率需要换算为月利率
    i = nlx / 12
    n = month
    A = P * (i * ((1 + i) ** n) / (((1 + i) ** n) - 1))  # 等额本息月供计算公式
    return A


# 计算贷款的实际利率（已知月供），P=贷款总额，A=月供，month=贷款月数，【返回值】i=实际利率
def debx_calac_lx(P, A, month):
    i = 0
    # 根据假设利率计算月供和实际月供进行比较，找到实际利率
    while i < 100:
        i = i + 0.0001
        # 用假设利率计算月供
        rA = debx_calac(P, i, month)
        if (int(rA) == int(A)):
            return i


# 回报计算，用来计算每月需要付出月供的情况下的总回报和每月回报 P=贷款总额，hbl=预期回报率（年），payback=每月支付月供金额，
# 【返回值：】allreback=总收益，monthback=每月收益
def huibaojisuan(P, hbl, payback):
    allreback = 0
    i = hbl / 12
    monthback = []

    while P > 0:
        sy = P * i  # 计算当月收益
        allreback = allreback + sy  # 总收益

        # P = P - payback + sy       #如果收益能够滚动成本金进行再投资，可以明显降低一些对回报率的需要
        P = P - payback  # 下月可投资本金扣除当月月供

        if P > 0:
            monthback.append((float('%.2f' % P), float('%.2f' % (sy))))
        else:
            monthback.append((0, float('%.2f' % (sy))))

    return allreback, monthback


# 计算每个月利息
def huibaojisuanLx(P, nlx, A, month):
    # Initialize total interest
    total_interest = 0
    i = nlx / 12
    for month in range(month):
        interest_payment = P * i
        principal_payment = A - interest_payment
        P -= principal_payment
        total_interest += interest_payment
        print(f'当前还款月: {month + 1}, 本月利息: {interest_payment}, 还款本金: {principal_payment}, 总还款利息: {total_interest}')


if __name__ == '__main__':
    # 贷款金额
    P = 70000
    # 银行提供的年利率
    nlx = 0.0898
    # 销售提供的每月还款额
    hke = 1452
    # 贷款月数
    month = 60

    debx = debx_calac(P=P, nlx=nlx, month=month)
    print(f'计算月供: {debx}')

    lx = debx_calac_lx(P=P, A=hke, month=month)
    print(f'实际利率: {lx}')

    huibaojisuanLx(P=P, nlx=nlx, A=hke, month=month)
