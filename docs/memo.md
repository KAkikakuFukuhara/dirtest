# memo

## 実行ファイルを`__main__.py`ディレクトリに置かない

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

## symbolic link で編集可能にする

開発段階ではpoetryでinstallしたモノは編集可能でインストールが可能である。  
一方 pip 環境において `pip install -e .` でインストールした場合、対象のディレクトリは変更可能であるが(ここではdirtest)、インストールしているモノは編集が反映されない。  
そこでシンボリックリンクを使用して編集したモノが反映されるようにする。  
以下のように `pkgs`　ディレクトリに存在するパッケージに対してシンボリックリンクを作る。  
注意点として パッケージに対してリンクするのではなく、ソースファイルがある場所にリンクさせる（例  ../pkgs/sa/sa)  
```console
.
├── README.md
├── dirtest
│   ├── __init__.py
│   ├── __main__.py
│   ├── sa -> ../pkgs/sa/sa/
├── pkgs
│   └── sa
│       ├── pyproject.toml
│       └── sa
│           ├── __init__.py
│           └── modsa.py
├── pyproject.toml
└── requirements.txt
```
