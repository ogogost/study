import arcade

# Задать константы для размеров экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Открыть окно. Задать заголовок и размеры окна (ширина и высота)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

# Задать белый цвет фона.
# Для просмотра списка названий цветов прочитайте:
# http://arcade.academy/arcade.color.html
# Цвета также можно задавать в (красный, зеленый, синий) и
# (красный, зеленый, синий, альфа) формате.
arcade.set_background_color(arcade.color.WHITE)

# Начать процесс рендера. Это нужно сделать до команд рисования
arcade.start_render()

# Нарисовать лицо
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)