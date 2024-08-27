from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.SudokuManager.as_view(), name="create_new_sudoku"),
]
