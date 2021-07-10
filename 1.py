from html2image import Html2Image
hti = Html2Image()

url = 'https://www.w3schools.com/python/'
hti.screenshot(url=url, save_as='w3schools.png')

exit()
hti.screenshot(url='https://www.python.org', save_as='python_org.png')


html = """<h1> An interesting title </h1> This page will be red"""
css = "body {background: red;}"

hti.screenshot(html_str=html, css_str=css, save_as='red_page.png') 
