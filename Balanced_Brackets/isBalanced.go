package isBalanced

func isBalanced(s string) string {
	stack := make([]rune, 0, len(s)) // If you give it initial size it gets filled with the zero element for the type that structure is
	lft := make(map[rune]bool)
	lft['{'] = true
	lft['['] = true
	lft['('] = true
	pop := func(stk *[]rune) rune {
		ele := (*stk)[len(*stk)-1] // needs pointers else you work with a copy
		*stk = (*stk)[:len(*stk)-1]
		return ele
	}
	for _, c := range s {
		if lft[c] {
			stack = append(stack, c)
			continue
		}
		if len(stack) == 0 {
			return "NO"
		}
		switch val := pop(&stack); val {
		case '{':
			if c != '}' {
				return "NO"
			}
		case '[':
			if c != ']' {
				return "NO"
			}
		case '(':
			if c != ')' {
				return "NO"
			}
		}
	}
	if len(stack) == 0 {
		return "YES"
	}
	return "NO"
}
