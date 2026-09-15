import reflex as rx

config = rx.Config(
    app_name="dental_clinic_system",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="light",
                has_background=True,
                radius="large",
                accent_color="purple",
                gray_color="slate",
            )
        ),
    ]
)