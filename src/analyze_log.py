import csv


def favourite_order(orders, customer):
    # returns the most ordered item by a customer
    order_counter = {}
    favorite_item = orders[0]['order']

    for order in orders:
        if order['customer'] == customer:
            if order['order'] in order_counter:
                order_counter[order['order']] += 1
            else:
                order_counter[order['order']] = 1

            if order_counter[order['order']] > order_counter[favorite_item]:
                favorite_item = order['order']

    return favorite_item


def item_counter(orders, customer, item):
    # returns the total of a specific item ordered by a customer
    total = 0

    for order in orders:
        if order['customer'] == customer and order['order'] == item:
            total += 1

    return total


def never_ordered(menu, orders, customer):
    # returns a set with the items never ordered by a customer
    customer_items = set()

    for order in orders:
        if order['customer'] == customer:
            customer_items.add(order['order'])

    divergent_items = menu.difference(customer_items)

    return divergent_items


def week_days_unattended(week_days, orders, customer):
    # returns a set with the week days that a customer never attended
    customer_days = set()

    for order in orders:
        if order['customer'] == customer:
            customer_days.add(order['day'])

    divergent_days = week_days.difference(customer_days)

    return divergent_days


def analyze_log(path_to_file):

    orders = []
    menu = set()
    week_days = set()

    try:
        with open(path_to_file, 'r') as file:
            reader = csv.reader(file)
            for customer, order, day in reader:
                orders.append({
                    'customer': customer,
                    'order': order,
                    'day': day
                })
                menu.add(order)
                week_days.add(day)
    except FileNotFoundError:
        # if file extension isn't .csv, returns:
        # "Extensão inválida: '{nome_do_arquivo}'"
        if not path_to_file.endswith('.csv'):
            raise FileNotFoundError(f'Extensão inválida: {path_to_file}')
        # if path to file isn't valid, returns an error with the message:
        # "Arquivo inexistente: '{nome_do_arquivo}'"
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')

    # maria most ordered -> item
    maria_favorite = favourite_order(orders, 'maria')

    # arnaldo x hamburguers -> total
    arnaldo_hamburgers = item_counter(orders, 'arnaldo', 'hamburguer')

    # joao nunca pediu -> {item, item, item}
    joao_never_ordered = never_ordered(menu, orders, 'joao')

    # dias joao nunca foi -> {item, item}
    joao_never_went = week_days_unattended(week_days, orders, 'joao')

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f'{maria_favorite}\n'
            f'{arnaldo_hamburgers}\n'
            f'{joao_never_ordered}\n'
            f'{joao_never_went}\n'
        )
