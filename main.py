with open('url.txt', 'r') as url_file:
    url = url_file.read()

with open('index-template.html', 'r') as template_file:
    contents = template_file.read()

with open('index.html', 'w') as index_file:
    index_file.write(contents.replace('__URL__', url.strip()))
