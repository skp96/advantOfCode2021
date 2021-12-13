def generate_sea_depth_list():
    depth_list = []
    with open("input.txt", "r") as sea_depth_file:
        for line in sea_depth_file:
            depth_list.append(int(line.strip()))

    return depth_list


def count_increasing_sea_depth(depth_list):
    num_increasing_depth = 0
    for depth_pos in range(1, len(depth_list)):
        if depth_list[depth_pos] > depth_list[depth_pos - 1]:
            num_increasing_depth += 1

    return num_increasing_depth


def three_measurement_sliding_window(depth_list):
    num_increasing_depth = 0
    previous_sum = 0
    current_sum = 0

    window_start = 0
    window_end = 0

    for window_end in range(len(depth_list)):
        current_sum += depth_list[window_end]

        if window_end >= 2:
            if current_sum > previous_sum:
                num_increasing_depth += 1
            previous_sum = current_sum
            current_sum -= depth_list[window_start]
            window_start += 1

    return num_increasing_depth - 1


if __name__ == "__main__":
    seaDepthList = generate_sea_depth_list()
    print(count_increasing_sea_depth(seaDepthList))
    print(three_measurement_sliding_window(seaDepthList))
