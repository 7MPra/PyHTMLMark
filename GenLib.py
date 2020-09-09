import re
tags = ['a','abbr','address','article','aside','audio','b','bdo','blockquote','body','button','canvas','caption','cite','cite','code','colgroup','command','datalist','dd','del','details','dfn','div','dl','dt','em','fieldset','figcaption','figure','footer','form','h1','h2','h3','h4','h5','h6','head','header','html','i','iframe','ins','kbd','label','legend','li','map','main','mark','menu','meter','nav','noscript','object','ol','optgroup','option','output','p','pre','progress','q','rp','rt','ruby','s','samp','script','section','select','small','span','strong','style','sub','summary','sup','table','tbody','td','textarea','tfoot','th','thead','time','title','tr','ul','var','video']
nctags = ['br','img','hr','meta','input','embed','area','base','col','keygen','link','param','source']
with open('ht.py', mode='w') as f:
	f.write('import re\n')
	for s in nctags:
		f.write('''def {1}(**kwargs):
	args = ' '+' '.join([re.sub('_','','{0}="{0}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<{1}{0}>\\n'.format(args)
'''.format('{}',s))
	for s in tags:
		f.write(re.sub('def del','def _del','''def {1}(content,**kwargs):
	content = content[:-1] if content[-1:]=='\\n' else content
	args = ' '+' '.join([re.sub('_','','{0}="{0}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<{1}{0}>\\n  '.format(args)+re.sub('\\n','\\n  ',content)+'\\n</{1}>\\n'
'''.format('{}',s)))
