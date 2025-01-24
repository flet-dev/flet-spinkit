# flet-spinkit
FletSpinkit control for Flet

Animated loading indicator based on [flutter_spinkit](https://pub.dev/packages/flutter_spinkit)

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

<img src="media/spinkit.gif" width="50%" />

## Properties

### `clip_behavior`

The `content` will be clipped (or not) according to this option.

Value is of type [`ClipBehavior`](/docs/reference/types/clipbehavior) and defaults to `ClipBehavior.NONE`.

### `color`

The card's background [color](/docs/reference/colors).

### `content`

The `Control` that should be displayed inside the card.

This control can only have one child. To lay out multiple children, let this control's child be a control such as [`Row`](/docs/controls/row), [`Column`](/docs/controls/column), or [`Stack`](/docs/controls/stack), which have a children property, and then provide the children to that control.

### `elevation`

Controls the size of the shadow below the card. Default value is `1.0`.