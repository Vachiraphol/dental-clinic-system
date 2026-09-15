import reflex as rx
from dental_clinic_system.components import header, footer

def service_card(image_url: str, title: str) -> rx.Component:
    return rx.box(
        rx.image(src=image_url, height="150px", width="250px", object_fit="cover", border_radius="lg"),
        rx.center(
            rx.text(title, weight="bold", size="3", color="var(--slate-12)", margin_top="2"),
        ),
        padding="2",
        border_radius="xl",
        background_color="white",
        box_shadow="sm",
        margin_x="2",
        min_width="260px",
        flex_shrink="0",
        transition="transform 0.2s",
        _hover={"transform": "scale(1.05)"},
    )

@rx.page(route="/", title="Dental Guardian - หน้าแรก")
def home() -> rx.Component:
    return rx.box(
        header(),
        
        # Hero Section
        rx.box(
            rx.container(
                rx.flex(
                    rx.vstack(
                        rx.heading(
                            "รอยยิ้มสวยเริ่มต้นที่นี่",
                            size="9",
                            weight="bold",
                            color="var(--slate-12)",
                            line_height="1.1",
                        ),
                        rx.text(
                            "สัมผัสประสบการณ์การดูแลสุขภาพช่องปากระดับโลกกับทีมผู้เชี่ยวชาญของเรา พร้อมเทคโนโลยีที่ทันสมัยเพื่อรอยยิ้มที่สดใสและสุขภาพดีของคุณ",
                            size="4",
                            color="var(--slate-11)",
                            margin_top="4",
                            margin_bottom="6",
                        ),
                        rx.hstack(
                            rx.button("นัดหมายล่วงหน้า", size="4", color_scheme="purple", radius="full"),
                            rx.button("บริการของเรา", size="4", variant="soft", color_scheme="purple", radius="full"),
                            spacing="4",
                        ),

                        align="start",
                        justify="center",
                        height="100%",
                        padding_right="8",
                    ),
                    rx.box(
                        rx.image(
                            src="https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&q=80&w=800",
                            border_radius="xl",
                            box_shadow="xl",
                        ),
                        width="100%",
                        display="block",
                    ),
                    direction="row",
                    spacing="9",
                    padding_y="9",
                    align="center",
                ),
            ),
            background="linear-gradient(to bottom right, var(--purple-2), var(--slate-1))",
            padding_top="12",
            padding_bottom="12",
        ),

        # Services Section
        rx.container(
            rx.center(
                rx.hstack(
                    rx.icon(
                        tag="chevron_left", 
                        size=40, 
                        color="var(--slate-9)", 
                        cursor="pointer", 
                        _hover={"color": "var(--slate-12)"},
                        on_click=rx.call_script("document.getElementById('services-scroll').scrollBy({left: -300, behavior: 'smooth'})"),
                        flex_shrink="0",
                    ),
                    
                    rx.hstack(
                        service_card("https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&q=80&w=400", "ตรวจสุขภาพ & เอกซเรย์"),
                        service_card("https://images.unsplash.com/photo-1598331668826-20cefac91461?auto=format&fit=crop&q=80&w=400", "ขูดหินปูน & ขัดฟัน"),
                        service_card("https://images.unsplash.com/photo-1599422314077-f4dfdaa4cd09?auto=format&fit=crop&q=80&w=400", "อุดฟัน & ถอนฟัน"),
                        service_card("https://images.unsplash.com/photo-1551076805-e1869043e560?auto=format&fit=crop&q=80&w=400", "รักษารากฟัน"),
                        service_card("https://images.unsplash.com/photo-1598331668826-20cefac91461?auto=format&fit=crop&q=80&w=400", "จัดฟัน & Invisalign"),
                        service_card("https://images.unsplash.com/photo-1599422314077-f4dfdaa4cd09?auto=format&fit=crop&q=80&w=400", "รากฟันเทียม & ฟันปลอม"),
                        service_card("https://images.unsplash.com/photo-1583324113626-70df0f4deaab?auto=format&fit=crop&q=80&w=400", "ผ่าฟันคุด & ศัลยกรรม"),
                        service_card("https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&q=80&w=400", "รักษาโรคเหงือก"),
                        service_card("https://images.unsplash.com/photo-1598331668826-20cefac91461?auto=format&fit=crop&q=80&w=400", "ทันตกรรมสำหรับเด็ก"),
                        service_card("https://images.unsplash.com/photo-1599422314077-f4dfdaa4cd09?auto=format&fit=crop&q=80&w=400", "ฟอกสีฟัน & วีเนียร์"),
                        id="services-scroll",
                        overflow_x="auto",
                        padding_y="4",
                        spacing="4",
                        width="100%",
                        style={"&::-webkit-scrollbar": {"display": "none"}, "scroll_behavior": "smooth"},
                    ),
                    
                    rx.icon(
                        tag="chevron_right", 
                        size=40, 
                        color="var(--slate-9)", 
                        cursor="pointer", 
                        _hover={"color": "var(--slate-12)"},
                        on_click=rx.call_script("document.getElementById('services-scroll').scrollBy({left: 300, behavior: 'smooth'})"),
                        flex_shrink="0",
                    ),
                    width="100%",
                    justify="center",
                    align="center",
                    spacing="6",
                ),
                width="100%",
                padding_top="8",
                padding_bottom="12",
                background_color="#F2EFE8", # Beige background from the image
            ),
        ),
        
        footer(),
        background_color="var(--slate-1)",
        min_height="100vh",
    )
