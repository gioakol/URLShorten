import pyshorteners as ps
import streamlit as sl
import validators as val

def ShortenURL(url):
    try:
        if isValidURL(url):
            s = ps.Shortener()
            shortenedUrl = s.tinyurl.short(url)
            return shortenedUrl
        else:
            return f"Error: the url {url} is not valid, add https:// to path"
    except Exception as error:
        return f"Error creating the new url: {error}"

def isValidURL(url):
    if val.url(url):
        return True
    else:
        return False

def main():
    # val = ShortenURL("aSASD")
    # print(val)

    sl.set_page_config(page_title="Shortener URL", page_icon=None, layout="centered")
    sl.title("URL Shortener")
    url = sl.text_input("Write u URL", placeholder="https://www.google.com")

    if sl.button("Get new URL"):
        sl.write("Result: ", ShortenURL(url))
        
main()