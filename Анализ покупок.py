def read_sales():
    try:
        with open('sales.txt','r',encoding='utf-8')as file:
            for line in file.readlines():
                print(line.strip())
    except FileNotFoundError:
        print("Файл не найден")


def parse_sales():
    sales = []
    try:
        with open('sales.txt','r',encoding='utf-8')as file:
            for line in file.readlines():
                line_new = line.strip().split("|")
                tovar,categor,price,count = line_new
                one_sale = {'категория':categor,'товар':tovar,'цена':int(price),'количество':int(count)}
                sales.append(one_sale)
        return sales
    except FileNotFoundError:
        print("Файл не найден")
        return []

def total_revenue(sales):
    total = 0
    for line in sales:
        total += line.get('цена')*line.get('количество')
    print(total)


def top_products():
    product_count = {}
    for line in sales_data:
        product = line.get('товар')
        count = line.get('количество')
        if product not in product_count:
            product_count [product] = count
        else:
            product_count[product] += count
    print(product_count)

    items = product_count.items()
    sorted_items = sorted(items, key=lambda x:x[1],reverse=True)
    for i,j  in sorted_items[:3]:
        print(f"{i} - {j} шт.")

sales_data= parse_sales()
top_products()
