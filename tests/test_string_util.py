import src.adash as _
from math import isnan


class TestReplaceAll:
    def test_01(self):
        s = "3円00銭"
        obj = {"円": ".", "銭": ""}
        assert _.replace_all(s, obj) == "3.00"

    def test_02(self):
        s = "abcabc"
        obj = {"a": "!", "b": "", "c": "?"}
        assert _.replace_all(s, obj) == "!?!?"

    def test_03(self):
        obj = {"[△▲]": "-", "[,、]": ""}
        assert _.replace_all('▲12,345', obj) == _.replace_all('△12、345', obj)


class TestHalfString:
    def test_01(self):
        assert _.to_half_string("１２３４５ａｂｃ") == "12345abc"


class TestToNumber:
    def test_01(self):
        assert _.to_number('123,456') == 123456
        assert _.to_number('-123,456') == -123456
        assert _.to_number('▲123,456') == -123456
        assert _.to_number('△123,456') == -123456
        assert isnan(_.to_number('▼123,456'))
        assert isnan(_.to_number('abc'))
        assert _.to_number('abc', True) is True
        assert _.to_number('abc', False) is False
        assert _.to_number('18円32銭') == 18.32
        assert _.to_number('18円00銭') == 18
        assert _.to_number('18円') == 18
        assert _.to_number('18%') == 18
        assert _.to_number('18％') == 18
        assert _.to_number('１２３，４５６，７８９') == 123456789


class TestToDate:
    def test_01(self):
        td = _.to_date
        assert td('２０１８年５月２７日') == '2018-05-27'
        assert td('2018年1月1日') == '2018-01-01'
        assert td('平成30年 5月11日') == '2018-05-11'
        assert td('令和元年 5月11日') == '2019-05-11'
        assert td('令和 元年 5月12日') == '2019-05-12'
        assert td('令和2年 5月11日') == '2020-05-11'
        assert td('平成３０年５月２７日') == '2018-05-27'
        assert td('昭和３０年５月２７日') == '1955-05-27'
        assert td('大正３年５月２７日') == '1914-05-27'
        assert td('大３年５月２７日') == '1914-05-27'
        assert td('2018-5-27') == '2018-05-27'
        assert td('2018/5/27') == '2018-05-27'
        assert td('20180527') == '2018-05-27'
        assert td('Unknown') is None


class TestSplitUpperCase:
    def test_01(self):
        assert _.split_uppercase('IsJSON') == ['Is', 'JSON']
        assert _.split_uppercase('ILoveYou') == ['ILove', 'You']
        assert _.split_uppercase('NextAccumulatedQ2Duration') == ['Next', 'Accumulated', 'Q2', 'Duration']
