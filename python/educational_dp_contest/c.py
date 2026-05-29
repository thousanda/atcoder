N = int(input())
activities = [list(map(int, input().split())) for _ in range(N)]

# print(activities)

def solve(activities):
    happiness = {
        "from_a": activities[0][0],
        "from_b": activities[0][1],
        "from_c": activities[0][2],
    }

    for a, b, c in activities[1:]:
        a_to_b = happiness["from_a"] + b
        a_to_c = happiness["from_a"] + c
        b_to_a = happiness["from_b"] + a
        b_to_c = happiness["from_b"] + c
        c_to_a = happiness["from_c"] + a
        c_to_b = happiness["from_c"] + b

        if b_to_a > c_to_a:
            happiness["from_a"] = b_to_a
        else:
            happiness["from_a"] = c_to_a
        if a_to_b > c_to_b:
            happiness["from_b"] = a_to_b
        else:
            happiness["from_b"] = c_to_b
        if a_to_c > b_to_c:
            happiness["from_c"] = a_to_c
        else:
            happiness["from_c"] = b_to_c

    return max(happiness.values())

print(solve(activities))
