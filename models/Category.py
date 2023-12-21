class Category:
    """
    Класс, представляющий категорию продуктов.
    """
    name_category: str
    """Название категории."""

    description_category: str
    """Описание категории."""

    products: list
    """Список продуктов в категории."""

    total_categories = 0
    """Общее количество категорий."""

    total_unique_products = 0
    """Общее количество уникальных продуктов."""

    def __init__(self, name_category: str, description_category: str) -> None:
        """
        Инициализация объекта класса Category.
        :param name_category: Название категории.
        :param description_category: Описание категории.
        """
        self.name_category = name_category
        self.description_category = description_category
        self.products = []
        Category.total_categories += 1
