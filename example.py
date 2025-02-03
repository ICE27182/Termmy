import termmy
settings = termmy.Settings()
try:
    settings.read_ansi_4bit_lookup()
except FileNotFoundError:
    settings.update_ansi_4bit_lookup(64)
    settings.write_ansi_4bit_lookup()
print("4bit done")
try:
    settings.read_ansi_8bit_lookup()
except FileNotFoundError:
    settings.update_ansi_8bit_lookup(24)
    settings.write_ansi_8bit_lookup()
print("8bit done")


def generate(type:int, width:int, height:int) -> termmy.Frame24:
        from random import randint
        frame = termmy.Frame24(width, height)
        for y in range(height):
            y_width = y * width
            for x in range(width):
                if type == 0:
                    frame.data[y_width + x] = (x * y % 256, (x + y) % 256, (x - y) % 256)
                elif type == 1:
                    frame.data[y_width + x] = (0,0,0) if (x + y) % 2 else (255, 255, 255)
                elif type == 2:
                    frame.data[y_width + x] = (randint(0, 255), randint(0, 255), randint(0, 255))
        return frame

frame = generate(0, 80, 20)
# frame = generate(0, 60, 20)

print(frame.str_ansi_24bit())

print('-'*80)

for y in range(frame.height):
    for x in range(frame.width):
        pixel = frame.data[y * frame.width + x]
        color_index = pixel[0] + (pixel[1] << 8) + (pixel[2] << 16)
        print(f"\033[48;5;{settings.ansi_8bit_lookup[color_index]}m  ", end="")
    print("\033[0m")
print('-'*80)
for y in range(frame.height):
    for x in range(frame.width):
        pixel = frame.data[y * frame.width + x]
        color_index = pixel[0] + (pixel[1] << 8) + (pixel[2] << 16)
        print(f"\033[{40 + settings.ansi_4bit_lookup[color_index]}m  ", end="")
    print("\033[0m")

print("\n" + "-" * 80 + "\n")
tags = [
    termmy.TextTag("X", (15, 18)),
    termmy.TextTag("ICE27182", color=(156, 220, 255), line_wrap=False)
]
print(frame.str_tagged(tags))

tags[-1].centered = True
tags[0].line_wrap = False
tags[0].centered = True
tags[0].text = "---**---"
print(
    frame.str_tagged(
        tags, 
        display_setting=termmy.DisplaySetting.ANSI8bit,
        color_quantization_table=settings.ansi_8bit_lookup
    )
)

