
# Vendor Management System




## Installation

## create virtual env using

python -m venv env

# activate virtual env 

env_name/Scripts/activate

# deactivate virtual env

deactivate

# Install django and djangorestframework

pip install django

pip install djangorestframework

# Install simplejwt package

pip install djangorestframework-simplejwt

## create django project

django-admin startproject project_name

# create django app

python manage.py startapp app_name



    
## API Reference

## JWT Endpoints
#### Generate access token and refresh token

```http
  POST /http://127.0.0.1:8000/api/both_tokens/
```

#### Regenerate access token from refresh token

```http
  POST /http://127.0.0.1:8000/api/new_token/
```

## API Endpoints

#### Get all vendors

```http
  GET /http://127.0.0.1:8000/api/vendors/
```

#### Get vendor

```http
  GET /http://127.0.0.1:8000/api/vendors/id/
```

#### add vendor

 ```http
  POST /http://127.0.0.1:8000/api/vendors/
```

#### Update vendor

 ```http
  PUT /http://127.0.0.1:8000/api/vendors/id/
```

#### Delete vendor

 ```http
  DELETE /http://127.0.0.1:8000/api/vendors/id/
```

#### Get all Purchase Orders

```http
  GET /http://127.0.0.1:8000/api/purchase_orders/
```

#### Get Purchase Order

```http
  GET /http://127.0.0.1:8000/api/purchase_orders/id/
```

#### add Purchase Order

 ```http
  POST /http://127.0.0.1:8000/api/purchase_orders/
```

#### Update Purchase Order

 ```http
  PUT /http://127.0.0.1:8000/api/purchase_orders/id/
```

#### Delete Purchase Order

 ```http
  DELETE /http://127.0.0.1:8000/api/purchase_orders/id/
```

#### Get vendor performance matrix

```http
  GET /http://127.0.0.1:8000/api/vendors/id/performance/
```