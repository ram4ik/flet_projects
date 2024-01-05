import flet as ft

def main(page: ft.Page):
    page.title = "Hello World"

    text = ft.Text(value="My First Flet App", color="green")
    page.controls.append(text)
    page.update()

# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)
