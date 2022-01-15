# Cart Backend

REST API built with Django/Django Rest Framework. API uses Celery and Redis as celery Broker for asynchrous tasks.
Backed uses SQLITE Database for datastorage.

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

6. Start Server
   ```
   python manage.py runserver
   ```

7. Access API endpoints via swagger docs at
   http://localhost:8000/

8. To run Tests
   ```
   python manage.py test
   ```