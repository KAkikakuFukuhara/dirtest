# memo

ディレクトリ直下に実行ファイルを置きたくないので以下のよう 'tools' ディレクトリに置く。
実行は `dirtest/__main__.py` がtoolsディレクトリの実行ファイルの main 関数を呼び出す形式にする。

```console
.
└ dirtest
  ├ __init__.py
  ├ __main__.py
  ├ moda.py
  ├ _path_adding.py
  └ tools
    ├ _path_adding.py
    ├ __init__.py
    ├ exe1.py
    └ exe2.py
```

`__main__.py` と同一のディレクトリに _path_adding.py を配置することでプロジェクトのルートから import 出来るようにする。
```diff
- from tools import exe1
+ from dirtest.tools import exe1
```




