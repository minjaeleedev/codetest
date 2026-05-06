from submit import Solution


def run_case(idx, box_grid, expected):
    actual = Solution().rotateTheBox([row[:] for row in box_grid])
    ok = actual == expected
    print(f"Example {idx}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        print(f"  input:    {box_grid}")
        print(f"  expected: {expected}")
        print(f"  actual:   {actual}")


def main():
    cases = [
        (
            [["#", ".", "#"]],
            [["."], ["#"], ["#"]],
        ),
        (
            [["#", ".", "*", "."], ["#", "#", "*", "."]],
            [["#", "."], ["#", "#"], ["*", "*"], [".", "."]],
        ),
        (
            [
                ["#", "#", "*", ".", "*", "."],
                ["#", "#", "#", "*", ".", "."],
                ["#", "#", "#", ".", "#", "."],
            ],
            [
                [".", "#", "#"],
                [".", "#", "#"],
                ["#", "#", "*"],
                ["#", "*", "."],
                ["#", ".", "*"],
                ["#", ".", "."],
            ],
        ),
    ]
    for i, (box_grid, expected) in enumerate(cases, 1):
        run_case(i, box_grid, expected)


if __name__ == "__main__":
    main()
