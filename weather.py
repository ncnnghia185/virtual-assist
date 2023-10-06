from requests_html import HTMLSession 
import speech_to_text
def weather():
    s = HTMLSession()
    query = "HaNoi"
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url,
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'})
    temp = r.html.find('div.weatheroX8Yw',first=True).text

    unit = r.html.find('span#weather-kHhk3').text

    desc = r.html.find('div.weather-yWMJE').text


    return temp+" " + unit+" "+desc