package ArrayManip

import "math"

func ArrayManipulation(n int32, queries [][]int32) int64 {
	base := make([]int32, n+2)
	for _, v := range queries {
		base[v[0]] += v[2]
		base[v[1]+1] -= v[2]
	}
	mx, acc := 0, 0
	for _, val := range base {
		acc += int(val)
		mx = int(math.Max(float64(mx), float64(acc)))
	}
	return int64(mx)
}
