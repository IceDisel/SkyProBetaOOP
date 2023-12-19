class Category:
    name_category: str
    description_category: str
    products: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name_category, description_category):
        self.name_category = name_category
        self.description_category = description_category
        self.products = []
        Category.total_categories += 1
