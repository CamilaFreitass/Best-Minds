from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastrar_produto', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('deletar_produto/<int:id>', views.deletar_produto, name='deletar_produto'),
]