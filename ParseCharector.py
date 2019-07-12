# coding=utf-8


import codecs, re


class ParseCharctor:

    def run(self):
        #print('xxx')
        raw_content = self.load_content()
        self.do_parse(raw_content)

    def load_content(self):
        file = '/Users/l/Downloads/8000ch.raw.txt'
        f = codecs.open(file, 'r', 'utf-8')
        raw_content = f.read()
        #print(raw_content)
        f.close()
        return raw_content

    def do_parse(self, raw_content):
        pattern = '<tr.*?<td.*?>(.*?)<.?/td>.*?>(.*?)<.?/td>.*?>(.*?)<.?/td.*?/tr>'
        #pattern = '<tr.*?>(.*?)<?/tr>'

        cparttern = re.compile(pattern)
        result1 = cparttern.findall(raw_content)
        if result1:
            for idx in result1:
                print(idx[0] + ', ' + idx[1] + ', ' + idx[2])

