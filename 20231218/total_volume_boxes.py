def volume_compute(area, height):
    volume = area * height
    return volume

def read_lines(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    box_data = read_lines('./box_data.dat')
    print(box_data)
    volume = []
    for i in range(1, len(box_data)):
        if i == 1:
            area,height = box_data[i].split()
            volume.append(volume_compute(float(area),float(height)))
        else:
            volume.append(volume_compute(float(box_data[1].split()[1]),float(box_data[i])))
    print(volume)