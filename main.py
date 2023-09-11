from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv
from livereload import Server, shell


def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render()

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = Server()
    server.watch('template.html', shell('make html'))
    server.serve(root='.')


if __name__ == '__main__':
    main()
