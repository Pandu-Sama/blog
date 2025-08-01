# Mini-Blog Django
 Un blog simple con Django que permite listar y ver detalles de publicaciones.
 
## Instalaciòn 
1. Clona el repositorio: 'git clone https://github.com/Pandu-Sama/blog.git'
2. Crea un entorno virtual: 'python -m venv django'
3. Activa el entorno: 'source djangoenv/bin/activate'
4. Instala Django: 'pip install django=5.2.4'
5. Aplica migraciones: 'python manage.py migrate'
6. Crea un superusuario: 'python manage.py createsuperuser'
7. Inicia el servidor: 'python manage.py runserver'

## Uso
- Admin: '/admin/'
- Lista de posts: '/posts/'
- Detalle de post: '/posts/<id>/'