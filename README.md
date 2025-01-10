# E-commerce API Development

This README file documents the step-by-step process of developing and deploying an E-commerce Product API. The project includes CRUD operations for products and users, a search functionality, and deployment to PythonAnywhere.

---

## **1. Project Initialization**

### **1.1. Environment Setup**
- **Install Python**: Ensure Python (>=3.8) is installed.
- **Install Django**: Use the following command:
  ```bash
  pip install django
  ```
- **Create Django Project**:
  ```bash
  django-admin startproject ecommerce_api
  ```
- **Navigate to the Project Directory**:
  ```bash
  cd ecommerce_api
  ```

### **1.2. Create an App**
- Create a new app for products:
  ```bash
  python manage.py startapp products
  ```
- Add `products` to `INSTALLED_APPS` in `settings.py`.

---

## **2. Database Design**

### **2.1. Create Models**
- Define the `Product` model in `products/models.py`:
  ```python
  from django.db import models

  class Product(models.Model):
      name = models.CharField(max_length=100)
      description = models.TextField()
      price = models.DecimalField(max_digits=10, decimal_places=2)
      category = models.CharField(max_length=50)
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.name
  ```

### **2.2. Apply Migrations**
- Run migrations to apply the model to the database:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

## **3. Building CRUD Operations**

### **3.1. Views**
- Implement views for Create, Read, Update, and Delete operations in `products/views.py`:
  ```python
  from django.shortcuts import get_object_or_404
  from django.http import JsonResponse
  from .models import Product
  from django.views import View

  class ProductCreateView(View):
      def post(self, request):
          data = request.POST
          product = Product.objects.create(
              name=data.get('name'),
              description=data.get('description'),
              price=data.get('price'),
              category=data.get('category')
          )
          return JsonResponse({'message': 'Product created', 'id': product.id})

  class ProductListView(View):
      def get(self, request):
          products = Product.objects.all().values()
          return JsonResponse(list(products), safe=False)

  class ProductUpdateView(View):
      def post(self, request, pk):
          product = get_object_or_404(Product, pk=pk)
          data = request.POST
          product.name = data.get('name', product.name)
          product.description = data.get('description', product.description)
          product.price = data.get('price', product.price)
          product.category = data.get('category', product.category)
          product.save()
          return JsonResponse({'message': 'Product updated'})

  class ProductDeleteView(View):
      def post(self, request, pk):
          product = get_object_or_404(Product, pk=pk)
          product.delete()
          return JsonResponse({'message': 'Product deleted'})
  ```

### **3.2. URLs**
- Configure URLs in `products/urls.py`:
  ```python
  from django.urls import path
  from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

  urlpatterns = [
      path('', ProductListView.as_view(), name='product-list'),
      path('create/', ProductCreateView.as_view(), name='product-create'),
      path('update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
      path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
  ]
  ```

- Include the app's URLs in the project `urls.py`:
  ```python
  from django.urls import path, include

  urlpatterns = [
      path('products/', include('products.urls')),
  ]
  ```

---

## **4. Deployment**

### **4.1. Prepare for Deployment**
- Install `gunicorn` and other dependencies:
  ```bash
  pip install gunicorn
  ```
- Create a `requirements.txt` file:
  ```bash
  pip freeze > requirements.txt
  ```

### **4.2. Configure Settings**
- Update `settings.py`:
  - Set `DEBUG = False`.
  - Add the deployment domain to `ALLOWED_HOSTS`:
    ```python
    ALLOWED_HOSTS = ['your-pythonanywhere-domain.pythonanywhere.com']
    ```

### **4.3. Deploy to PythonAnywhere**
1. **Upload Files**:
   - Upload the project files to PythonAnywhere.

2. **Create Virtual Environment**:
   ```bash
   mkvirtualenv myenv --python=python3
   pip install -r requirements.txt
   ```

3. **Configure Web App**:
   - Point the WSGI configuration file to the project.

4. **Test the App**:
   - Navigate to the domain and test the endpoints.

---

## **5. Challenges and Solutions**

### **5.1. Deployment Errors**
- **Issue**: "Unhandled Exception" during deployment.
- **Solution**: Verified virtual environment setup, corrected `wsgi.py` and `settings.py` configuration.

### **5.2. Dependency Management**
- Used `requirements.txt` to ensure consistent environment setup.

---

## **6. Next Steps**
- Enhance functionality with user authentication.
- Add more test cases.
- Explore alternative deployment platforms.

---

## **7. Acknowledgments**
This project was a learning experience, providing insights into web development and deployment practices. Special thanks to the development and debugging tools that assisted throughout the project.

---

