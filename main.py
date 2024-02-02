from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render()

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    main()
    server = Server()
    server.watch('template.html', main)
    server.serve(port=8087, host='localhost')
