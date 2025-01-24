# flet-spinkit

FletSpinkit control for Flet.

Animated loading indicator based on [flutter_spinkit](https://pub.dev/packages/flutter_spinkit).

## Examples

```python
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

```

<img src="media/spinkit.gif" width="20%" />

## Properties

### `color`

The color of the indicator.

### `size`

The size of the indicator in virtual pixels. The default is 100.