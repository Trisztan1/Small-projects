import csv

def main():
    all_x_points = []
    all_y_points = []
    get_range = fget_range()
    strt_value = get_range[0]

    for i in range(get_range[0], get_range[1]):
        x_points = []
        y_points = []
        y_point = strt_value
        counter = 1

        while y_point != 1:
            if y_point == strt_value:
                y_points.append(y_point)
                x_points.append(counter)
                counter += 1

            y_point = rules(y_point)
            y_points.append(y_point)
            x_points.append(counter)
            counter += 1
        
        strt_value += 1
        all_x_points.append(x_points)
        all_y_points.append(y_points)

    for i in range(len(all_x_points)):
        with open(f"./data/{i+1}_x_data_points.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([[x] for x in all_x_points[i]])
        
        with open(f"./data/{i+1}_y_data_points.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([[y] for y in all_y_points[i]])


    


def rules(n: int):
    if n % 2 == 0:
        return int(n/2)
    elif n % 2 == 1:
        return int(n*3+1)
    else:
        raise Exception(f"n % 2 = {n % 2}")

def fget_range(start: int | None = None, end: int | None = None):
    if start and end:
        return (start, end+1)
    else:
        try:
            start = int(input("Number to start: "))
            end = int(input("Number to end: "))
        except ValueError:
            raise
    return (start, end+1)
    


if __name__ == "__main__":
    main()