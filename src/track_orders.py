class TrackOrders:
    # aqui deve expor a quantidade de estoque

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({
            'customer': customer,
            'order': order,
            'day': day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        counter = {}
        favorite_item = self.orders[0]['order']

        for order in self.orders:
            if order['customer'] == customer:
                if order['order'] in counter:
                    counter[order['order']] += 1
                else:
                    counter[order['order']] = 1

                if counter[order['order']] > counter[favorite_item]:
                    favorite_item = order['order']

        return favorite_item

    def get_never_ordered_per_customer(self, customer):
        ordered_items = set()
        customer_orders = set()

        for order in self.orders:
            if order['customer'] == customer:
                customer_orders.add(order['order'])
            ordered_items.add(order['order'])

        divergent_items = ordered_items.difference(customer_orders)

        return divergent_items

    def get_days_never_visited_per_customer(self, customer):
        customer_days = set()
        week_days = set()

        for order in self.orders:
            if order['customer'] == customer:
                customer_days.add(order['day'])
            week_days.add(order['day'])

        divergent_days = week_days.difference(customer_days)

        return divergent_days

    def get_busiest_day(self):
        counter = {}
        busiest_day = self.orders[0]['day']

        for order in self.orders:
            if order['day'] in counter:
                counter[order['day']] += 1
            else:
                counter[order['day']] = 1

            if counter[order['day']] > counter[busiest_day]:
                busiest_day = order['day']

        return busiest_day

    def get_least_busy_day(self):
        counter = {}
        least_busy_day = self.orders[0]['day']

        for order in self.orders:
            if order['day'] in counter:
                counter[order['day']] += 1
            else:
                counter[order['day']] = 1

            if counter[order['day']] < counter[least_busy_day]:
                least_busy_day = order['day']

        return least_busy_day
