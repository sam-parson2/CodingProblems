package isBalanced

import "testing"

func TestIsBalanced(t *testing.T) {
	tests := []struct {
		input    string
		expected string
	}{
		// A balanced expression.
		{"{[()]}", "YES"},
		// An unbalanced expression.
		{"{[(])}", "NO"},
		// An empty string should be considered balanced.
		{"", "YES"},
	}

	for _, tc := range tests {
		got := isBalanced(tc.input)
		if got != tc.expected {
			t.Errorf("isBalanced(%q) = %q; expected %q", tc.input, got, tc.expected)
		}
	}
}
