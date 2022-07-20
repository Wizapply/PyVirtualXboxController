
from kivy.base import runTouchApp
from kivy.app import App
from kivy.uix.button import Label, Button
from kivy.uix.slider import Slider
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox

import threading

import ctypes





#UI配置用クラス
class RootWidget(FloatLayout):

    #UI構造体
    class UIStruct():

        #左スティックX
        SliderTitle_LeftStickX = Label()
        Slider_LeftStickX = Slider()
        SliderValue_LeftStickX = Label()
        #左スティックY
        SliderTitle_LeftStickY = Label()
        Slider_LeftStickY = Slider()
        SliderValue_LeftStickY = Label()
        #右スティックX
        SliderTitle_RightStickX = Label()
        Slider_RightStickX = Slider()
        SliderValue_RightStickX = Label()
        #右スティックY
        SliderTitle_RightStickY = Label()
        Slider_RightStickY = Slider()
        SliderValue_RightStickY = Label()
        #左トリガー
        SliderTitle_LeftTrigger = Label()
        Slider_LeftTrigger = Slider()
        SliderValue_LeftTrigger = Label()
        #右トリガー
        SliderTitle_RightTrigger = Label()
        Slider_RightTrigger = Slider()
        SliderValue_RightTrigger = Label()
        #Aボタン
        CheckBoxTitle_ButtonA = Label()
        ButtonA = CheckBox()
        #Bボタン
        CheckBoxTitle_ButtonB = Label()
        ButtonB = CheckBox()
        #Xボタン
        CheckBoxTitle_ButtonX = Label()
        ButtonX = CheckBox()
        #Yボタン
        CheckBoxTitle_ButtonY = Label()
        ButtonY = CheckBox()
        #LSボタン
        CheckBoxTitle_ButtonLS = Label()
        ButtonLS = CheckBox()
        #RSボタン
        CheckBoxTitle_ButtonRS = Label()
        ButtonRS = CheckBox()
        #LTボタン
        CheckBoxTitle_ButtonLT = Label()
        ButtonLT = CheckBox()
        #RTボタン
        CheckBoxTitle_ButtonRT = Label()
        ButtonRT = CheckBox()
        #Upボタン
        CheckBoxTitle_ButtonUp = Label()
        ButtonUp = CheckBox()
        #Downボタン
        CheckBoxTitle_ButtonDown = Label()
        ButtonUp = CheckBox()
        #Leftボタン
        CheckBoxTitle_ButtonLeft = Label()
        ButtonLeft = CheckBox()
        #Rightボタン
        CheckBoxTitle_ButtonRight = Label()
        ButtonRight = CheckBox()
        #Sartボタン
        CheckBoxTitle_ButtonStart = Label()
        ButtonStart = CheckBox()
        #Backボタン
        CheckBoxTitle_ButtonBack = Label()
        ButtonBack = CheckBox()
        
        #リセットボタン
        CheckBoxTitle_Reset = Label()
        ButtonReset = Button()

    #UI配置初期化
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        #座標
        #スライダー
        self.sliderPosX = 0.05
        self.sliderPosY = 0.95
        self.slilderWidth = 0.075
        #ボタン(チェックボックス)
        self.buttonPosX = 0.05
        self.buttonPosY = 0.25
        self.buttonWidth = 0.06
        self.buttonHeight = 0.1

        #コントローラー入力格納用構造体
        global controllerInputList
        self.controllerInputList = controllerInputList
        self.uiList = []
        #コントローラー番号
        controllerNum = 0

        while(controllerNum < len(self.controllerInputList)):
            self.uiList.append(self.UIStruct())

            #左スティックX_Slider
            self.uiList[controllerNum].SliderTitle_LeftStickX = Label(text="LeftX", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 0) + controllerNum * 0.5, 'center_y': self.sliderPosY})
            self.add_widget(self.uiList[controllerNum].SliderTitle_LeftStickX)
            self.uiList[controllerNum].Slider_LeftStickX = Slider(min=-1.00, max=1.00, value=0.00,orientation='vertical',step=0.01, size_hint=(0.05, 0.5),pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 0) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.325})
            if(controllerNum == 0):
                self.uiList[controllerNum].Slider_LeftStickX.bind(value=self.callbackSlider1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].Slider_LeftStickX.bind(value=self.callbackSlider2)
            self.add_widget(self.uiList[controllerNum].Slider_LeftStickX)
            self.uiList[controllerNum].SliderValue_LeftStickX = Label(text="0.00", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 0) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.05})
            self.uiList[controllerNum].SliderValue_LeftStickX.text=str(self.uiList[controllerNum].Slider_LeftStickX.value)
            self.add_widget(self.uiList[controllerNum].SliderValue_LeftStickX)
        
            #左スティックY_Slider
            self.uiList[controllerNum].SliderTitle_LeftStickY = Label(text="LeftY", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 1) + controllerNum * 0.5, 'center_y': self.sliderPosY})
            self.add_widget(self.uiList[controllerNum].SliderTitle_LeftStickY)
            self.uiList[controllerNum].Slider_LeftStickY = Slider(min=-1.00, max=1.00, value=0.00,orientation='vertical',step=0.01, size_hint=(0.05, .5),pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 1) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.325})
            if(controllerNum == 0):
                self.uiList[controllerNum].Slider_LeftStickY.bind(value=self.callbackSlider1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].Slider_LeftStickY.bind(value=self.callbackSlider2)
            self.add_widget(self.uiList[controllerNum].Slider_LeftStickY)
            self.uiList[controllerNum].SliderValue_LeftStickY = Label(text="0.00", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 1) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.05})
            self.uiList[controllerNum].SliderValue_LeftStickY.text=str(self.uiList[controllerNum].Slider_LeftStickY.value)
            self.add_widget(self.uiList[controllerNum].SliderValue_LeftStickY)

            #右スティックX_Slider
            self.uiList[controllerNum].SliderTitle_RightStickX = Label(text="RightX", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 2) + controllerNum * 0.5, 'center_y': self.sliderPosY})
            self.add_widget(self.uiList[controllerNum].SliderTitle_RightStickX)
            self.uiList[controllerNum].Slider_RightStickX = Slider(min=-1.00, max=1.00, value=0.00,orientation='vertical',step=0.01, size_hint=(0.05, .5),pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 2) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.325})
            if(controllerNum == 0):
                self.uiList[controllerNum].Slider_RightStickX.bind(value=self.callbackSlider1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].Slider_RightStickX.bind(value=self.callbackSlider2)
            self.add_widget(self.uiList[controllerNum].Slider_RightStickX)
            self.uiList[controllerNum].SliderValue_RightStickX = Label(text="0.00", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 2) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.05})
            self.uiList[controllerNum].SliderValue_RightStickX.text=str(self.uiList[controllerNum].Slider_RightStickX.value)
            self.add_widget(self.uiList[controllerNum].SliderValue_RightStickX)
        
            #右スティックY_Slider
            self.uiList[controllerNum].SliderTitle_RightStickY = Label(text="RightY", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 3) + controllerNum * 0.5, 'center_y': self.sliderPosY})
            self.add_widget(self.uiList[controllerNum].SliderTitle_RightStickY)
            self.uiList[controllerNum].Slider_RightStickY = Slider(min=-1.00, max=1.00, value=0.00,orientation='vertical',step=0.01, size_hint=(0.05, 0.5),pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 3) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.325})
            if(controllerNum == 0):
                self.uiList[controllerNum].Slider_RightStickY.bind(value=self.callbackSlider1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].Slider_RightStickY.bind(value=self.callbackSlider2)
            self.add_widget(self.uiList[controllerNum].Slider_RightStickY)
            self.uiList[controllerNum].SliderValue_RightStickY = Label(text="0.00", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 3) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.05})
            self.uiList[controllerNum].SliderValue_RightStickY.text=str(self.uiList[controllerNum].Slider_RightStickY.value)
            self.add_widget(self.uiList[controllerNum].SliderValue_RightStickY)

            #左トリガー_Slider
            self.uiList[controllerNum].SliderTitle_LeftTrigger = Label(text="LeftT", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 4) + controllerNum * 0.5, 'center_y': self.sliderPosY})
            self.add_widget(self.uiList[controllerNum].SliderTitle_LeftTrigger)
            self.uiList[controllerNum].Slider_LeftTrigger = Slider(min=0.00, max=1.00, value=0.00,orientation='vertical',step=0.01, size_hint=(0.05, 0.5),pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 4) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.325})
            if(controllerNum == 0):
                self.uiList[controllerNum].Slider_LeftTrigger.bind(value=self.callbackSlider1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].Slider_LeftTrigger.bind(value=self.callbackSlider2)
            self.add_widget(self.uiList[controllerNum].Slider_LeftTrigger)
            self.uiList[controllerNum].SliderValue_LeftTrigger = Label(text="0.00", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 4) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.05})
            self.uiList[controllerNum].SliderValue_LeftTrigger.text=str(self.uiList[controllerNum].Slider_LeftTrigger.value)
            self.add_widget(self.uiList[controllerNum].SliderValue_LeftTrigger)

            #右トリガー_Slider
            self.uiList[controllerNum].SliderTitle_RightTrigger = Label(text="RightT", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 5) + controllerNum * 0.5, 'center_y': self.sliderPosY})
            self.add_widget(self.uiList[controllerNum].SliderTitle_RightTrigger)
            self.uiList[controllerNum].Slider_RightTrigger = Slider(min=0.00, max=1.00, value=0.00,orientation='vertical',step=0.01, size_hint=(0.05, 0.5),pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 5) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.325})
            if(controllerNum == 0):
                self.uiList[controllerNum].Slider_RightTrigger.bind(value=self.callbackSlider1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].Slider_RightTrigger.bind(value=self.callbackSlider2)
            self.add_widget(self.uiList[controllerNum].Slider_RightTrigger)
            self.uiList[controllerNum].SliderValue_RightTrigger = Label(text="0.00", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.sliderPosX + self.slilderWidth * 5) + controllerNum * 0.5, 'center_y': self.sliderPosY - 0.05})
            self.uiList[controllerNum].SliderValue_RightTrigger.text=str(self.uiList[controllerNum].Slider_RightTrigger.value)
            self.add_widget(self.uiList[controllerNum].SliderValue_RightTrigger)

            #Aボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonA = Label(text="A", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': self.buttonPosY + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonA)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonA = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonA.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonA = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonA.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonA)

            #Bボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonB = Label(text="B", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': self.buttonPosY + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonB)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonB = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonB.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonB = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonB.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonB)

            #Xボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonX = Label(text="X", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': self.buttonPosY + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonX)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonX = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonX.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonX = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonX.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonX)

            #Yボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonY = Label(text="Y", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': self.buttonPosY + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonY)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonY = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonY.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonY = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': self.buttonPosY})
                self.uiList[controllerNum].ButtonY.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonY)

            #Upボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonUp = Label(text="Up", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonUp)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonUp = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonUp.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonUp = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonUp.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonUp)

            #Downボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonDown = Label(text="Down", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonDown)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonDown = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonDown.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonDown = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonDown.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonDown)

            #Leftボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonLeft = Label(text="Left", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonLeft)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonLeft = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonLeft.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonLeft = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonLeft.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonLeft)

            #Rightボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonRight = Label(text="Right", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonRight)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonRight = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonRight.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonRight = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 1)})
                self.uiList[controllerNum].ButtonRight.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonRight)


            #LSボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonLS = Label(text="LS", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonLS)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonLS = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonLS.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonLS = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 0) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonLS.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonLS)

            #RSボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonRS = Label(text="RS", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonRS)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonRS = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonRS.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonRS = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 1) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonRS.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonRS)

            #LTボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonLT = Label(text="LT", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonLT)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonLT = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonLT.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonLT = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 2) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonLT.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonLT)

            #RTボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonRT = Label(text="RT", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonRT)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonRT = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonRT.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonRT = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 3) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonRT.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonRT)


            #Backボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonBack = Label(text="Back", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 4) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonBack)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonBack = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 4) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonBack.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonBack = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 4) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonBack.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonBack)

            #Startボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonStart = Label(text="Start", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 5) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonStart)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonStart = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 5) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonStart.bind(active=self.onCheckbox1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonStart = CheckBox(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 5) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)})
                self.uiList[controllerNum].ButtonStart.bind(active=self.onCheckbox2)
            self.add_widget(self.uiList[controllerNum].ButtonStart)

            #リセットボタン
            self.uiList[controllerNum].CheckBoxTitle_ButtonReset = Label(text="Reset", font_size = "18sp",size_hint=(0.3, 0.2), pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 6.5) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2) + 0.05})
            self.add_widget(self.uiList[controllerNum].CheckBoxTitle_ButtonReset)
            if(controllerNum == 0):
                self.uiList[controllerNum].ButtonReset = Button(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 6.5) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)}, on_press = self.onReset1)
                #self.uiList[controllerNum].ButtonReset.bind(active=self.onReset1)
            elif(controllerNum == 1):
                self.uiList[controllerNum].ButtonReset = Button(size_hint=(0.05, 0.05),pos_hint={'center_x': (self.buttonPosX + self.buttonWidth * 6.5) + controllerNum * 0.5, 'center_y': (self.buttonPosY - self.buttonHeight * 2)}, on_press = self.onReset2)
                #self.uiList[controllerNum].ButtonReset.bind(active=self.onReset2)
            self.add_widget(self.uiList[controllerNum].ButtonReset)

            controllerNum += 1

    #スライダーコールバック(コントローラー１用)
    def callbackSlider1(self,instance,value):
        self.uiList[0].SliderValue_LeftStickX.text=str(format(self.uiList[0].Slider_LeftStickX.value,".2f"))
        self.controllerInputList[0].leftStickXValue = self.uiList[0].Slider_LeftStickX.value
        self.uiList[0].SliderValue_LeftStickY.text=str(format(self.uiList[0].Slider_LeftStickY.value,".2f"))
        self.controllerInputList[0].leftStickYValue = self.uiList[0].Slider_LeftStickY.value
        self.uiList[0].SliderValue_RightStickX.text=str(format(self.uiList[0].Slider_RightStickX.value,".2f"))
        self.controllerInputList[0].rightStickXValue = self.uiList[0].Slider_RightStickX.value
        self.uiList[0].SliderValue_RightStickY.text=str(format(self.uiList[0].Slider_RightStickY.value,".2f"))
        self.controllerInputList[0].rightStickYValue = self.uiList[0].Slider_RightStickY.value
        self.uiList[0].SliderValue_LeftTrigger.text=str(format(self.uiList[0].Slider_LeftTrigger.value,".2f"))
        self.controllerInputList[0].leftTriggerValue = self.uiList[0].Slider_LeftTrigger.value
        self.uiList[0].SliderValue_RightTrigger.text=str(format(self.uiList[0].Slider_RightTrigger.value,".2f"))
        self.controllerInputList[0].rightTriggerValue = self.uiList[0].Slider_RightTrigger.value


    #スライダーコールバック(コントローラー２用)
    def callbackSlider2(self,instance,value):
        self.uiList[1].SliderValue_LeftStickX.text=str(format(self.uiList[1].Slider_LeftStickX.value,".2f"))
        self.controllerInputList[1].leftStickXValue = self.uiList[1].Slider_LeftStickX.value
        self.uiList[1].SliderValue_LeftStickY.text=str(format(self.uiList[1].Slider_LeftStickY.value,".2f"))
        self.controllerInputList[1].leftStickYValue = self.uiList[1].Slider_LeftStickY.value
        self.uiList[1].SliderValue_RightStickX.text=str(format(self.uiList[1].Slider_RightStickX.value,".2f"))
        self.controllerInputList[1].rightStickXValue = self.uiList[1].Slider_RightStickX.value
        self.uiList[1].SliderValue_RightStickY.text=str(format(self.uiList[1].Slider_RightStickY.value,".2f"))
        self.controllerInputList[1].rightStickYValue = self.uiList[1].Slider_RightStickY.value
        self.uiList[1].SliderValue_LeftTrigger.text=str(format(self.uiList[1].Slider_LeftTrigger.value,".2f"))
        self.controllerInputList[1].leftTriggerValue = self.uiList[1].Slider_LeftTrigger.value
        self.uiList[1].SliderValue_RightTrigger.text=str(format(self.uiList[1].Slider_RightTrigger.value,".2f"))
        self.controllerInputList[1].rightTriggerValue = self.uiList[1].Slider_RightTrigger.value

    #チェックボックスコールバック(コントローラー１用)
    def onCheckbox1(self,instance,value):
        self.controllerInputList[0].ButtonA = self.uiList[0].ButtonA.active
        self.controllerInputList[0].ButtonB = self.uiList[0].ButtonB.active
        self.controllerInputList[0].ButtonX = self.uiList[0].ButtonX.active
        self.controllerInputList[0].ButtonY = self.uiList[0].ButtonY.active
        self.controllerInputList[0].ButtonUp = self.uiList[0].ButtonUp.active
        self.controllerInputList[0].ButtonDown = self.uiList[0].ButtonDown.active
        self.controllerInputList[0].ButtonLeft = self.uiList[0].ButtonLeft.active
        self.controllerInputList[0].ButtonRight = self.uiList[0].ButtonRight.active
        self.controllerInputList[0].ButtonLS = self.uiList[0].ButtonLS.active
        self.controllerInputList[0].ButtonRS = self.uiList[0].ButtonRS.active
        self.controllerInputList[0].ButtonLT = self.uiList[0].ButtonLT.active
        self.controllerInputList[0].ButtonRT = self.uiList[0].ButtonRT.active
        self.controllerInputList[0].ButtonStart = self.uiList[0].ButtonStart.active
        self.controllerInputList[0].ButtonBack = self.uiList[0].ButtonBack.active

    #チェックボックスコールバック(コントローラー２用)
    def onCheckbox2(self,instance,value):
        self.controllerInputList[1].ButtonA = self.uiList[1].ButtonA.active
        self.controllerInputList[1].ButtonB = self.uiList[1].ButtonB.active
        self.controllerInputList[1].ButtonX = self.uiList[1].ButtonX.active
        self.controllerInputList[1].ButtonY = self.uiList[1].ButtonY.active
        self.controllerInputList[1].ButtonUp = self.uiList[1].ButtonUp.active
        self.controllerInputList[1].ButtonDown = self.uiList[1].ButtonDown.active
        self.controllerInputList[1].ButtonLeft = self.uiList[1].ButtonLeft.active
        self.controllerInputList[1].ButtonRight = self.uiList[1].ButtonRight.active
        self.controllerInputList[1].ButtonLS = self.uiList[1].ButtonLS.active
        self.controllerInputList[1].ButtonRS = self.uiList[1].ButtonRS.active
        self.controllerInputList[1].ButtonLT = self.uiList[1].ButtonLT.active
        self.controllerInputList[1].ButtonRT = self.uiList[1].ButtonRT.active
        self.controllerInputList[1].ButtonStart = self.uiList[1].ButtonStart.active
        self.controllerInputList[1].ButtonBack = self.uiList[1].ButtonBack.active

    #リセットコールバック(コントローラー１用)
    def onReset1(self,instance):
        self.uiList[0].ButtonA.active = False
        self.uiList[0].ButtonB.active = False
        self.uiList[0].ButtonX.active = False
        self.uiList[0].ButtonY.active = False
        self.uiList[0].ButtonUp.active = False
        self.uiList[0].ButtonDown.active = False
        self.uiList[0].ButtonLeft.active = False
        self.uiList[0].ButtonRight.active = False
        self.uiList[0].ButtonLS.active = False
        self.uiList[0].ButtonRS.active = False
        self.uiList[0].ButtonLT.active = False
        self.uiList[0].ButtonRT.active = False
        self.uiList[0].ButtonStart.active = False
        self.uiList[0].ButtonBack.active = False

        self.controllerInputList[0].ButtonA = self.uiList[0].ButtonA.active
        self.controllerInputList[0].ButtonB = self.uiList[0].ButtonB.active
        self.controllerInputList[0].ButtonX = self.uiList[0].ButtonX.active
        self.controllerInputList[0].ButtonY = self.uiList[0].ButtonY.active
        self.controllerInputList[0].ButtonUp = self.uiList[0].ButtonUp.active
        self.controllerInputList[0].ButtonDown = self.uiList[0].ButtonDown.active
        self.controllerInputList[0].ButtonLeft = self.uiList[0].ButtonLeft.active
        self.controllerInputList[0].ButtonRight = self.uiList[0].ButtonRight.active
        self.controllerInputList[0].ButtonLS = self.uiList[0].ButtonLS.active
        self.controllerInputList[0].ButtonRS = self.uiList[0].ButtonRS.active
        self.controllerInputList[0].ButtonLT = self.uiList[0].ButtonLT.active
        self.controllerInputList[0].ButtonRT = self.uiList[0].ButtonRT.active
        self.controllerInputList[0].ButtonStart = self.uiList[0].ButtonStart.active
        self.controllerInputList[0].ButtonBack = self.uiList[0].ButtonBack.active

        self.uiList[0].Slider_LeftStickX.value = 0
        self.uiList[0].Slider_LeftStickY.value = 0
        self.uiList[0].Slider_RightStickX.value = 0
        self.uiList[0].Slider_RightStickY.value = 0
        self.uiList[0].Slider_LeftTrigger.value = 0
        self.uiList[0].Slider_RightTrigger.value = 0
        self.uiList[0].SliderValue_LeftStickX.text=str(format(self.uiList[0].Slider_LeftStickX.value,".2f"))
        self.controllerInputList[0].leftStickXValue = self.uiList[0].Slider_LeftStickX.value
        self.uiList[0].SliderValue_LeftStickY.text=str(format(self.uiList[0].Slider_LeftStickY.value,".2f"))
        self.controllerInputList[0].leftStickYValue = self.uiList[0].Slider_LeftStickY.value
        self.uiList[0].SliderValue_RightStickX.text=str(format(self.uiList[0].Slider_RightStickX.value,".2f"))
        self.controllerInputList[0].rightStickXValue = self.uiList[0].Slider_RightStickX.value
        self.uiList[0].SliderValue_RightStickY.text=str(format(self.uiList[0].Slider_RightStickY.value,".2f"))
        self.controllerInputList[0].rightStickYValue = self.uiList[0].Slider_RightStickY.value
        self.uiList[0].SliderValue_LeftTrigger.text=str(format(self.uiList[0].Slider_LeftTrigger.value,".2f"))
        self.controllerInputList[0].leftTriggerValue = self.uiList[0].Slider_LeftTrigger.value
        self.uiList[0].SliderValue_RightTrigger.text=str(format(self.uiList[0].Slider_RightTrigger.value,".2f"))
        self.controllerInputList[0].rightTriggerValue = self.uiList[0].Slider_RightTrigger.value

    #リセットコールバック(コントローラー２用)
    def onReset2(self,instance):
        self.uiList[1].ButtonA.active = False
        self.uiList[1].ButtonB.active = False
        self.uiList[1].ButtonX.active = False
        self.uiList[1].ButtonY.active = False
        self.uiList[1].ButtonUp.active = False
        self.uiList[1].ButtonDown.active = False
        self.uiList[1].ButtonLeft.active = False
        self.uiList[1].ButtonRight.active = False
        self.uiList[1].ButtonLS.active = False
        self.uiList[1].ButtonRS.active = False
        self.uiList[1].ButtonLT.active = False
        self.uiList[1].ButtonRT.active = False
        self.uiList[1].ButtonStart.active = False
        self.uiList[1].ButtonBack.active = False

        self.controllerInputList[1].ButtonA = self.uiList[1].ButtonA.active
        self.controllerInputList[1].ButtonB = self.uiList[1].ButtonB.active
        self.controllerInputList[1].ButtonX = self.uiList[1].ButtonX.active
        self.controllerInputList[1].ButtonY = self.uiList[1].ButtonY.active
        self.controllerInputList[1].ButtonUp = self.uiList[1].ButtonUp.active
        self.controllerInputList[1].ButtonDown = self.uiList[1].ButtonDown.active
        self.controllerInputList[1].ButtonLeft = self.uiList[1].ButtonLeft.active
        self.controllerInputList[1].ButtonRight = self.uiList[1].ButtonRight.active
        self.controllerInputList[1].ButtonLS = self.uiList[1].ButtonLS.active
        self.controllerInputList[1].ButtonRS = self.uiList[1].ButtonRS.active
        self.controllerInputList[1].ButtonLT = self.uiList[1].ButtonLT.active
        self.controllerInputList[1].ButtonRT = self.uiList[1].ButtonRT.active
        self.controllerInputList[1].ButtonStart = self.uiList[1].ButtonStart.active
        self.controllerInputList[1].ButtonBack = self.uiList[1].ButtonBack.active

        self.uiList[1].Slider_LeftStickX.value = 0
        self.uiList[1].Slider_LeftStickY.value = 0
        self.uiList[1].Slider_RightStickX.value = 0
        self.uiList[1].Slider_RightStickY.value = 0
        self.uiList[1].Slider_LeftTrigger.value = 0
        self.uiList[1].Slider_RightTrigger.value = 0
        self.uiList[1].SliderValue_LeftStickX.text=str(format(self.uiList[1].Slider_LeftStickX.value,".2f"))
        self.controllerInputList[1].leftStickXValue = self.uiList[1].Slider_LeftStickX.value
        self.uiList[1].SliderValue_LeftStickY.text=str(format(self.uiList[1].Slider_LeftStickY.value,".2f"))
        self.controllerInputList[1].leftStickYValue = self.uiList[1].Slider_LeftStickY.value
        self.uiList[1].SliderValue_RightStickX.text=str(format(self.uiList[1].Slider_RightStickX.value,".2f"))
        self.controllerInputList[1].rightStickXValue = self.uiList[1].Slider_RightStickX.value
        self.uiList[1].SliderValue_RightStickY.text=str(format(self.uiList[1].Slider_RightStickY.value,".2f"))
        self.controllerInputList[1].rightStickYValue = self.uiList[1].Slider_RightStickY.value
        self.uiList[1].SliderValue_LeftTrigger.text=str(format(self.uiList[1].Slider_LeftTrigger.value,".2f"))
        self.controllerInputList[1].leftTriggerValue = self.uiList[1].Slider_LeftTrigger.value
        self.uiList[1].SliderValue_RightTrigger.text=str(format(self.uiList[1].Slider_RightTrigger.value,".2f"))
        self.controllerInputList[1].rightTriggerValue = self.uiList[1].Slider_RightTrigger.value
        
#kivyクラス(GUI表示用)
class kjvyApp(App):
    def build(self):
        self.root = root = RootWidget()
        self.title = 'kjvyApp'

        return self.root


#仮想コントローラークラス
class VirtualController(threading.Thread):
    def __init__(self,controllerInput,num):
        super().__init__()

        #vGen##############
        self.vGenlib = ctypes.cdll.LoadLibrary("./External/vGenInterface64.dll")
        self.vGenlib.PlugIn(num);
        self.controllerInput = controllerInput
        self.controllerNum = num
        print(self.vGenlib)
        #################

        #XINPUTボタン###########
        self.XINPUT_GAMEPAD_DPAD_UP = 0x0001
        self.XINPUT_GAMEPAD_DPAD_DOWN = 0x0002
        self.XINPUT_GAMEPAD_DPAD_LEFT = 0x0004
        self.XINPUT_GAMEPAD_DPAD_RIGHT = 0x0008
        self.XINPUT_GAMEPAD_START = 0x0010
        self.XINPUT_GAMEPAD_BACK = 0x0020
        self.XINPUT_GAMEPAD_LEFT_THUMB = 0x0040
        self.XINPUT_GAMEPAD_RIGHT_THUMB = 0x0080
        self.XINPUT_GAMEPAD_LEFT_SHOULDER = 0x0100
        self.XINPUT_GAMEPAD_RIGHT_SHOULDER = 0x0200
        self.XINPUT_GAMEPAD_A = 0x1000
        self.XINPUT_GAMEPAD_B = 0x2000
        self.XINPUT_GAMEPAD_X = 0x4000
        self.XINPUT_GAMEPAD_Y = 0x8000
        ####################

    #正規化
    def normalize(self,value,min,max):
        if(value < min):
            value = min
        if(value > max):
            value = max
        return value

    def run(self):
        while(1):

            #vgen#############
            #スティック
            #-1～1→-32768～32768
            Lx = int(self.controllerInput.leftStickXValue * 32768)
            Ly = int(self.controllerInput.leftStickYValue * 32768)
            Rx = int(self.controllerInput.rightStickXValue * 32768)
            Ry = int(self.controllerInput.rightStickYValue * 32768)
            #-32768～32767に正規化
            Lx = self.normalize(Lx,-32768,32767)
            Ly = self.normalize(Ly,-32768,32767)
            Rx = self.normalize(Rx,-32768,32767)
            Ry = self.normalize(Ry,-32768,32767)
            #コントローラー入力
            self.vGenlib.SetAxisLx(self.controllerNum, Lx)
            self.vGenlib.SetAxisLy(self.controllerNum, Ly)
            self.vGenlib.SetAxisRx(self.controllerNum, Rx)
            self.vGenlib.SetAxisRy(self.controllerNum, Ry)
            #トリガー
            #0～1→0～255
            Lt = int(self.controllerInput.leftTriggerValue * 255)
            Rt = int(self.controllerInput.rightTriggerValue * 255)
            #コントローラー入力
            self.vGenlib.SetTriggerL(self.controllerNum, Lt);
            self.vGenlib.SetTriggerR(self.controllerNum, Rt);
            #ボタン
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_A ,self.controllerInput.ButtonA)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_B ,self.controllerInput.ButtonB)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_X ,self.controllerInput.ButtonX)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_Y ,self.controllerInput.ButtonY)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_LEFT_SHOULDER ,self.controllerInput.ButtonLS)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_RIGHT_SHOULDER ,self.controllerInput.ButtonRS)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_LEFT_THUMB ,self.controllerInput.ButtonLT)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_RIGHT_THUMB ,self.controllerInput.ButtonRT)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_DPAD_UP ,self.controllerInput.ButtonUp)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_DPAD_DOWN ,self.controllerInput.ButtonDown)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_DPAD_LEFT ,self.controllerInput.ButtonLeft)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_DPAD_RIGHT ,self.controllerInput.ButtonRight)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_START ,self.controllerInput.ButtonStart)
            self.vGenlib.SetButton(self.controllerNum,self.XINPUT_GAMEPAD_BACK ,self.controllerInput.ButtonBack)
            ################

#コントローラー入力格納用構造体
class ControllerInput():
    leftStickXValue = 0.00
    leftStickYValue = 0.00
    rightStickXValue = 0.00
    rightStickYValue = 0.00
    leftTriggerValue = 0.00
    rightTriggerValue = 0.00
    ButtonA = False
    ButtonB = False
    ButtonX = False
    ButtonY = False
    ButtonUp = False
    ButtonDown = False
    ButtonLeft = False
    ButtonRight = False
    ButtonLS = False
    ButtonRS = False
    ButtonLT = False
    ButtonRT = False
    ButtonStart = False
    ButtonBack = False


#メイン
if __name__ == "__main__":

    #コントローラー入力格納用構造体
    controllerInputList = []

    #仮想コントローラースレッド
    VirtualControllerList = []
    #コントローラー数(1か2)
    controllerMax = 2
    #コントローラースレッドを立てる
    controllerNum = 0
    while(controllerNum < controllerMax):
        #コントローラー入力格納用構造体を増やす
        controllerInputList.append(ControllerInput())
        #VirtualController(コントローラー入力格納用構造体リスト、コントローラー番号(1～))
        VirtualControllerList.append(VirtualController(controllerInputList[controllerNum],controllerNum + 1))
        #デーモンにする(メインスレッドが終了すれば、このスレッドを終了させる)
        VirtualControllerList[controllerNum].setDaemon(True)
        VirtualControllerList[controllerNum].start()
        controllerNum += 1

    #kjvy
    kjvyApp().run()

    #終了処理
    vGenlib = ctypes.cdll.LoadLibrary("./External/vGenInterface64.dll")
    vGenlib.UnPlug(1);
    vGenlib.UnPlug(2);
    print("vGenlib UnPlug")