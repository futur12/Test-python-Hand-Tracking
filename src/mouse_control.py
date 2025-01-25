import pyautogui

class MouseController:
    def __init__(self):
        self.previous_position = None

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y)

    def click(self, button='left'):
        pyautogui.click(button=button)

    def right_click(self):
        self.click(button='right')

