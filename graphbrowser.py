import webview
class webbrowser():
    def __init__(self,title,url):
        webview.create_window(title, url)
        webview.start()