package DynamicArray

// https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true

func dynamicArray(n int32, queries [][]int32) []int32 {
	// O(n + q)
	var ans int32
	res := make([]int32, 0, n)
	XOR := func(x, y int32) int32 {
		return x ^ y
	}
	nested_arrs := make([][]int32, n)
	compute_ans := func(x, y, last int32, collection [][]int32) int32 {
		return collection[XOR(x, last)%n][int(y)%len(collection[XOR(x, last)%n])]
	}
	for _, query := range queries {
		if query[0] == 1 {
			nested_arrs[XOR(query[1], ans)%n] = append(nested_arrs[XOR(query[1], ans)%n], query[2])
		}
		if query[0] == 2 {
			ans = compute_ans(query[1], query[2], ans, nested_arrs)
			res = append(res, ans)
		}
	}
	return res
}
