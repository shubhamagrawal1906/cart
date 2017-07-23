# Cart

## Description :-

It is a cart system api that involve the creation and retrieval of order and its order items.
It is developed using django rest framework and for the authentication token based scheme is used.
To authenticate user, you have to add token with headers in each api you call, that is retrieved from login.

Add it in header as given below -

__Authorization: _Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b___

User need to __approved__ after order any item.
The link has been sent to __registered email__ of user.
Click that __link__ to __approve__ your order.

## Requiements are provided in requirements.txt :-

_Django==1.11.3_

_django-filter==1.0.4_

_djangorestframework==3.6.3_

_Markdown==2.6.8_

_pytz==2017.2_

## Urls are :-

/auth/signup/ -> To register new user

/auth/login/ -> To login existig user

/order/create/ -> To create new order for authenticated user

/order/validate/token/ -> To approve created order

/order/order_id/ -> To get detail of specific order of authenticated user only

/order/?page=n -> To get all orders of authenticated user only with pagination

/orderitem/create/ -> To create item according to order for authenticated user

/orderitem/order_id/?page=n -> To get all order items of specific order of authenticated user only with pagination
