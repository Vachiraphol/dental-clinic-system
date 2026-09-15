import reflex as rx
from dental_clinic_system.components import header, footer

def social_login_button(provider: str, icon_tag: str) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.icon(tag=icon_tag, size=20),
            rx.text(f"ดำเนินการต่อด้วย {provider}", weight="medium"),
            spacing="2",
            align="center",
        ),
        variant="outline",
        size="3",
        width="100%",
        color_scheme="gray",
        radius="large",
        margin_bottom="3",
    )

def login_form() -> rx.Component:
    return rx.vstack(
        rx.text("ยินดีต้อนรับกลับมา! กรุณากรอกข้อมูลของคุณ", size="2", color="var(--slate-10)", margin_bottom="4"),
        
        rx.vstack(
            rx.text("อีเมล", size="2", weight="medium"),
            rx.input(placeholder="กรอกอีเมลของคุณ", type="email", width="100%", size="3"),
            spacing="1",
            width="100%",
            margin_bottom="3",
        ),
        
        rx.vstack(
            rx.text("รหัสผ่าน", size="2", weight="medium"),
            rx.input(placeholder="••••••••", type="password", width="100%", size="3"),
            spacing="1",
            width="100%",
            margin_bottom="4",
        ),
        
        rx.button("เข้าสู่ระบบ", size="3", width="100%", color_scheme="purple", radius="large", margin_bottom="4"),
        
        rx.hstack(
            rx.divider(width="100%"),
            rx.text("หรือ", size="1", color="var(--slate-9)", white_space="nowrap"),
            rx.divider(width="100%"),
            align="center",
            width="100%",
            spacing="3",
            margin_bottom="4",
        ),
        
        social_login_button("Google", "chrome"),
        social_login_button("Facebook", "facebook"),
        social_login_button("Apple", "apple"),
        
        width="100%",
        align="start",
    )

def signup_form() -> rx.Component:
    return rx.vstack(
        rx.text("สร้างบัญชีเพื่อจัดการการนัดหมายของคุณ", size="2", color="var(--slate-10)", margin_bottom="4"),
        
        rx.hstack(
            rx.vstack(
                rx.text("ชื่อ", size="2", weight="medium"),
                rx.input(placeholder="สมชาย", width="100%", size="3"),
                spacing="1",
                width="100%",
            ),
            rx.vstack(
                rx.text("นามสกุล", size="2", weight="medium"),
                rx.input(placeholder="ใจดี", width="100%", size="3"),
                spacing="1",
                width="100%",
            ),
            spacing="4",
            width="100%",
            margin_bottom="3",
        ),
        
        rx.vstack(
            rx.text("วันเกิด", size="2", weight="medium"),
            rx.input(type="date", width="100%", size="3"),
            spacing="1",
            width="100%",
            margin_bottom="3",
        ),

        rx.vstack(
            rx.text("อีเมล", size="2", weight="medium"),
            rx.input(placeholder="กรอกอีเมลของคุณ", type="email", width="100%", size="3"),
            spacing="1",
            width="100%",
            margin_bottom="3",
        ),
        
        rx.vstack(
            rx.text("รหัสผ่าน", size="2", weight="medium"),
            rx.input(placeholder="ตั้งรหัสผ่าน", type="password", width="100%", size="3"),
            spacing="1",
            width="100%",
            margin_bottom="5",
        ),
        
        rx.button("สร้างบัญชีผู้ใช้", size="3", width="100%", color_scheme="purple", radius="large"),
        
        width="100%",
        align="start",
    )

@rx.page(route="/auth", title="Dental Guardian - เข้าสู่ระบบ/สมัครสมาชิก")
def auth() -> rx.Component:
    return rx.box(
        header(),
        
        rx.center(
            rx.card(
                rx.vstack(
                    rx.center(
                        rx.icon(tag="activity", color="var(--accent-9)", size=40),
                        margin_bottom="4",
                        width="100%",
                    ),
                    rx.heading("Dental Guardian", size="7", align="center", width="100%", margin_bottom="6"),
                    
                    rx.tabs.root(
                        rx.tabs.list(
                            rx.tabs.trigger("เข้าสู่ระบบ", value="login", width="50%"),
                            rx.tabs.trigger("สมัครสมาชิก", value="signup", width="50%"),
                            width="100%",
                            margin_bottom="4",
                        ),
                        rx.tabs.content(
                            login_form(),
                            value="login",
                            width="100%",
                        ),
                        rx.tabs.content(
                            signup_form(),
                            value="signup",
                            width="100%",
                        ),
                        default_value="login",
                        width="100%",
                    ),
                    width="100%",
                    padding_x="6",
                    padding_y="4",
                ),
                width="450px",
                padding="6",
                box_shadow="lg",
                margin_top="12",
                margin_bottom="12",
            ),
            width="100%",
            min_height="calc(100vh - 150px)", # subtract header roughly
            background="linear-gradient(135deg, var(--purple-2) 0%, white 100%)",
        ),
        
        footer(),
        background_color="var(--slate-1)",
    )
