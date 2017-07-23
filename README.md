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

* _/auth/signup/_ -> To register new user

* _/auth/login/_ -> To login existig user

* _/order/create/_ -> To create new order for authenticated user

* _/order/validate/token/_ -> To approve created order

* _/order/order_id/_ -> To get detail of specific order of authenticated user only

* _/order/?page=n_ -> To get all orders of authenticated user only with pagination

* _/orderitem/create/_ -> To create item according to order for authenticated user

* _/orderitem/order_id/?page=n_ -> To get all order items of specific order of authenticated user only with pagination
