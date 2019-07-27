# 因为每种商品的颜色、尺寸描述上有差异，为了方面统计，我们进行了简单的数据清洗。
def flush_data(data):
    if '肤' in data:
        return '肤色'
    if '黑' in data:
        return '黑色'
    if '紫' in data:
        return '紫色'
    if '粉' in data:
        return '粉色'
    if '蓝' in data:
        return '蓝色'
    if '白' in data:
        return '白色'
    if '灰' in data:
        return '灰色'
    if '槟' in data:
        return '香槟色'
    if '琥' in data:
        return '琥珀色'
    if '红' in data:
        return '红色'
    if '紫' in data:
        return '紫色'
    if 'A' in data:
        return 'A'
    if 'B' in data:
        return 'B'
    if 'C' in data:
        return 'C'
    if 'D' in data:
        return 'D'