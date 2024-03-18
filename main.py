import streamlit as st
import streamlit.components.v1 as components

Col1, Col2, Col3 = st.columns(3)

Col2.image('https://i.imgur.com/YMei8p1.png', use_column_width='auto')

st.title("Color Palette Tester")

st.link_button("Color Palettes", "https://colorhunt.co/")

with st.form("ColorForm"):

    color_code1 = st.text_input("Enter color 1 code (#FF0000):")
    color_code2 = st.text_input("Enter color 2 code (#FF0000):")
    color_code3 = st.text_input("Enter color 3 code (#FF0000):")
    color_code4 = st.text_input("Enter color 4 code (#FF0000):")

    submitted = st.form_submit_button("Submit")

    if submitted:
        # Render HTML with injected color codes using f-strings (as shown above)
        htmlText1 = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Colorful Information Page</title>
            <style>
            :root {
        """
        
        htmlText2 = f""" 
            --first-color: {color_code1}; 
            --second-color: {color_code2}; 
            --third-color: {color_code3};  
            --fourth-color: {color_code4}; 
        """
        
        htmlText3 = """
            }

            body {
                font-family: Arial, sans-serif;
                background: var(--first-color);
                color: var(--fourth-color);
                margin: 0;
                padding: 0;
            }

            .header {
                background: var(--third-color);
                color: #ffffff;
                padding: 10px;
                text-align: center;
            }

            .container {
                max-width: 1200px;
                margin: 20px auto;
                padding: 20px;
                background: var(--first-color);
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            .section {
                margin-bottom: 20px;
            }

            .section h2 {
                color: var(--second-color);
            }

            .section p {
                line-height: 1.6;
            }

            .footer {
                background: var(--third-color);
                color: #ffffff;
                text-align: center;
                padding: 10px;
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
            }
            </style>
            </head>
            <body>
            <header class="header">
                <h1>Colorful Information Page</h1>
            </header>
            <div class="container">
                <div class="section">
                <h2>About Us</h2>
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
                </div>
                <div class="section">
                <h2>Services</h2>
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
                </div>
                <div class="section">
                <h2>Contact Us</h2>
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
                </div>
            </div>
            <footer class="footer">
                <p>&copy; 2024 Colorful Information Page</p>
            </footer>
            </body>
            </html>
        """
        
        htmlText = htmlText1 + htmlText2 + htmlText3

        components.html(htmlText, height=800)

        