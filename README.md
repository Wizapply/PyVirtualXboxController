# PyVirtualXboxController
VirtualXboxController for Python

# フォルダ構成
 
* `VirtualController32.py`
…仮想コントローラーを動作させるプログラム(32bit)
* `VirtualController64.py`
…仮想コントローラーを動作させるプログラム(64bit)
* `External/vGenInterface32.dll`
…vGenライブラリ(32bit)ビルド済み
https://github.com/shauleiz/vGen
* `External/vGenInterface64.dll`
…vGenライブラリ(64bit)ビルド済み
https://github.com/shauleiz/vGen

## 使用パッケージ
* `Kivy`
…GUIライブラリ
* `threading`
…マルチスレッド用ライブラリ
* `ctypes`
…C互換用ライブラリ

## 使用SDK
* `vJoy`
…仮想コントローラー用
https://sourceforge.net/projects/vjoystick/?source=directory
* `UCR`
…仮想コントローラーのキーマッピング用
https://inoookov.hatenablog.com/entry/2020/05/18/143935

# ソースコードについて
* `class RootWidget(FloatLayout)`
… UI配置用クラス
* `class kivy(App)`
… kivyクラス(GUI表示用)
* `class VirtualController(threading.Thread)`
… 仮想コントローラークラス(コントローラー毎にスレッドを立てています)
* `class ControllerInput`
… コントローラー入力格納用構造体
