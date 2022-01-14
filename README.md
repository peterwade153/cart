# Cart Backend

REST API built with Django/Django Rest Framework. API uses Celery and Redis as celery Broker for asynchrous tasks.

### Installation

1. Create and activate a virtual environment and Clone the project `https://github.com/peterwade153/cart.git`

2. Move into the project folder
   ```
   $ cd cart
   ```

3. Install dependencies 
   ```
   $ pip install -r requirements.txt
   ```

4. Create a `.env` file using the keys in the `.env.sample` file, and replace the values with actual values.

5. Run migrations
   ```
   python manage.py migrate
   ```
   