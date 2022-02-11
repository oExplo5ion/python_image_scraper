from yattag import Doc

def generate_images_html(srcs):
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('body'):
            for src in srcs:
                with tag('div'):
                    doc.stag('img', src='{0}'.format(src))
                    with tag('p'):
                        text(src)
    return doc.getvalue()