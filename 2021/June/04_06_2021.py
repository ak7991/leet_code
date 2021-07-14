class Solution:

    def next_states(self, current_state):
        states = []
        i = 0
        while i < len(current_state):
            state = list(current_state)
            turn = int(state[i]) + 1
            if turn == 10:
                turn = 0
            state[i] = str(turn)
            states.append(''.join(state))
            turn = int(state[i]) - 2
            if turn < 0:
                turn = 10 + turn
            state[i] = str(turn)
            states.append(''.join(state))
            i += 1
        return states

    def openLock(self, deadends, target):
        visited = set(deadends)
        stack = ["0"*len(target)]
        level = 0
        curr_level = []
        k = 0
        while stack != [] or curr_level != []:
            k += 1
            # if k > 502:
            #     print("handbrake")
            #     break
            # if level > 7:
            #     break
            print("visited", len(visited))
            # print("curr_level",  curr_level)
            print("stack", len(stack))
            if len(visited) > 6561:
                break

            curr_state = stack.pop(0)
            visited.add(curr_state) # catalog this state
            next_states = self.next_states(curr_state)
            if curr_state == "0203":
                print("===========", level, next_states)
            for state in next_states:
                if state == target:
                    print("MILLLA")
                    return level
                if state not in visited:
                    curr_level.append(state)
                    visited.add(state)
            if state == target:
                print("MILLLA")
                break
            if stack == []:
                stack = curr_level.copy()
                curr_level = []
                level += 1
        return -1


if __name__ == "__main__":
    # deadends = ["0201","0101","0102","1212","2002"]
    # target = "0050"
    # deadends = ["3"]
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"

    s = Solution()
    print(s.openLock(deadends, target))

        