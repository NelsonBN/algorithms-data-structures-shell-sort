# Algorithms and Data Structures - Shell Sort

Shell Sort is a generalization of Insertion Sort. It was created by Donald Shell in 1959.

Here an example of the [Insertion Sort](https://github.com/NelsonBN/algorithms-data-structures-insertion-sort)


## Characteristics
- Time complexity:
    - Best: Ω(n log(n)) -> Depends on the gap sequence
    - Average: Θ(n^(3/2)) -> Depends on the gap sequence
    - Worst: O(n^2) -> Depends on the gap sequence
- Space complexity: O(1)
- In-place
- Unstable


## Demos:
- [Original Implementation](./src/basic.py)
- [Knuth's Sequence](./src/knuth.py)
- [Hibbard's Sequence](./src/hibbard.py)
- [Sedgewick's Sequence](./src/sedgewick.py)
- [Comparisons all versions](./src/comparisons.py)


## Demonstration
- [Algorithm Visualizer](https://algorithm-visualizer.org/brute-force/shellsort)


## References
- [Other algoritmos & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
- [A High-Speed Sorting Procedure - D.L. Shell](https://dl.acm.org/doi/pdf/10.1145/368370.368387)
