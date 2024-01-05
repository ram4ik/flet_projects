import flet as ft

def main(page: ft.Page):
    page.title = "Favorite Fruits"

    page.add(
        ft.Row(controls=[ft.Text("My Favorite Fruits:\n")]),
        ft.Row(
            controls=[
                ft.Text("Apple"),
                ft.Text("Mango"),
                ft.Text("Guava"),
            ]
        ),
        ft.Column(controls=[ft.Text("My Favorite Vegetables:\n")]),
        ft.Column(
            controls=[
                ft.Text("Potato"),
                ft.Text("Tomato"),
                ft.Text("Carrot"),
            ]
        )
    )

ft.app(target=main)
