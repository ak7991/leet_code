import numpy as np

WORST_CASE_DISTANCE = 12 * 20

class Solution:
    
    # Takes best route and generates superstring
    def ans_generator(self, words, route, distance_matrix):
        prev = route[0]
        ans = words[route[0]]
        for curr in route[1:]:
            distance = distance_matrix[curr][prev]

            _ans = self.create_superstring(ans, words[curr], distance)
            ans  = _ans
            prev = curr
        return ans

    # Generate a superstring given two strings and their distance
    def create_superstring(self, w1, w2, distance):
        if len(w1) <= len(w2):
            short_w = w1
            long_w = w2
        else:
            short_w = w2
            long_w = w1
        len_sw = len(short_w)
        superstring = long_w + short_w[-1*distance:]
        if short_w == long_w[-1*len_sw]:
            pass
        else:
            superstring = short_w[:distance] + long_w
        return superstring
                
    # Computes letters to add to w2 for w1 to be "inside" w2
    def distance_calculator(self, w1, w2):
        """
        How many letters should be added to the longer word so that 
        the shorter word fits inside it.
        """
        if len(w1) <= len(w2):
            short_w = w1
            long_w = w2
        else:
            short_w = w2
            long_w = w1
        distance = len_sw = len(short_w)
        i = 0
        while i < len_sw:
            if (short_w[i:] == long_w[:len_sw-i]) or (short_w[:len_sw-i] == long_w[-1*(len_sw-i):]):
                distance = i
                break
            else:
                pass
                # print("..?")
                # print(w1, w2)
            i += 1 
        return distance
    
    # Accepts a words iterable with *distinct* words
    def create_distance_matrix(self, words):
        """
        Create a distance matrix between every possible combination.
        Every combination is = take two elements from set of words for 
        distance computation
        """
        distance_matrix = np.zeros((len(words), len(words)), dtype="uint8")
        for w1_i, w1 in enumerate(words):
            for w2_i, w2 in enumerate(words):
                if w1 != w2:
                    distance = self.distance_calculator(w1, w2)
                    distance_matrix[w1_i, w2_i] = distance
                    distance_matrix[w2_i, w1_i] = distance
                else:
                    distance_matrix[w2_i, w1_i] = 0
        return distance_matrix
                    
    # Recursive method to compute best distance given a start and end point
    def calc_route(self, start_i, end_i, journey_node_indices, distance_matrix):
        """
        Follows recursion algorithm:
        calc_route for [1, 2, 0] starting from 1 and ending at 0 == 
        calc_route for [1, 2] + calc_route for [2, 0]

        If no nodes left between start and end => return the distance 
        between them with best route = start -> end
        """
        # Stop recursion is no nodes left to traverse
        if len(journey_node_indices) == 0:
            return distance_matrix[start_i][end_i], [start_i, end_i]
        
        min_dist = WORST_CASE_DISTANCE
        route = []
        for node_index in journey_node_indices:
            alt_node_indices = journey_node_indices.copy()
            alt_node_indices.remove(node_index)
            # distance from (end's successor) to end
            existing_dist, e_r = self.calc_route(node_index, end_i, [], distance_matrix)
            # distance from "here" to (end's successor)
            curr_dist, c_r = self.calc_route(start_i, node_index, alt_node_indices, distance_matrix)
            route_distance = curr_dist + existing_dist
            if route_distance < min_dist:
                min_dist = route_distance
                c_r.append(e_r[1])
                route = c_r.copy()
        return min_dist, route

    def shortestSuperstring(self, words) -> str:
        words = list(set(words))
        # create distance matrix; save computation
        distance_matrix = self.create_distance_matrix(words) 
        min_dist = WORST_CASE_DISTANCE # max
        best_route = [] # store route with least "cost"
        initial_node_indices = [] # should have [1, 2, ...len(words)-1]
        j = 1
        for word in words[1:]:
            initial_node_indices.append(j)
            j += 1

        # Traversing
        i = 1
        while i < len(words):
            curr_node_indices = initial_node_indices.copy()
            curr_node_indices.remove(i)
            min_dist_for_node, best_route_for_node = self.calc_route(i, 0, curr_node_indices, distance_matrix)
            if min_dist_for_node < min_dist:
                min_dist = min_dist_for_node
                best_route = best_route_for_node
            i += 1
        
        ans = self.ans_generator(words, best_route, distance_matrix)
        # print(f"best_route {best_route} generated answer: {ans}")
        return ans


                    
if __name__ == "__main__":
    s = Solution()
    words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    words = ["alex","loves","leetcode"]
    a = s.shortestSuperstring(words)