# shopping-cart-backend
The API written in django using djangorestframework. 

## The API includes:

### Products:
Product has a name, description, price, archive and image.
- API:
  - Get all products.
  - Add a product.
  - Get a single product.
  - Delete (archive) a product.
  - Update a product.
  - Search by name.

### Cart:
Cart has a name.
- API:
  - Get a cart.

### CartItem:
Cart item has a cart, product, quantity and paid status.
- API:
  - Get all CartItems.
  - Create a CartItem.
  - Get a single CartItem.
  - Add a CartItem.
  - Delete a CartItem.
  - Update a CartItem.

### Order:
Order has products, cart and total price.
- API:
  - Get an Order by cart ID.
  - Create an order.

## Coming soon:
- Authentication (react + django). 
