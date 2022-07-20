# PyVirtualXboxController
VirtualXboxController for Python

# フォルダ構成
 
* `VirtualController32.py`
…仮想コントローラーを動作させるプログラム(32bit)
* `VirtualController64.py`
…仮想コントローラーを動作させるプログラム(64bit)
* `vGenInterface32.dll`
…vGenライブラリ(32bit)
* `vGenInterface64.dll`
…vGenライブラリ(64bit)

# 使用パッケージ
* `Kivy`
…GUIライブラリ
* `threading`
…マルチスレッド用ライブラリ
* `ctypes`
…C互換用ライブラリ

# ソースコードについて
* `class RootWidget(FloatLayout)`
… UI配置用クラス
* `class kivy(App)`
… kivyクラス(GUI表示用)
* `class VirtualController(threading.Thread)`
… 仮想コントローラークラス(コントローラー毎にスレッドを立てています)
* `class ControllerInput`
… コントローラー入力格納用構造体