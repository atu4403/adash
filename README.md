ユーティリティライブラリ

## install

```bash
pip install adash
```

## useit

[Lodash](https://lodash.com/)のような使い方を推奨します。

```python
import adash as _

s = "abcabc"
obj = {"a": "!", "b": "", "c": "?"}
_.replace_all(s, obj) #-> !?!?
```
