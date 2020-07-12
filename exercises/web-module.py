import webbrowser as page, requests as req

res = req.get('https://economia.uol.com.br/')
print(res.text[:50])