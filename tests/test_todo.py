import pytest
from pages.todo_page import TodoPage

def test_add_single_todo(page):
    todo = TodoPage(page)
    todo.navigate()
    todo.add_todo("Buy groceries")
    assert todo.get_todo_count() == 1

def test_add_multiple_todos(page):
    todo = TodoPage(page)
    todo.navigate()
    todo.add_todo("Buy groceries")
    todo.add_todo("Walk the dog")
    todo.add_todo("Read a book")
    assert todo.get_todo_count() == 3

def test_complete_todo(page):
    todo = TodoPage(page)
    todo.navigate()
    todo.add_todo("Buy groceries")
    todo.complete_todo(0)
    assert todo.get_completed_count() == 1

def test_clear_completed(page):
    todo = TodoPage(page)
    todo.navigate()
    todo.add_todo("Buy groceries")
    todo.add_todo("Walk the dog")
    todo.complete_todo(0)
    todo.clear_completed()
    assert todo.get_todo_count() == 1