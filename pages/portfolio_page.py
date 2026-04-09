class PortfolioPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://haris-noonari.vercel.app"
    def navigate(self):
        self.page.goto(self.url)

    def get_title(self):
        return self.page.title()

    def get_hero_name(self):
        return self.page.locator("h1").first.text_content()

    def click_nav(self, section):
        self.page.get_by_text(section, exact=True).first.click()

    def is_section_visible(self, section_id):
        return self.page.locator(f"#{section_id}").is_visible()

    def click_github(self):
        self.page.get_by_text("GitHub").first.click()

    def get_projects_count(self):
        return self.page.locator(".project-card").count()

    def switch_language(self, lang):
        self.page.get_by_text(lang, exact=True).click()