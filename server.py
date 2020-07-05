
import os
import re

from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder="./static", template_folder="./ui/views")


@app.route('/')
def home():
    """

    :return:
    """
    return 'Hoe page'


@app.route('/docs')
def viewer():
  """
  Home page for the documentation
  :return:
  """
  return render_template('MarkdownReader.html'), 200


@app.route('/docs/get/<category>', methods=['POST'])
def viewer_content(category=None):
  """
  API to get the content from the Markdown file on the server.

  :param category: String. The documentation category
  """
  if category is None:
    pass

  doc_file_path = os.path.join(app.static_folder, "docs", "%s.md" % category)
  if os.path.exists(doc_file_path):
    with open(doc_file_path) as f:
      content = f.read()
      anchors = re.findall('<a id="([_a-zA-Z0-9]*)" name"anchor" data-level=([0-9]*) data-label="(.*)"></a>', content)
      content_table = []
      if anchors is not None:
        for anchor in anchors:
          content_table.append({"text": anchor[2], "anchor": "#%s" % anchor[0], 'level': int(anchor[1])})
      return {"markdown": content, 'contents': content_table}

  return {"markdown": "This documentation %s it not yet available" % category, 'contents': []}
