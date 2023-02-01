from stack import brackets_check
import pytest

testcases_pos = [
	"(((([{}]))))",
	"[([])((([[[]]])))]{()}",
	"{{[()]}}"
]

testcases_neg = [
	"}{}",
	"{{[(])]}}",
	"[[{())}]",
	"{[(([])])}"
]


@pytest.mark.parametrize('_input', testcases_pos)
def test_pos(_input):
	res = brackets_check(_input)
	assert res == 'Сбалансировано'

# @pytest.mark.xfail
@pytest.mark.parametrize('_input', testcases_neg)
def test_neg(_input):
	res = brackets_check(_input)
	assert res == 'Несбалансировано'
