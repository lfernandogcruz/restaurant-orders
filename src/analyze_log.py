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
    # dias joao nunca foi -> {item, item}
