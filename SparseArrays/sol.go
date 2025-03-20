package sol

func matchingStrings(stringList []string, queries []string) []int32 {
	res := make(map[string]int32)
	for _, val := range queries {
		res[val] = 0
	}

	for _, val := range stringList {
		if _, ok := res[val]; ok {
			res[val] += 1
		}

	}
	out := make([]int32, len(queries))
	for i, val := range queries {
		out[i] = res[val]
	}

	return out
}
