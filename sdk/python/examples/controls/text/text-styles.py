import flet
from flet import ListView, Page, Text


def main(page: Page):
    page.title = "Text Examples"
    page.padding = 50
    page.spacing = 10
    page.scroll = "adaptive"

    page.add(
        Text("Display Large", style="displayLarge"),
        Text("Display Medium", style="displayMedium"),
        Text("Display Small", style="displaySmall"),
        Text("Headline Large", style="headlineLarge"),
        Text("Headline Medium", style="headlineMedium"),
        Text(
            "Headline Small",
            size=40,
            color="onPrimary",
            bgcolor="primary",
        ),
        Text("Title Large", style="titleLarge"),
        Text("Title Medium", style="titleMedium"),
        Text("Title Small", style="titleSmall"),
        Text("Label Large", style="labelLarge"),
        Text("Label Medium", style="labelMedium"),
        Text("Label Small", style="labelSmall"),
        Text("Body Large", style="bodylLarge"),
        Text("Body Medium", style="bodyMedium"),
        Text("Body Small", style="bodySmall"),
        Text("Size 10", size=10),
        Text("Size 30, Italic", size=20, color="pink600", italic=True),
        Text(
            "Size 40, w100",
            size=40,
            color="white",
            bgcolor="blue600",
            weight="w100",
        ),
        Text(
            "Size 50, Normal",
            size=50,
            color="white",
            bgcolor="orange800",
            weight="normal",
        ),
        Text(
            "Size 60, Bold",
            size=50,
            color="white",
            bgcolor="green700",
            weight="bold",
        ),
        Text("Size 70, w900", size=70, weight="w900", selectable=True),
    )


flet.app(target=main, view=flet.WEB_BROWSER)
