import csv


def analyze_log(path_to_file):

    orders = []
    menu = set()
    week_days = set()

    # maria most ordered -> item
    # arnaldo x hamburguers -> total
    # joao nunca pediu -> {item, item, item}
    # dias joao nunca foi -> {item, item}
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
    