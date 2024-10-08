class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        existing_products = self.get_products().strip().split('\n')

        for product in products:

            if product.name in [p.split(',')[0] for p in existing_products]:
                print(f'Продукт {product.name} уже есть в магазине')
            else:

                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')



if __name__ == '__main__':
    shop = Shop()
    potato = Product('Potato', 50.0, 'Vegetables')
    carrot = Product('Carrot', 30.0, 'Vegetables')

    shop.add(potato)
    shop.add(carrot)
    shop.add(potato)
    print(shop.get_products())

