from pages.portfolio_page import PortfolioPage

def test_portfolio_loads(page):
    portfolio = PortfolioPage(page)
    portfolio.navigate()
    assert "Haris" in portfolio.get_hero_name() or "Muhammad" in portfolio.get_hero_name()

def test_about_section_visible(page):
    portfolio = PortfolioPage(page)
    portfolio.navigate()
    assert portfolio.is_section_visible("about")

def test_projects_section_visible(page):
    portfolio = PortfolioPage(page)
    portfolio.navigate()
    assert portfolio.is_section_visible("projects")

def test_experience_section_visible(page):
    portfolio = PortfolioPage(page)
    portfolio.navigate()
    assert portfolio.is_section_visible("experience")

def test_contact_section_visible(page):
    portfolio = PortfolioPage(page)
    portfolio.navigate()
    assert portfolio.is_section_visible("contact")

def test_language_switch_to_german(page):
    portfolio = PortfolioPage(page)
    portfolio.navigate()
    page.get_by_role("button", name="DE").click()
    assert page.get_by_role("button", name="EN").is_visible()

def test_page_title(page):
    portfolio = PortfolioPage(page)
    portfolio.navigate()
    title = portfolio.get_title()
    assert title != ""