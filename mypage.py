
class Mypage():

    def __init__(self,page,ret):                              #self.n当前页码 self.x最大页码
        self.page=page
        self.ret=ret
        if not self.page:
            self.page = '1'
        try:
            self.n = int(self.page)
            count = self.ret.count()
            self.x, self.y = divmod(count, 9)
            if self.y:
                self.x = self.x + 1
            if self.n > self.x:
                self.n = self.x
        except:
            self.n = 1

        self.start = self.n - 3
        self.end = self.n + 3

        if self.start < 1:
            self.start = 1
        if self.end > self.x:
            self.end = self.x

    def html(self):
        html=''
        for i in range(self.start-1,self.end):
            if i+1 == self.n:
                html += '<li class="active"><a href="/book/?page={0}">{0}</a></li>'.format(i + 1)
            else:
                html+='<li><a href="/book/?page={0}">{0}</a></li>'.format(i+1)

        html+="""<li><a href="/book/?page={}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                    </a></li>""".format(self.x)
        return html

    @property
    def lastret(self):
        ret = self.ret[self.n * 8 - 8:self.n * 8]
        return ret
