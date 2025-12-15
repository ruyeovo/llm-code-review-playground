def process(value):
    if value == None:        # ❌ 风格问题
        return 0

    if value > 0:
        return 100 / value  # ❌ 潜在 ZeroDivision
    else:
        return 1
