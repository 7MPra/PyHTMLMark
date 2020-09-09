import re
def br(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<br{}>\n'.format(args)
def img(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<img{}>\n'.format(args)
def hr(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<hr{}>\n'.format(args)
def meta(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<meta{}>\n'.format(args)
def input(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<input{}>\n'.format(args)
def embed(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<embed{}>\n'.format(args)
def area(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<area{}>\n'.format(args)
def base(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<base{}>\n'.format(args)
def col(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<col{}>\n'.format(args)
def keygen(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<keygen{}>\n'.format(args)
def link(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<link{}>\n'.format(args)
def param(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<param{}>\n'.format(args)
def source(**kwargs):
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<source{}>\n'.format(args)
def a(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<a{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</a>\n'
def abbr(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<abbr{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</abbr>\n'
def address(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<address{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</address>\n'
def article(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<article{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</article>\n'
def aside(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<aside{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</aside>\n'
def audio(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<audio{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</audio>\n'
def b(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<b{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</b>\n'
def bdo(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<bdo{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</bdo>\n'
def blockquote(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<blockquote{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</blockquote>\n'
def body(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<body{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</body>\n'
def button(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<button{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</button>\n'
def canvas(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<canvas{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</canvas>\n'
def caption(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<caption{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</caption>\n'
def cite(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<cite{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</cite>\n'
def cite(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<cite{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</cite>\n'
def code(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<code{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</code>\n'
def colgroup(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<colgroup{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</colgroup>\n'
def command(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<command{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</command>\n'
def datalist(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<datalist{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</datalist>\n'
def dd(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<dd{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</dd>\n'
def _del(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<del{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</del>\n'
def details(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<details{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</details>\n'
def dfn(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<dfn{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</dfn>\n'
def div(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<div{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</div>\n'
def dl(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<dl{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</dl>\n'
def dt(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<dt{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</dt>\n'
def em(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<em{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</em>\n'
def fieldset(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<fieldset{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</fieldset>\n'
def figcaption(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<figcaption{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</figcaption>\n'
def figure(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<figure{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</figure>\n'
def footer(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<footer{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</footer>\n'
def form(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<form{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</form>\n'
def h1(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<h1{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</h1>\n'
def h2(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<h2{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</h2>\n'
def h3(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<h3{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</h3>\n'
def h4(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<h4{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</h4>\n'
def h5(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<h5{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</h5>\n'
def h6(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<h6{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</h6>\n'
def head(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<head{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</head>\n'
def header(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<header{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</header>\n'
def html(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<html{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</html>\n'
def i(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<i{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</i>\n'
def iframe(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<iframe{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</iframe>\n'
def ins(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<ins{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</ins>\n'
def kbd(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<kbd{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</kbd>\n'
def label(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<label{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</label>\n'
def legend(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<legend{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</legend>\n'
def li(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<li{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</li>\n'
def map(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<map{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</map>\n'
def main(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<main{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</main>\n'
def mark(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<mark{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</mark>\n'
def menu(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<menu{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</menu>\n'
def meter(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<meter{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</meter>\n'
def nav(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<nav{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</nav>\n'
def noscript(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<noscript{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</noscript>\n'
def object(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<object{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</object>\n'
def ol(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<ol{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</ol>\n'
def optgroup(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<optgroup{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</optgroup>\n'
def option(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<option{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</option>\n'
def output(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<output{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</output>\n'
def p(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<p{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</p>\n'
def pre(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<pre{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</pre>\n'
def progress(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<progress{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</progress>\n'
def q(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<q{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</q>\n'
def rp(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<rp{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</rp>\n'
def rt(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<rt{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</rt>\n'
def ruby(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<ruby{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</ruby>\n'
def s(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<s{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</s>\n'
def samp(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<samp{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</samp>\n'
def script(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<script{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</script>\n'
def section(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<section{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</section>\n'
def select(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<select{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</select>\n'
def small(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<small{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</small>\n'
def span(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<span{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</span>\n'
def strong(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<strong{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</strong>\n'
def style(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<style{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</style>\n'
def sub(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<sub{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</sub>\n'
def summary(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<summary{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</summary>\n'
def sup(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<sup{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</sup>\n'
def table(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<table{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</table>\n'
def tbody(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<tbody{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</tbody>\n'
def td(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<td{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</td>\n'
def textarea(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<textarea{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</textarea>\n'
def tfoot(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<tfoot{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</tfoot>\n'
def th(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<th{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</th>\n'
def thead(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<thead{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</thead>\n'
def time(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<time{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</time>\n'
def title(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<title{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</title>\n'
def tr(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<tr{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</tr>\n'
def ul(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<ul{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</ul>\n'
def var(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<var{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</var>\n'
def video(content,**kwargs):
	content = content[:-1] if content[-1:]=='\n' else content
	args = ' '+' '.join([re.sub('_','','{}="{}"'.format(s,kwargs[s])) for s in [ ss for ss in kwargs.keys()]])
	args = args[:-1] if args[-1:]==' ' else args
	return '<video{}>\n  '.format(args)+re.sub('\n','\n  ',content)+'\n</video>\n'
