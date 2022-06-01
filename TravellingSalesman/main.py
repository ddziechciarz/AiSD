import math


class City:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def calc_dist(self, other):
        return math.dist([self.x, self.y], [other.x, other.y])

    def find_nearest_neigh(self, other_cities):
        shortest_dist = math.inf
        shortest_index = self.index
        for city in other_cities:
            if city is not None:
                if self.calc_dist(city) < shortest_dist:
                    shortest_dist = self.calc_dist(city)
                    shortest_index = city.index
        return shortest_index


def load_data():
    cities = []
    with open("TSP.txt") as f:
        for line in f:
            line = line.split()
            cities.append(City(int(line[0]), float(line[1]), float(line[2])))
    return cities


def fast_sol(city_list: list[City]):
    total_len = 0
    for i in range(1, len(city_list)):
        total_len += city_list[i].calc_dist(city_list[i - 1])
    total_len += city_list[i].calc_dist(city_list[0])
    return total_len


def nearest_neigh(city_list: list[City]):
    current_point = city_list[0]
    route = "1, "
    cities_left = city_list[1:]
    num_of_visited_cities = 0
    total_len = 0

    while num_of_visited_cities < len(city_list) - 1:
        nearest_index = current_point.find_nearest_neigh(cities_left) - 1
        total_len += current_point.calc_dist(city_list[nearest_index])
        route += f"{city_list[nearest_index].index}, "
        num_of_visited_cities += 1
        cities_left[nearest_index - 1] = None
        current_point = city_list[nearest_index]

    total_len += current_point.calc_dist(city_list[0])

    print(total_len)
    return route


if __name__ == '__main__':
    cities = load_data()
    print(nearest_neigh(cities))
    print(fast_sol(cities))