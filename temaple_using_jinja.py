from jinja2 import Template
import pdfkit


def open_template(template_filename) -> Template:
    with open(template_filename, 'r') as template_file:
        return Template(template_file.read())


def get_invoice_as_html(items_data) -> str:
    invoice_template = open_template('./template/invoice.html')
    return invoice_template.render(items=items_data)


def main():
    items_data = [
        {'value1': 'Row One Value One', 'value2': 'Row One Value Two',
         'value3': 'Row One Value Three'},
        {'value1': 'Row Two Value One', 'value2': 'Row Two Value Two',
         'value3': 'Row Two Value Three'},
        {'value1': 'Row Three Value One', 'value2': 'Row Three Value Two',
         'value3': 'Row Three Value Three'},
    ]

    invoice_html = get_invoice_as_html(items_data)
    invoice = pdfkit.from_string(invoice_html, False)

    # Esto no tendríamos que hacer porque mandaríamos el binario a printnode
    with open('invoice-1.pdf', 'wb') as invoice_file:
        invoice_file.write(invoice)


if __name__ == '__main__':
    main()
