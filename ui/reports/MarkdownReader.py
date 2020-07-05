
from epyk.core.data import datamap, events, primitives


def get_page(page):
    """

    :param page:

    :type page: epyk.core.Page.Report
    """
    page.headers.dev()
    contents = page.ui.contents("Contente")
    md = page.ui.rich.markdown()
    # md.tooltips({"value": 'Ok'})

    md.onReady([
      page.js.post(primitives.str("/docs/get/") + page.js.location.urlSearchParams.get("type"),
        datamap(attrs={"category": 'file'})).onSuccess([
          md.build(events.data['markdown']), contents.build(events.data['contents'])
      ])
    ])
