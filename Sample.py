import ht
google='https://google.com'
print(
ht.head(
	ht.title('test')
	+ht.link(rel='stylesheet',href='style.css')
	)
+ht.body(
	ht.h1('test')
	+'this is test page\n'
	+ht.a('link',href=google)
	)
)
