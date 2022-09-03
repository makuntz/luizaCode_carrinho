# focar em um usuario
# varios produtos (codigos diferentes)
# diferentes quantidades de produtos (posso querer mais de um produto)


cart = []

id_user = input("Insira o id do usuário: ")
id_product = input("Insira o id do produto: ")
price_product = float(input("Insira o preço do produto: "))
quantity_product = int(input("Insira a quantidade de produtos: "))

item = [id_user, id_product, price_product, quantity_product]


def add_item_cart():
    cart.append(item)
    return cart
add_item_cart()


def get_all_items_cart():
    #return todos os itens do carrinho2
    print(cart)
    return cart
get_all_items_cart()
    

new_lista = []
def get_item_cart_by_id(id_product):
    #retornar o item inteiro, onde o produto tiver o id desejado
    for i in cart:
        if i[1] == id_product:
            new_lista.append(i)
            print(new_lista)            
get_item_cart_by_id('546')
    

# exemplo lista de compreensao
# newlist = [item for item in cart if item[0] == '123']



def remove_item_id(id_product):
    #remover o item do carrinho que tem esse produto
    for i in cart:
        if i[1] == id_product:
            cart.clear()
            print(cart)
remove_item_id('546')