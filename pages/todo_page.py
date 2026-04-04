class TodoPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://demo.playwright.dev/todomvc"
        self.input_box = page.locator(".new-todo")
        self.todo_items = page.locator(".todo-list li")

    def navigate(self):
        self.page.goto(self.url)

    def add_todo(self, text):
        self.input_box.fill(text)
        self.input_box.press("Enter")

    def get_todo_count(self):
        return self.todo_items.count()

    def complete_todo(self, index):
        self.todo_items.nth(index).locator(".toggle").click()

    def get_completed_count(self):
        return self.page.locator(".todo-list li.completed").count()

    def clear_completed(self):
        self.page.locator(".clear-completed").click()