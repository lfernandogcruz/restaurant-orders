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
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
