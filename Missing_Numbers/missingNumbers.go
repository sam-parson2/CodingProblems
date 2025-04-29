package main

import (
	"sort"
)

func missingNumbers(arr []int32, brr []int32) []int32 {
	if len(arr) == 0 {
		result := make([]int32, len(brr))
		copy(result, brr)
		sort.Slice(result, func(i, j int) bool { return result[i] > result[j] })
		return result
	}
	if len(brr) == 0 {
		result := make([]int32, len(arr))
		copy(result, arr)
		sort.Slice(result, func(i, j int) bool { return result[i] > result[j] })
		return result
	}

	createCounter := func(collection []int32) map[int32]int32 {
		freqs := make(map[int32]int32)
		for _, v := range collection {
			if _, ok := freqs[v]; ok {
				freqs[v] += 1
			} else {
				freqs[v] = 1
			}
		}
		return freqs
	}
	checkEquality := func(base, comparison map[int32]int32) []int32 {
		res := []int32{}
		for k, v := range base {
			if _, ok := base[k]; ok {
				if _, exists := comparison[k]; !exists {
					res = append(res, k)
				} else if comparison[k] != v {
					res = append(res, k)
				}
			}
		}
		sort.Slice(res, func(i, j int) bool { return res[i] < res[j] })
		return res
	}
	return checkEquality(createCounter(brr), createCounter(arr))
}
