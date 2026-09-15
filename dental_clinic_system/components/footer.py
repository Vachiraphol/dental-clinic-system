import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="activity", color="var(--accent-9)", size=24),
                        rx.heading("Dental Guardian", size="5", color="var(--accent-11)"),
                        align="center",
                    ),
                    rx.text("มอบการดูแลรักษาสุขภาพช่องปากที่ดีที่สุดสำหรับครอบครัวคุณ", size="2", color="var(--slate-10)"),
                    align="start",
                    spacing="3",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.heading("ติดต่อเรา", size="4", color="var(--slate-12)"),
                    rx.text("📞 +66 2 123 4567", size="2", color="var(--slate-10)"),
                    rx.text("📧 contact@dentalguardian.com", size="2", color="var(--slate-10)"),
                    align="start",
                    spacing="2",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.heading("สถานที่ตั้ง", size="4", color="var(--slate-12)"),
                    rx.text("123 Health Ave,", size="2", color="var(--slate-10)"),
                    rx.text("Bangkok, 10110", size="2", color="var(--slate-10)"),
                    align="start",
                    spacing="2",
                ),
                direction="row",
                spacing="9",
                align="start",
                wrap="wrap",
            ),
            padding_top="8",
            padding_bottom="8",
        ),
        background_color="var(--slate-2)",
        border_top="1px solid var(--slate-4)",
        width="100%",
        margin_top="9",
    )
