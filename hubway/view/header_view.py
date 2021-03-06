import tkinter as tk
from viewable import Viewable
from megawidget.toast import Toast


class HeaderView(Viewable):
    def __init__(self, master, main_view, main_host):
        super().__init__()
        self._master = master
        self._main_view = main_view
        self._main_host = main_host
        self._body = None
        self._toast_loading = None
        # stringvar
        self._stringvar = tk.StringVar()

    def show_rate(self, data):
        if self._toast_loading:
            self._toast_loading.destroy()
            self._toast_loading = None
        status_code, status_text, data = data
        message = None
        duration = 1600
        if status_code in (200, 304):
            message = "Rate Limit:\t{}\nRemaining :\t{}".format(data["limit"],
                                                             data["remaining"])
            message = tab_to_space(message, tab_size=4)
        else:
            duration = 1000
            message = "Failed to load data\n{}".format(status_text)
        Toast(self._body, message=message, duration=duration)

    # =========================================
    #               LIFECYCLE
    # =========================================
    def _build(self):  # TODO, on windows, the ">" button isn't well aligned with widgets at Left
        self._body = tk.Frame(self._master)
        # label Query
        label_query = tk.Label(self._body, name="label_query", text="Query:")
        label_query.pack(side=tk.LEFT, fill=tk.BOTH)
        # entry
        entry_search = tk.Entry(self._body, name="entry_search",
                                width=40,
                                textvariable=self._stringvar)
        entry_search.bind("<Return>", lambda e, self=self: self._on_click_search())
        entry_search.pack(side=tk.LEFT, fill=tk.BOTH)
        entry_search.focus()
        # button run
        button_run = tk.Button(self._body, name="button_go", text=">",
                               command=self._on_click_search)
        button_run.pack(side=tk.LEFT, fill=tk.BOTH)
        # button rate
        button_rate = tk.Button(self._body, name="button_rate", text="Rate",
                                command=self._on_click_rate)
        button_rate.pack(side=tk.RIGHT, fill=tk.BOTH)

    # =========================================
    #               PRIVATE
    # =========================================
    def _on_click_search(self):
        data = self._stringvar.get()
        if data:
            data = self._main_host.extract_owner_repo_from_url(data)
        if not data:
            return
        self._stringvar.set("{}/{}".format(*data))
        self._main_view.central_view.add_node(*data)

    def _on_click_rate(self):
        if self._toast_loading:
            return
        self._toast_loading = Toast(self._body,
                                    message="Rate Limit: Loading...",
                                    duration=None)
        threadom = self._main_view.threadom
        host = self._main_host.rate
        consumer = self.show_rate
        threadom.run(host, consumer=consumer)


def tab_to_space(text, tab_size=4):
    TAB = "\t"
    SPACE = " "
    lines = text.split("\n")
    results = []
    for line in lines:
        cache = str()
        for char in line:
            if char == TAB:
                while len(cache) % tab_size != 0:
                    cache += SPACE
            else:
                cache += char
        results.append(cache)
    return "\n".join(results)
