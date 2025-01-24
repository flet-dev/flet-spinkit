import flet as ft

from flet_spinkit import FletSpinkit


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Stack(
            [
                ft.Container(height=200, width=200, bgcolor=ft.Colors.BLUE_100),
                FletSpinkit(
                    opacity=0.5,
                    tooltip="Spinkit tooltip",
                    top=0,
                    left=0,
                    color=ft.Colors.YELLOW,
                    size=150,
                ),
            ]
        )
    )


ft.app(main)
