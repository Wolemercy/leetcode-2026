# https://leetcode.com/problems/separate-squares-ii

from bisect import bisect_left


# I have no idea what is going on here. It's something to do with segment trees and line sweeping.
# TODO: Review this problem again later
class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.cover = [0] * (4 * self.n)
        self.length = [0] * (4 * self.n)

    def _push_up(self, idx: int, lo: int, hi: int) -> None:
        if self.cover[idx] > 0:
            self.length[idx] = self.xs[hi + 1] - self.xs[lo]
        elif lo == hi:
            self.length[idx] = 0
        else:
            self.length[idx] = self.length[idx * 2 + 1] + self.length[idx * 2 + 2]

    def _add(self, idx: int, lo: int, hi: int, ql: int, qh: int, delta: int) -> None:
        if qh < lo or hi < ql:
            return
        if ql <= lo and hi <= qh:
            self.cover[idx] += delta
            self._push_up(idx, lo, hi)
            return
        mid = (lo + hi) // 2
        self._add(idx * 2 + 1, lo, mid, ql, qh, delta)
        self._add(idx * 2 + 2, mid + 1, hi, ql, qh, delta)
        self._push_up(idx, lo, hi)

    def add_interval(self, x1: int, x2: int, delta: int) -> None:
        if self.n <= 0:
            return
        l = bisect_left(self.xs, x1)
        r = bisect_left(self.xs, x2) - 1
        if l <= r:
            self._add(0, 0, self.n - 1, l, r, delta)

    def covered_length(self) -> int:
        return self.length[0] if self.n > 0 else 0


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        luntrivexi = squares

        events = []
        xs = set()

        for x, y, l in squares:
            x2 = x + l
            y2 = y + l
            events.append((y, 1, x, x2))
            events.append((y2, -1, x, x2))
            xs.add(x)
            xs.add(x2)

        events.sort()
        xs = sorted(xs)

        def total_union_area() -> float:
            st = SegmentTree(xs)
            area = 0.0
            prev_y = events[0][0]
            i = 0
            while i < len(events):
                y = events[i][0]
                covered = st.covered_length()
                area += covered * (y - prev_y)

                # apply all events at this y
                while i < len(events) and events[i][0] == y:
                    _, delta, x1, x2 = events[i]
                    st.add_interval(x1, x2, delta)
                    i += 1

                prev_y = y
            return area

        total = total_union_area()
        half = total / 2.0

        st = SegmentTree(xs)
        prefix = 0.0
        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]
            covered = st.covered_length()
            gain = covered * (y - prev_y)

            if covered > 0 and prefix + gain >= half:
                return prev_y + (half - prefix) / covered

            prefix += gain

            while i < len(events) and events[i][0] == y:
                _, delta, x1, x2 = events[i]
                st.add_interval(x1, x2, delta)
                i += 1

            prev_y = y

        return float(prev_y)
