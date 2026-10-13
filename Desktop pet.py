import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QTransform, QPainter, QColor
from PyQt5.QtCore import Qt, QTimer

class DesktopPet(QWidget):
    def __init__ (self):
        super(). __init__()
        self.label = QLabel(self)
        self.direction = 1
        self.state = "idle"
        self.state_time = 0
        self.speed = 5
        self.frame_index = 0
        self.delay = 0
        self.has_ball = False
        self.idle_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Idle 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Idle 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Idle 3.png")]
        self.walk_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Walk 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Walk 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Walk 3.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Walk 4.png")]
        self.sleep_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Sleep 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Sleep 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Sleep 3.png")]
        self.happy_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Happy 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Happy 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Happy 3.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Happy 4.png")]
        self.confused_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Confused 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Confused 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Confused 3.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Confused 4.png")]
        self.annoyed_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Annoyed 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Annoyed 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Annoyed 3.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Annoyed 4.png")]
        self.holding_ball_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Run 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Run 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Run 3.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Run 4.png")]
        self.sad_frames = [
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Sad 1.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Sad 2.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Sad 3.png"),
            QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Sad 4.png")]
        self.hang_frames = [QPixmap("C:/Users/admin/Desktop/pet/Robot Monkey Hang.png")]
        self.click_count = 0
        self.click_timer = QTimer()
        self.click_timer.setSingleShot(True)
        self.click_timer.timeout.connect(self.reset_clicks)
        self.has_ball = False
        self.ball = None
        self.ball_released = False
        self.idle_duration = random.randint(4, 10)
        self.rod_x = 900
        self.rod_y = 150
        self.hanging = False
        self.initUI()
    def initUI(self):
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(250,250)

        self.label.setGeometry(0,0,250,250)
        pixmap=QPixmap("C:/Users/admin/Desktop/Cherry's folder/Robot Monkey Idle 1.png")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_pet)
        self.timer.start(250)

    def move_pet(self):
        pos = self.pos()
        screen = QApplication.primaryScreen().availableGeometry()

        # Check whether the monkey has reached the rod
        if abs(pos.x() - self.rod_x) <= self.speed:
            self.state = "hanging"
            self.state_time = 0
            self.frame_index = 0
            self.delay = 0
            self.move(self.rod_x, self.rod_y - 40)
            return

        if pos.x() + self.width() >= screen.right():
            self.direction = -1

        elif pos.x() <= screen.left():
            self.direction = 1

        self.move(pos.x() + (self.speed * self.direction), pos.y())

    def update_frame(self):

        if self.state == "idle":
            frames = self.idle_frames

        elif self.state == "walking":
            frames = self.walk_frames

        elif self.state == "holding_ball":
            frames = self.holding_ball_frames

        elif self.state == "hanging":
            frames = self.hang_frames
            self.label.setPixmap(self.hang_frames[0])

        elif self.state == "sleeping":
            frames = self.sleep_frames
            self.delay += 1

            if self.delay < 6:
                return

            self.delay = 0

            if self.frame_index == 0:
                pixmap = frames[0]
                self.frame_index = 1
            else:
                pixmap = frames[self.frame_index]

                if self.frame_index == 1:
                    self.frame_index = 2
                else:
                    self.frame_index = 1

            self.label.setPixmap(pixmap)
            return

        elif self.state == "happy":
            frames = self.happy_frames
            self.delay += 1

            if self.delay < 2:
                return

            self.delay = 0

        elif self.state == "confused":
            frames = self.confused_frames
            self.delay += 1

            if self.delay < 2:
                return

            self.delay = 0

        elif self.state == "annoyed":
            frames = self.annoyed_frames
            self.delay += 1

            if self.delay < 2:
                return

            self.delay = 0

        elif self.state == "sad":
            frames = self.sad_frames
            self.delay += 1

            if self.delay < 2:
                return

            self.delay = 0

        else:
            return

        pixmap = frames[self.frame_index]

        if self.state in ["idle", "walking"] and self.direction == -1:
            pixmap = pixmap.transformed(QTransform().scale(-1, 1))

        self.label.setPixmap(pixmap)

        self.frame_index += 1

        if self.frame_index >= len(frames):
            self.frame_index = 0

    def enterEvent(self, event):
        if self.has_ball:
            return

        self.state = "happy"
        self.state_time = 0
        self.frame_index = 0
        self.delay = 0

    def leaveEvent(self, event):
        if self.has_ball:
            return

        self.state = "confused"
        self.state_time = 0
        self.frame_index = 0
        self.delay = 0

    def mousePressEvent(self, event):
        self.click_count += 1

        self.click_timer.start(1500)

        if self.click_count >= 3:
            self.state = "annoyed"
            self.state_time = 0
            self.frame_index = 0
            self.delay = 0

            self.click_count = 0
            self.click_timer.stop()

        if self.has_ball:
            self.has_ball = False
            self.ball_released = True
            self.ball.show()
            self.state = "sad"
            self.state_time = 0
            self.frame_index = 0
            self.delay = 0

    def reset_clicks(self):
        self.click_count = 0

    def ball_near_monkey(self):
        if self.ball_released:
            return
        if self.ball is None or self.has_ball:
            return

        ball_center = self.ball.geometry().center()
        monkey_center = self.geometry().center()

        distance = ((ball_center.x() - monkey_center.x()) ** 2 +(ball_center.y() - monkey_center.y()) ** 2) ** 0.5

        if distance < 100:
            self.has_ball = True
            self.state = "holding_ball"
            self.state_time = 0
            self.frame_index = 0
            self.delay = 0

    def check_ball_taken(self):
        if not self.has_ball or self.ball is None:
            return

    def move_ball_with_pet(self):
        if self.ball is None:
            return

        if self.has_ball and not self.ball.dragging:
            self.ball.hide()
        else:
            self.ball.show()

    def update_pet(self):

        self.state_time += 0.25
        self.ball_near_monkey()
        self.check_ball_taken()
        self.move_ball_with_pet()
        self.update_frame()

        if self.state == "idle" and self.state_time >= self.idle_duration:
            self.state = "walking"
            self.state_time = 0
            self.idle_duration = random.randint(4, 10)

        elif self.state == "walking":
            self.move_pet()
            if self.state_time >= 10:
                self.state = "sleeping"
                self.state_time = 0
                self.frame_index = 0

        elif self.state == "hanging":
            if self.state_time >= 5:
                self.state = "idle"
                self.state_time = 0
                self.frame_index = 0
                self.delay = 0

        elif self.state == "sleeping":
            if self.state_time >= 10:
                self.state = "idle"
                self.state_time = 0
                self.frame_index = 0

        elif self.state == "happy":
            if self.state_time >= 2:
                self.state_time = 0
                self.frame_index = 0
                self.delay = 0

        elif self.state == "confused":
            if self.state_time >= 3:
                self.state = "idle"
                self.state_time = 0
                self.frame_index = 0
                self.delay = 0

        elif self.state == "annoyed":
            if self.state_time >= 2:
                self.state = "idle"
                self.state_time = 0
                self.frame_index = 0
                self.delay = 0

        elif self.state == "sad":
            if self.state_time >= 5:
                self.state = "idle"
                self.state_time = 0
                self.frame_index = 0
                self.delay = 0

        elif self.state == "holding_ball":
            self.move_pet()


class Ball(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.label = QLabel(self)
        self.ball = QPixmap("C:/Users/admin/Desktop/pet/ball.png").copy(497, 497, 254, 254).scaled(
    60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(self.ball)
        self.label.resize(self.ball.size())
        self.resize(self.ball.size())
        print(self.ball.size())
        self.offset = None
        self.dragging = False
        self.desktop_pet = None
    def mousePressEvent(self, event):
        self.dragging = True
        self.offset = event.pos()
        self.show()
        if self.desktop_pet:
            self.desktop_pet.ball_released = False

    def mouseMoveEvent(self, event):
        if self.dragging:
            new_position = event.globalPos() - self.offset
            self.move(new_position)
            self.show()

            if self.desktop_pet and self.desktop_pet.has_ball:
                self.desktop_pet.has_ball = False
                self.desktop_pet.state = "sad"
                self.desktop_pet.state_time = 0
                self.desktop_pet.frame_index = 0
                self.desktop_pet.delay = 0
    def mouseReleaseEvent(self, event):
        self.dragging = False


class Rod(QWidget):
    def __init__(self, x=500, y=300, width=180):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.rod_width = width
        self.setGeometry(x, y, width, 12)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#A9A9A9"))
        painter.drawRoundedRect(0, 3, self.rod_width, 6, 3, 3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    desktop_pet = DesktopPet()
    ball = Ball()
    desktop_pet.ball = ball
    ball.desktop_pet = desktop_pet
    desktop_pet.move(200, 200)
    ball.move(600, 300)
    rod = Rod(900, 150, 180)
    rod.show()
    ball.show()
    desktop_pet.show()
    sys.exit(app.exec_())
