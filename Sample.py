import ht
print("Content-Type: text/html")
print()
google='https://google.com'
print(html(
ht.head(
	ht.title('test')
	+ht.link(rel='stylesheet',href='style.css')
	)
+ht.body(
	ht.h1('test')
	+'this is test page\n'
	+ht.a('link',href=google)
	)
))
