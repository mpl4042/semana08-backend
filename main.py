#No Monólito: O sistema tem acesso direto aos dados.
class EcommerceSystem:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def place_order(self, user, product):
        if product in self.products:
            self.orders.append((user, product))
            return "Order placed successfully"
        
        return "Product not available"

# Exemplo de uso
system = EcommerceSystem()
system.add_user("Alice")
system.add_product("Laptop")
print(system.place_order("Alice", "Laptop"))


#separar as responsabilidades, Imagine que cada classe dessas
#  poderia estar em um servidor diferente no futuro. 
# Para o código funcionar, precisamos garantir que o OrderService 
# consiga "conversar" com o ProductService.
#Passo 2: Refatoração para microsserviços
class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class ProductService:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def check_availability(self, product):
        # Este método simula uma consulta ao estoque
        return product in self.products


class OrderService:
    def __init__(self):
        self.orders = []

    def place_order(self, user, product, product_service):
        # O serviço de pedidos "pergunta" ao serviço de produtos se há estoque
        if product_service.check_availability(product):
            self.orders.append({"user": user, "product": product})
            return "Order placed successfully (Microservice Mode)"
        
        return "Product not available"


# --- Simulação do Sistema Rodando ---

# 1. Instanciamos os serviços separadamente
user_service = UserService()
product_service = ProductService()
order_service = OrderService()

# 2. Alimentamos os serviços com dados
user_service.add_user("Alice")
product_service.add_product("Laptop")

# 3. O OrderService realiza o pedido usando a dependência do ProductService
resultado = order_service.place_order("Alice", "Laptop", product_service)

print(resultado)
#o código está organizado de uma forma que, se o sistema de Produtos cair ou
#precisar de manutenção, o sistema de Usuários continua intacto.