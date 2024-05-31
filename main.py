from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")
top_text = input("введите верхний текст мема: ")
bottom_text = input("введите нижний текст мема: ")
top_indent = len(top_text) / 2 * 50
bottom_indent = len(bottom_text) / 2 * 50

image = None
print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
image_number = int(input("введите номер картинки: "))
if image_number == 1:
  image = "Кот в ресторане.png"
elif image_number == 2:
  image = "Кот в очках.png"
else:
  print("Такой картинки нет")
image = Image.open(image)
pero = ImageDraw.Draw(image)
shrift = ImageFont.truetype("arial.ttf", 93)



pero.text((image.width // 2 - top_indent, 0), top_text ,font=shrift, fill="black") #размещаем верхний текст
pero.text((image.width // 2 - bottom_indent, image.height-100), bottom_text, font=shrift, fill="black")

#сохранение
image_name = input("Введите название картинки") + ".png"
image.save(image_name)