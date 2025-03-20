package sol

import (
	"reflect"
	"testing"
)

func TestMatchingStrings(t *testing.T) {
	tests := []struct {
		name       string
		stringList []string
		queries    []string
		expected   []int32
	}{
		{
			name:       "Example test case",
			stringList: []string{"aba", "baba", "aba", "xzxb"},
			queries:    []string{"aba", "xzxb", "ab"},
			expected:   []int32{2, 1, 0},
		},
		{
			name:       "Empty strings and queries",
			stringList: []string{},
			queries:    []string{},
			expected:   []int32{},
		},
		{
			name:       "Repeated strings with no matches",
			stringList: []string{"abc", "abc", "abc", "abc"},
			queries:    []string{"def", "ghi", "jkl"},
			expected:   []int32{0, 0, 0},
		},
		{
			name:       "All strings match",
			stringList: []string{"abc", "def", "ghi", "jkl"},
			queries:    []string{"abc", "def", "ghi", "jkl"},
			expected:   []int32{1, 1, 1, 1},
		},
		{
			name:       "Multiple occurrences of each query",
			stringList: []string{"a", "b", "a", "c", "b", "a"},
			queries:    []string{"a", "b", "c", "d"},
			expected:   []int32{3, 2, 1, 0},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := matchingStrings(tt.stringList, tt.queries)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("matchingStrings() = %v, want %v", result, tt.expected)
			}
		})
	}
}
