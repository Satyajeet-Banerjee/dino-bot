def detect_obstacle(image):
    pixels = image.load()
    width, height = image.size

    y = int(height * 0.70)

    # scan only front area
    for x in range(int(width * 0.60), int(width * 0.80)):
        r, g, b = pixels[x, y]

        if r < 140 and g < 140 and b < 140:
            return True

    return False