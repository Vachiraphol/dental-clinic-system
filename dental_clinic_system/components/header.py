import reflex as rx

def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo / Home Link
            rx.link(
                rx.hstack(
                    rx.center(
                        rx.icon(tag="shield_plus", color="white", size=20),
                        background="linear-gradient(135deg, var(--purple-9) 0%, var(--plum-9) 100%)",
                        border_radius="xl",
                        padding="2",
                        box_shadow="0px 4px 10px rgba(142, 78, 208, 0.3)",
                    ),
                    rx.heading(
                        "Dental Guardian", 
                        size="6", 
                        weight="bold", 
                        color="var(--slate-12)",
                        letter_spacing="-0.02em",
                    ),
                    align="center",
                    spacing="3",
                    transition="transform 0.2s ease",
                    _hover={"transform": "scale(1.02)"},
                ),
                href="/",
                underline="none",
            ),
            rx.spacer(),
            # Navigation Links
            rx.hstack(
                rx.link(
                    "ประวัติการรักษา",
                    href="/history",
                    size="3",
                    weight="medium",
                    color="var(--slate-11)",
                    padding_x="4",
                    padding_y="2",
                    border_radius="full",
                    transition="all 0.2s ease",
                    _hover={"background_color": "var(--purple-3)", "color": "var(--purple-11)"},
                    underline="none",
                ),
                rx.link(
                    rx.button(
                        "เข้าสู่ระบบ",
                        variant="solid",
                        color_scheme="purple",
                        size="3",
                        radius="full",
                        weight="bold",
                        box_shadow="0px 4px 12px rgba(142, 78, 208, 0.25)",
                        transition="all 0.2s ease",
                        _hover={"transform": "translateY(-1px)", "box_shadow": "0px 6px 16px rgba(142, 78, 208, 0.35)"},
                    ),
                    href="/auth",
                ),
                rx.avatar(
                    fallback="US", 
                    color_scheme="purple", 
                    size="3", 
                    radius="full",
                    box_shadow="0px 2px 8px rgba(0,0,0,0.08)",
                ),
                align="center",
                spacing="4",
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            align="center",
            padding_x="6",
            padding_y="3",
        ),
        box_shadow="0px 4px 20px rgba(0, 0, 0, 0.03)",
        background_color="rgba(255, 255, 255, 0.85)",
        backdrop_filter="blur(12px)",
        border_bottom="1px solid var(--slate-3)",
        position="sticky",
        top="0",
        z_index="50",
        width="100%",
    )
