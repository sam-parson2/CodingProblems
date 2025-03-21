package ArrayManip

import (
	"testing"
)

func TestArrayManipulation(t *testing.T) {
	testCases := []struct {
		name     string
		n        int32
		queries  [][]int32
		expected int64
	}{
		{
			name:     "Simple case with one operation",
			n:        5,
			queries:  [][]int32{{1, 3, 100}},
			expected: 100,
		},
		{
			name:     "Multiple operations",
			n:        10,
			queries:  [][]int32{{1, 5, 3}, {4, 8, 7}, {6, 9, 1}},
			expected: 10,
		},
		{
			name:     "Larger numbers",
			n:        10,
			queries:  [][]int32{{2, 6, 8}, {3, 5, 7}, {1, 8, 1}, {5, 9, 15}},
			expected: 31,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := ArrayManipulation(tc.n, tc.queries)
			if result != tc.expected {
				t.Errorf("Expected %d, got %d", tc.expected, result)
			}
		})
	}
}
